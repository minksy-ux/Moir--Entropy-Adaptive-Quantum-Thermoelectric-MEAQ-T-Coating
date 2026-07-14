#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from meaqt.coating_optimizer import optimize_stacks, pareto_front
from meaqt.moire_transport import scan_moire_response
from meaqt.plotting import save_moire_heatmap, save_pareto_scatter, save_pulse_trajectory
from meaqt.pulse_response import simulate_pulse_switching


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate MEAQ-T plotting outputs")
    parser.add_argument("--out-dir", type=str, default="figures")
    parser.add_argument("--filling", type=float, default=0.1)
    parser.add_argument("--temp", type=float, default=50.0, help="Temperature for heatmaps")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    theta = np.linspace(0.4, 3.0, 21)
    displacement = np.linspace(-0.5, 0.5, 21)
    temp = np.array([args.temp])
    moire_df = scan_moire_response(theta, displacement, temp, filling=args.filling)
    moire_df.to_csv(out_dir / "moire_grid.csv", index=False)
    save_moire_heatmap(moire_df, "seebeck_uV_per_K", args.temp, str(out_dir / "seebeck_map.png"))
    save_moire_heatmap(moire_df, "power_factor_arb", args.temp, str(out_dir / "power_factor_map.png"))

    pulse = simulate_pulse_switching()
    save_pulse_trajectory(pulse["time_ps"], pulse["m"], str(out_dir / "pulse_trajectory.png"))

    ranked = optimize_stacks(top_k=20)
    pf = pareto_front(
        ranked,
        maximize=["heat_tol", "radiation_tol", "healing_rate", "coupling"],
        minimize=["thermal_kappa_wmk"],
    )
    ranked.to_csv(out_dir / "coating_ranked.csv", index=False)
    pf.to_csv(out_dir / "coating_pareto.csv", index=False)
    save_pareto_scatter(ranked, str(out_dir / "coating_scatter.png"))

    print(f"Saved outputs under {out_dir}")


if __name__ == "__main__":
    main()
