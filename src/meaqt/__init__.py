"""MEAQ-T modeling scaffolds.

This package provides starter modules for:
- high-entropy composition screening,
- moire thermoelectric response sweeps,
- pulse-driven magnetic switching,
- coating stack optimization.
"""

from .composition import screen_compositions
from .coating_optimizer import optimize_stacks
from .dft_adapters import parse_dft_report, parse_dft_text
from .moire_transport import scan_moire_response
from .plotting import (
    save_moire_heatmap,
    save_pareto_scatter,
    save_pulse_trajectory,
    save_switching_phase_diagram,
)
from .pulse_response import simulate_pulse_switching

__all__ = [
    "screen_compositions",
    "scan_moire_response",
    "simulate_pulse_switching",
    "optimize_stacks",
    "parse_dft_report",
    "parse_dft_text",
    "save_moire_heatmap",
    "save_pareto_scatter",
    "save_pulse_trajectory",
    "save_switching_phase_diagram",
]
