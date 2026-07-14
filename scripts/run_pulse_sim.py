#!/usr/bin/env python3
from __future__ import annotations

import argparse

import numpy as np

from meaqt.pulse_response import simulate_pulse_switching


def main() -> None:
    parser = argparse.ArgumentParser(description="Run pulse switching simulation")
    parser.add_argument("--amp", type=float, default=-1.2, help="Pulse IFE amplitude in Tesla")
    parser.add_argument("--duration", type=float, default=20.0, help="Simulation duration in ps")
    args = parser.parse_args()

    out = simulate_pulse_switching(duration_ps=args.duration, pulse_amp_t=args.amp)
    mz = out["m"][:, 2]
    switched = out["switched"]
    print(f"Switching detected: {switched}")
    print(f"mz initial={mz[0]:.4f}, mz final={mz[-1]:.4f}, mz mean last 100={np.mean(mz[-100:]):.4f}")


if __name__ == "__main__":
    main()
