from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def _norm(vec: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(vec)
    if n < 1e-12:
        return np.array([0.0, 0.0, 1.0])
    return vec / n


def gaussian_pulse(t: float, t0: float, width: float, amp: float) -> float:
    return float(amp * np.exp(-0.5 * ((t - t0) / max(width, 1e-12)) ** 2))


def _llg_rhs(
    t: float,
    m: np.ndarray,
    gamma: float,
    alpha: float,
    h_bias: np.ndarray,
    anisotropy_t: float,
    pulse_t0: float,
    pulse_w: float,
    pulse_amp: float,
) -> np.ndarray:
    m_vec = _norm(m)
    # Effective field includes bias, anisotropy, and pulse-induced IFE term.
    h_aniso = anisotropy_t * np.array([0.0, 0.0, m_vec[2]])
    h_ife = np.array([0.0, 0.0, gaussian_pulse(t, pulse_t0, pulse_w, pulse_amp)])
    h_eff = h_bias + h_aniso + h_ife

    mxh = np.cross(m_vec, h_eff)
    mxmxh = np.cross(m_vec, mxh)
    dm = -gamma * mxh - alpha * gamma * mxmxh
    return dm


def simulate_pulse_switching(
    duration_ps: float = 20.0,
    n_steps: int = 1500,
    alpha: float = 0.05,
    gamma: float = 176.0,
    anisotropy_t: float = 0.18,
    h_bias_t: tuple[float, float, float] = (0.0, 0.0, 0.02),
    pulse_center_ps: float = 4.0,
    pulse_width_ps: float = 0.8,
    pulse_amp_t: float = -1.2,
) -> dict[str, np.ndarray | bool]:
    t_eval = np.linspace(0.0, duration_ps, n_steps)
    m0 = np.array([0.03, 0.0, 0.999])

    sol = solve_ivp(
        fun=lambda t, m: _llg_rhs(
            t,
            m,
            gamma=gamma,
            alpha=alpha,
            h_bias=np.array(h_bias_t),
            anisotropy_t=anisotropy_t,
            pulse_t0=pulse_center_ps,
            pulse_w=pulse_width_ps,
            pulse_amp=pulse_amp_t,
        ),
        t_span=(0.0, duration_ps),
        y0=m0,
        t_eval=t_eval,
        rtol=1e-6,
        atol=1e-8,
    )

    m = sol.y.T
    m = np.array([_norm(v) for v in m])
    switched = bool(np.mean(m[-100:, 2]) < 0.0)
    return {"time_ps": sol.t, "m": m, "switched": switched}


def topological_charge_from_texture(m: np.ndarray, dx: float = 1.0, dy: float = 1.0) -> float:
    """Estimate topological charge for a 2D texture m[ny, nx, 3]."""
    if m.ndim != 3 or m.shape[-1] != 3:
        raise ValueError("Expected shape [ny, nx, 3]")
    ny, nx, _ = m.shape
    if ny < 3 or nx < 3:
        raise ValueError("Texture must be at least 3x3")

    dmx = (m[:, 2:, :] - m[:, :-2, :]) / (2.0 * dx)
    dmy = (m[2:, :, :] - m[:-2, :, :]) / (2.0 * dy)
    mc = m[1:-1, 1:-1, :]
    dmx_c = dmx[1:-1, :, :]
    dmy_c = dmy[:, 1:-1, :]
    integrand = np.einsum("...i,...i->...", mc, np.cross(dmx_c, dmy_c))
    return float(np.sum(integrand) * dx * dy / (4.0 * np.pi))
