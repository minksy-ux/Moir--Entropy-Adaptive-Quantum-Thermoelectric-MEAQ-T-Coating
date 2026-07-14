from __future__ import annotations

from itertools import combinations
from typing import Iterable

import numpy as np
import pandas as pd

R_GAS = 8.314462618  # J/mol-K

# Lightweight descriptor table for first-pass screening.
ELEMENT_DB = {
    "Hf": {"radius_pm": 159.0, "chi": 1.30, "tm_k": 2506.0},
    "Zr": {"radius_pm": 160.0, "chi": 1.33, "tm_k": 2128.0},
    "Ta": {"radius_pm": 146.0, "chi": 1.50, "tm_k": 3290.0},
    "Nb": {"radius_pm": 146.0, "chi": 1.60, "tm_k": 2750.0},
    "Ti": {"radius_pm": 147.0, "chi": 1.54, "tm_k": 1941.0},
    "Mo": {"radius_pm": 139.0, "chi": 2.16, "tm_k": 2896.0},
    "W": {"radius_pm": 139.0, "chi": 2.36, "tm_k": 3695.0},
    "Si": {"radius_pm": 111.0, "chi": 1.90, "tm_k": 1687.0},
    "Al": {"radius_pm": 143.0, "chi": 1.61, "tm_k": 933.0},
    "Y": {"radius_pm": 180.0, "chi": 1.22, "tm_k": 1799.0},
    "Yb": {"radius_pm": 194.0, "chi": 1.10, "tm_k": 1097.0},
}


def config_entropy(composition: dict[str, float]) -> float:
    """Ideal configurational entropy in J/mol-K."""
    x = np.array(list(composition.values()), dtype=float)
    return float(-R_GAS * np.sum(x * np.log(x + 1e-12)))


def radius_mismatch(composition: dict[str, float]) -> float:
    """Atomic-radius mismatch as a distortion proxy (higher can lower kappa_L)."""
    radii = np.array([ELEMENT_DB[e]["radius_pm"] for e in composition], dtype=float)
    fractions = np.array(list(composition.values()), dtype=float)
    r_avg = np.sum(fractions * radii)
    mismatch = np.sqrt(np.sum(fractions * (1.0 - radii / r_avg) ** 2))
    return float(mismatch)


def average_melting_point(composition: dict[str, float]) -> float:
    temps = np.array([ELEMENT_DB[e]["tm_k"] for e in composition], dtype=float)
    fractions = np.array(list(composition.values()), dtype=float)
    return float(np.sum(fractions * temps))


def electronegativity_spread(composition: dict[str, float]) -> float:
    chi = np.array([ELEMENT_DB[e]["chi"] for e in composition], dtype=float)
    fractions = np.array(list(composition.values()), dtype=float)
    chi_avg = np.sum(fractions * chi)
    return float(np.sqrt(np.sum(fractions * (chi - chi_avg) ** 2)))


def _normalize(series: pd.Series) -> pd.Series:
    span = float(series.max() - series.min())
    if span < 1e-12:
        return pd.Series(np.ones(len(series)), index=series.index)
    return (series - series.min()) / span


def screen_compositions(
    elements: Iterable[str] | None = None,
    n_elements: int = 5,
    min_entropy_r: float = 1.5,
    top_k: int = 50,
) -> pd.DataFrame:
    """Enumerate equiatomic combinations and rank with simple physics proxies."""
    selected = list(elements) if elements is not None else list(ELEMENT_DB.keys())
    if n_elements < 2:
        raise ValueError("n_elements must be >= 2")
    if n_elements > len(selected):
        raise ValueError("n_elements exceeds number of available elements")

    rows: list[dict[str, float | str]] = []
    for combo in combinations(selected, n_elements):
        frac = 1.0 / n_elements
        comp = {el: frac for el in combo}
        s_mix = config_entropy(comp)
        if s_mix < min_entropy_r * R_GAS:
            continue
        rows.append(
            {
                "composition": "-".join(combo),
                "S_mix_J_molK": s_mix,
                "S_mix_over_R": s_mix / R_GAS,
                "radius_mismatch": radius_mismatch(comp),
                "avg_tm_k": average_melting_point(comp),
                "chi_spread": electronegativity_spread(comp),
            }
        )

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    df["score"] = (
        0.35 * _normalize(df["S_mix_over_R"])
        + 0.30 * _normalize(df["radius_mismatch"])
        + 0.25 * _normalize(df["avg_tm_k"])
        + 0.10 * _normalize(df["chi_spread"])
    )
    return df.sort_values("score", ascending=False).head(top_k).reset_index(drop=True)
