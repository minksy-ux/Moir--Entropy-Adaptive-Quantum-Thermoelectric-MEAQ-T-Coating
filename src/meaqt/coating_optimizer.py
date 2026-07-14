from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Literal

import pandas as pd


@dataclass(frozen=True)
class LayerOption:
    name: str
    heat_tol: float
    radiation_tol: float
    healing_rate: float
    thermal_kappa_wmk: float
    coupling: float


PROTECTIVE_OPTIONS = [
    LayerOption("bio_vitrimer_imine_sio2_2wt", 0.48, 0.36, 0.96, 0.32, 0.62),
    LayerOption("polyimine_vanillin_priamine", 0.42, 0.33, 0.94, 0.30, 0.58),
    LayerOption("hfb2_sic_tasi2_uhtc", 0.99, 0.94, 0.42, 4.50, 0.52),
    LayerOption("yb2si2o7_sic", 0.86, 0.82, 0.65, 2.10, 0.58),
]

INTERLAYER_OPTIONS = [
    LayerOption("he_rocksalt_mg_co_ni_cu_zn_o", 0.82, 0.78, 0.26, 1.08, 0.70),
    LayerOption("he_oxide_hf_zr_ta_nb_ti", 0.84, 0.80, 0.30, 1.25, 0.72),
    LayerOption("he_perovskite_sr_la_nd_sm_eu_tio3", 0.77, 0.71, 0.22, 0.95, 0.83),
    LayerOption("he_carbide_hf_zr_nb_ta", 0.95, 0.88, 0.24, 1.75, 0.66),
    LayerOption("zintl_multication", 0.65, 0.57, 0.20, 0.65, 0.80),
]

MOIRE_OPTIONS = [
    LayerOption("mote2_wse2_hbn", 0.32, 0.30, 0.10, 0.45, 1.00),
    LayerOption("wse2_twist_hbn", 0.36, 0.34, 0.10, 0.42, 0.93),
]

SUBSTRATE_OPTIONS = [
    LayerOption("he_ceramic", 0.90, 0.86, 0.20, 2.50, 0.70),
    LayerOption("sic_composite", 0.88, 0.80, 0.25, 3.80, 0.74),
]


WEIGHT_PRESETS = {
    "balanced": {
        "heat_tol": 0.24,
        "radiation_tol": 0.20,
        "healing_rate": 0.22,
        "coupling": 0.22,
        "low_kappa": 0.12,
    },
    "prototype_low_temp": {
        "heat_tol": 0.18,
        "radiation_tol": 0.14,
        "healing_rate": 0.34,
        "coupling": 0.22,
        "low_kappa": 0.12,
    },
    "extreme_uht": {
        "heat_tol": 0.34,
        "radiation_tol": 0.26,
        "healing_rate": 0.10,
        "coupling": 0.20,
        "low_kappa": 0.10,
    },
}

REQUIRED_WEIGHT_KEYS = {"heat_tol", "radiation_tol", "healing_rate", "coupling", "low_kappa"}


def _stack_score(row: pd.Series, weights: dict[str, float]) -> float:
    low_kappa_score = 1.0 / max(row["thermal_kappa_wmk"], 1e-6)
    return (
        weights["heat_tol"] * row["heat_tol"]
        + weights["radiation_tol"] * row["radiation_tol"]
        + weights["healing_rate"] * row["healing_rate"]
        + weights["coupling"] * row["coupling"]
        + weights["low_kappa"] * low_kappa_score
    )


def _normalize(series: pd.Series) -> pd.Series:
    span = float(series.max() - series.min())
    if span < 1e-12:
        return pd.Series(1.0, index=series.index)
    return (series - series.min()) / span


def _apply_constraints(
    df: pd.DataFrame,
    min_heat_tol: float | None,
    min_radiation_tol: float | None,
    min_healing_rate: float | None,
    max_thermal_kappa_wmk: float | None,
    min_coupling: float | None,
) -> pd.DataFrame:
    mask = pd.Series(True, index=df.index)
    if min_heat_tol is not None:
        mask &= df["heat_tol"] >= min_heat_tol
    if min_radiation_tol is not None:
        mask &= df["radiation_tol"] >= min_radiation_tol
    if min_healing_rate is not None:
        mask &= df["healing_rate"] >= min_healing_rate
    if max_thermal_kappa_wmk is not None:
        mask &= df["thermal_kappa_wmk"] <= max_thermal_kappa_wmk
    if min_coupling is not None:
        mask &= df["coupling"] >= min_coupling
    return df.loc[mask].reset_index(drop=True)


def optimize_stacks(
    weights: dict[str, float] | None = None,
    top_k: int = 10,
    preset: str = "balanced",
    score_mode: Literal["raw", "normalized"] = "raw",
    min_heat_tol: float | None = None,
    min_radiation_tol: float | None = None,
    min_healing_rate: float | None = None,
    max_thermal_kappa_wmk: float | None = None,
    min_coupling: float | None = None,
) -> pd.DataFrame:
    if top_k <= 0:
        raise ValueError("top_k must be a positive integer")

    if weights is None:
        if preset not in WEIGHT_PRESETS:
            raise ValueError(f"Unknown preset '{preset}'. Available presets: {sorted(WEIGHT_PRESETS)}")
        weights = WEIGHT_PRESETS[preset]
    else:
        missing = REQUIRED_WEIGHT_KEYS.difference(weights.keys())
        extra = set(weights.keys()).difference(REQUIRED_WEIGHT_KEYS)
        if missing or extra:
            raise ValueError(
                "weights must contain exactly keys "
                f"{sorted(REQUIRED_WEIGHT_KEYS)}; missing={sorted(missing)}, extra={sorted(extra)}"
            )

    rows = []
    for protective, interlayer, moire, substrate in product(
        PROTECTIVE_OPTIONS,
        INTERLAYER_OPTIONS,
        MOIRE_OPTIONS,
        SUBSTRATE_OPTIONS,
    ):
        parts = [protective, interlayer, moire, substrate]
        row = {
            "protective": protective.name,
            "interlayer": interlayer.name,
            "moire": moire.name,
            "substrate": substrate.name,
            "heat_tol": sum(p.heat_tol for p in parts) / len(parts),
            "radiation_tol": sum(p.radiation_tol for p in parts) / len(parts),
            "healing_rate": sum(p.healing_rate for p in parts) / len(parts),
            "thermal_kappa_wmk": sum(p.thermal_kappa_wmk for p in parts) / len(parts),
            "coupling": sum(p.coupling for p in parts) / len(parts),
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df = _apply_constraints(
        df,
        min_heat_tol=min_heat_tol,
        min_radiation_tol=min_radiation_tol,
        min_healing_rate=min_healing_rate,
        max_thermal_kappa_wmk=max_thermal_kappa_wmk,
        min_coupling=min_coupling,
    )
    if df.empty:
        return df

    df["score_raw"] = df.apply(lambda r: _stack_score(r, weights), axis=1)
    if score_mode == "raw":
        df["score"] = df["score_raw"]
    elif score_mode == "normalized":
        inv_kappa = 1.0 / df["thermal_kappa_wmk"].clip(lower=1e-6)
        df["score"] = (
            weights["heat_tol"] * _normalize(df["heat_tol"])
            + weights["radiation_tol"] * _normalize(df["radiation_tol"])
            + weights["healing_rate"] * _normalize(df["healing_rate"])
            + weights["coupling"] * _normalize(df["coupling"])
            + weights["low_kappa"] * _normalize(inv_kappa)
        )
    else:
        raise ValueError("score_mode must be 'raw' or 'normalized'")

    return df.sort_values("score", ascending=False).head(top_k).reset_index(drop=True)


def pareto_front(df: pd.DataFrame, maximize: list[str], minimize: list[str]) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    keep = []
    for i, row_i in df.iterrows():
        dominated = False
        for j, row_j in df.iterrows():
            if i == j:
                continue
            better_or_equal = all(row_j[m] >= row_i[m] for m in maximize) and all(
                row_j[m] <= row_i[m] for m in minimize
            )
            strictly_better = any(row_j[m] > row_i[m] for m in maximize) or any(
                row_j[m] < row_i[m] for m in minimize
            )
            if better_or_equal and strictly_better:
                dominated = True
                break
        if not dominated:
            keep.append(i)
    return df.loc[keep].reset_index(drop=True)
