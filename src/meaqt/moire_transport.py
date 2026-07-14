from __future__ import annotations

import numpy as np
import pandas as pd

KB_EV = 8.617333262e-5  # eV/K


def moire_wavelength_nm(lattice_constant_nm: float, theta_deg: float) -> float:
    theta = np.deg2rad(max(theta_deg, 1e-6))
    return float(lattice_constant_nm / (2.0 * np.sin(theta / 2.0)))


def _fd_derivative(energy_ev: np.ndarray, mu_ev: float, temp_k: float) -> np.ndarray:
    kbt = KB_EV * temp_k
    x = (energy_ev - mu_ev) / max(kbt, 1e-12)
    expx = np.exp(np.clip(x, -100, 100))
    return expx / ((1.0 + expx) ** 2 * max(kbt, 1e-12))


def _transport_integrals(
    energy_ev: np.ndarray,
    dos: np.ndarray,
    velocity2: np.ndarray,
    tau_s: float,
    mu_ev: float,
    temp_k: float,
) -> tuple[float, float]:
    kernel = dos * velocity2 * tau_s
    minus_dfde = _fd_derivative(energy_ev, mu_ev, temp_k)
    de = energy_ev[1] - energy_ev[0]
    l0 = np.sum(kernel * minus_dfde) * de
    l1 = np.sum((energy_ev - mu_ev) * kernel * minus_dfde) * de
    return float(l0), float(l1)


def moire_band_dos(
    energy_ev: np.ndarray,
    theta_deg: float,
    displacement_vnm: float,
    filling: float,
) -> tuple[np.ndarray, np.ndarray]:
    # Toy miniband centers capturing theta/displacement/filling sensitivity.
    e0 = np.array([-0.045, -0.010, 0.015, 0.050], dtype=float)
    shift = 0.020 * (theta_deg - 1.5) + 0.030 * displacement_vnm + 0.010 * filling
    width = 0.004 + 0.003 * np.clip(theta_deg, 0.1, 4.0)
    centers = e0 + shift

    dos = np.zeros_like(energy_ev)
    for i, c in enumerate(centers):
        weight = 1.0 + 0.25 * np.cos(i + 3.0 * filling)
        dos += weight * np.exp(-0.5 * ((energy_ev - c) / width) ** 2)

    # Velocity suppression near flat-band conditions (small theta).
    v0 = 1.0
    flatness = np.clip((2.2 - theta_deg) / 2.0, 0.0, 1.0)
    velocity2 = (v0 * (1.0 - 0.6 * flatness)) ** 2 * np.ones_like(energy_ev)
    return dos, velocity2


def simulate_transport_point(
    theta_deg: float,
    displacement_vnm: float,
    filling: float,
    temp_k: float,
    mu_ev: float = 0.0,
    tau_s: float = 1e-13,
) -> dict[str, float]:
    energy_ev = np.linspace(-0.2, 0.2, 2400)
    dos, velocity2 = moire_band_dos(energy_ev, theta_deg, displacement_vnm, filling)
    l0, l1 = _transport_integrals(energy_ev, dos, velocity2, tau_s, mu_ev, temp_k)

    sigma_arb = max(l0, 1e-16)
    seebeck_uvk = -(l1 / (KB_EV * temp_k * sigma_arb + 1e-16)) * 86.17

    # Nernst proxy: Hall-angle-like factor times Seebeck slope w.r.t. displacement.
    hall_angle = 0.02 + 0.03 * np.tanh(0.4 - abs(filling))
    nernst_proxy = hall_angle * seebeck_uvk / max(temp_k, 1.0)

    return {
        "theta_deg": theta_deg,
        "displacement_vnm": displacement_vnm,
        "filling": filling,
        "temp_k": temp_k,
        "moire_lambda_nm": moire_wavelength_nm(0.33, theta_deg),
        "sigma_arb": sigma_arb,
        "seebeck_uV_per_K": float(seebeck_uvk),
        "power_factor_arb": float(sigma_arb * (seebeck_uvk**2)),
        "nernst_proxy": float(nernst_proxy),
    }


def scan_moire_response(
    theta_grid: np.ndarray,
    displacement_grid: np.ndarray,
    temp_grid: np.ndarray,
    filling: float,
) -> pd.DataFrame:
    rows = []
    for theta in theta_grid:
        for dfield in displacement_grid:
            for temp in temp_grid:
                rows.append(simulate_transport_point(theta, dfield, filling, temp))
    return pd.DataFrame(rows)
