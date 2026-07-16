from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from meaqt.coating_optimizer import WEIGHT_PRESETS, optimize_stacks, pareto_front
from meaqt.composition import R_GAS, config_entropy, screen_compositions
from meaqt.dft_adapters import parse_dft_report, parse_dft_text
from meaqt.moire_transport import scan_moire_response
from meaqt.plotting import save_moire_heatmap, save_pareto_scatter
from meaqt.pulse_response import simulate_pulse_switching

ROOT = Path(__file__).resolve().parents[1]


def test_config_entropy_equiatomic_5() -> None:
    comp = {k: 0.2 for k in ["Hf", "Zr", "Ta", "Nb", "Ti"]}
    s_mix = config_entropy(comp)
    assert np.isclose(s_mix / R_GAS, np.log(5), rtol=1e-6)


def test_screen_compositions_has_rows() -> None:
    df = screen_compositions(n_elements=5, top_k=10)
    assert len(df) > 0
    assert (df["score"] >= 0.0).all()
    assert (df["S_mix_over_R"] >= 1.5).all()


def test_moire_scan_shape_and_columns() -> None:
    theta = np.array([0.8, 1.6])
    displacement = np.array([-0.2, 0.2])
    temp = np.array([25.0])
    df = scan_moire_response(theta, displacement, temp, filling=0.1)
    assert len(df) == 4
    assert {"seebeck_uV_per_K", "power_factor_arb", "nernst_proxy"}.issubset(df.columns)


def test_pulse_switching_default_true() -> None:
    result = simulate_pulse_switching()
    assert result["switched"] is True


def test_coating_presets_available_and_scored() -> None:
    assert "balanced" in WEIGHT_PRESETS
    assert "prototype_low_temp" in WEIGHT_PRESETS
    assert "extreme_uht" in WEIGHT_PRESETS
    ranked = optimize_stacks(top_k=6, preset="balanced")
    assert len(ranked) == 6
    assert ranked["score"].is_monotonic_decreasing


def test_coating_optimizer_normalized_score_mode() -> None:
    ranked = optimize_stacks(top_k=8, preset="balanced", score_mode="normalized")
    assert len(ranked) == 8
    assert ranked["score"].between(0.0, 1.0).all()
    assert "score_raw" in ranked.columns


def test_coating_optimizer_constraints_are_applied() -> None:
    ranked = optimize_stacks(
        top_k=20,
        preset="balanced",
        min_heat_tol=0.75,
        min_radiation_tol=0.70,
        max_thermal_kappa_wmk=2.0,
    )
    assert len(ranked) > 0
    assert (ranked["heat_tol"] >= 0.75).all()
    assert (ranked["radiation_tol"] >= 0.70).all()
    assert (ranked["thermal_kappa_wmk"] <= 2.0).all()


def test_dft_parser_vasp_and_qe_samples() -> None:
    vasp_text = (ROOT / "data/benchmarks/vasp_sample.out").read_text(encoding="utf-8")
    qe_text = (ROOT / "data/benchmarks/qe_sample.out").read_text(encoding="utf-8")

    vasp = parse_dft_text(vasp_text, code="auto")
    qe = parse_dft_text(qe_text, code="auto")

    assert vasp.code == "vasp"
    assert np.isclose(vasp.fermi_ev, 5.4321)
    assert np.isclose(vasp.total_energy_ev, -123.456789)

    assert qe.code == "qe"
    assert np.isclose(qe.fermi_ev, 3.2100)
    assert qe.total_energy_ev is not None
    assert qe.total_energy_ev < 0.0


def test_dft_report_confidence_range() -> None:
    vasp_text = (ROOT / "data/benchmarks/vasp_sample.out").read_text(encoding="utf-8")
    report = parse_dft_report(vasp_text, code="auto")
    assert 0.0 <= report.confidence <= 1.0
    assert report.summary.code == "vasp"


def test_expected_ranges_file_exists_and_valid_json() -> None:
    payload = json.loads((ROOT / "data/benchmarks/expected_ranges.json").read_text(encoding="utf-8"))
    assert payload["composition"]["min_smix_over_r"] >= 1.5


def test_optimizer_golden_top_rank_per_preset() -> None:
    golden = json.loads((ROOT / "data/benchmarks/coating_preset_golden.json").read_text(encoding="utf-8"))
    for preset, expected in golden.items():
        top = optimize_stacks(top_k=1, preset=preset).iloc[0]
        assert top["protective"] == expected["protective"]
        assert top["interlayer"] == expected["interlayer"]
        assert top["moire"] == expected["moire"]
        assert top["substrate"] == expected["substrate"]


def test_plot_outputs_are_created(tmp_path: Path) -> None:
    df = scan_moire_response(
        theta_grid=np.array([0.8, 1.2]),
        displacement_grid=np.array([-0.2, 0.2]),
        temp_grid=np.array([25.0]),
        filling=0.1,
    )
    heatmap_path = tmp_path / "seebeck.png"
    save_moire_heatmap(df, "seebeck_uV_per_K", 25.0, str(heatmap_path))
    assert heatmap_path.exists()
    assert heatmap_path.stat().st_size > 100

    ranked = optimize_stacks(top_k=6, preset="balanced")
    scatter_path = tmp_path / "coating_scatter.png"
    save_pareto_scatter(ranked, str(scatter_path))
    assert scatter_path.exists()
    assert scatter_path.stat().st_size > 100


def test_compare_preset_script_outputs(tmp_path: Path) -> None:
    out_side = tmp_path / "side.csv"
    out_rank = tmp_path / "rank.csv"
    out_ranked = tmp_path / "ranked.csv"
    script = ROOT / "scripts/compare_coating_presets.py"

    subprocess.run(
        [
            sys.executable,
            str(script),
            "--left",
            "prototype_low_temp",
            "--right",
            "extreme_uht",
            "--top-k",
            "6",
            "--out-side",
            str(out_side),
            "--out-by-rank",
            str(out_rank),
            "--out-ranked",
            str(out_ranked),
        ],
        check=True,
        cwd=str(ROOT),
    )

    for p in [out_side, out_rank, out_ranked]:
        assert p.exists()
        df = pd.read_csv(p)
        assert len(df) > 0


def test_coating_opt_script_outputs(tmp_path: Path) -> None:
    out_ranked = tmp_path / "coating_ranked.csv"
    out_pareto = tmp_path / "coating_pareto.csv"
    script = ROOT / "scripts/run_coating_opt.py"

    subprocess.run(
        [
            sys.executable,
            str(script),
            "--preset",
            "balanced",
            "--score-mode",
            "normalized",
            "--top-k",
            "6",
            "--out",
            str(out_ranked),
            "--out-pareto",
            str(out_pareto),
        ],
        check=True,
        cwd=str(ROOT),
    )

    ranked = pd.read_csv(out_ranked)
    pareto = pd.read_csv(out_pareto)
    assert len(ranked) == 6
    assert 0 < len(pareto) <= len(ranked)
    assert {"score", "score_raw", "protective", "interlayer", "moire", "substrate"}.issubset(ranked.columns)


def test_optimize_stacks_invalid_top_k_raises() -> None:
    with pytest.raises(ValueError, match="top_k"):
        optimize_stacks(top_k=0)


def test_optimize_stacks_invalid_weight_keys_raise() -> None:
    with pytest.raises(ValueError, match="weights"):
        optimize_stacks(weights={"heat_tol": 1.0}, top_k=2)


def test_pareto_front_empty_input() -> None:
    empty = pd.DataFrame(columns=["heat_tol", "radiation_tol", "thermal_kappa_wmk"])
    out = pareto_front(empty, maximize=["heat_tol", "radiation_tol"], minimize=["thermal_kappa_wmk"])
    assert out.empty
    assert list(out.columns) == list(empty.columns)
