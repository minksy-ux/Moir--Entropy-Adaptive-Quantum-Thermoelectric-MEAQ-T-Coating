from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_moire_heatmap(
    df: pd.DataFrame,
    value_col: str,
    temp_k: float,
    out_path: str,
) -> None:
    cut = df[np.isclose(df["temp_k"], temp_k)].copy()
    if cut.empty:
        raise ValueError(f"No rows found for temp_k={temp_k}")

    pivot = cut.pivot_table(
        index="theta_deg",
        columns="displacement_vnm",
        values=value_col,
        aggfunc="mean",
    )
    x = pivot.columns.to_numpy(dtype=float)
    y = pivot.index.to_numpy(dtype=float)
    z = pivot.to_numpy(dtype=float)

    plt.figure(figsize=(8, 5))
    mesh = plt.pcolormesh(x, y, z, shading="auto", cmap="coolwarm")
    plt.colorbar(mesh, label=value_col)
    plt.xlabel("Displacement field (V/nm)")
    plt.ylabel("Twist angle (deg)")
    plt.title(f"{value_col} at T={temp_k:.1f} K")
    plt.tight_layout()
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=180)
    plt.close()


def save_pulse_trajectory(time_ps: np.ndarray, m: np.ndarray, out_path: str) -> None:
    plt.figure(figsize=(8, 4.5))
    plt.plot(time_ps, m[:, 0], label="mx", lw=1.4)
    plt.plot(time_ps, m[:, 1], label="my", lw=1.4)
    plt.plot(time_ps, m[:, 2], label="mz", lw=1.8)
    plt.xlabel("Time (ps)")
    plt.ylabel("Magnetization")
    plt.ylim(-1.05, 1.05)
    plt.title("Pulse-driven magnetization trajectory")
    plt.legend(frameon=False)
    plt.tight_layout()
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=180)
    plt.close()


def save_pareto_scatter(df: pd.DataFrame, out_path: str) -> None:
    plt.figure(figsize=(7.5, 5))
    sc = plt.scatter(
        df["thermal_kappa_wmk"],
        df["healing_rate"],
        c=df["score"],
        s=70,
        cmap="viridis",
        edgecolors="black",
        linewidths=0.4,
    )
    plt.colorbar(sc, label="Score")
    plt.xlabel("Thermal conductivity proxy (W/mK)")
    plt.ylabel("Healing rate")
    plt.title("Coating candidates: healing vs thermal conductivity")
    plt.tight_layout()
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=180)
    plt.close()


def save_switching_phase_diagram(
    widths_ps: np.ndarray,
    amps_t: np.ndarray,
    switching_matrix: np.ndarray,
    out_path: str,
) -> None:
    if switching_matrix.shape != (len(amps_t), len(widths_ps)):
        raise ValueError("switching_matrix must have shape (len(amps_t), len(widths_ps))")

    plt.figure(figsize=(8, 5))
    mesh = plt.pcolormesh(widths_ps, amps_t, switching_matrix, shading="auto", cmap="RdYlGn")
    cbar = plt.colorbar(mesh)
    cbar.set_label("Switching probability")
    plt.xlabel("Pulse width (ps)")
    plt.ylabel("Pulse amplitude (T)")
    plt.title("Pulse switching phase diagram")
    plt.tight_layout()
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=180)
    plt.close()
