#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from meaqt.plotting import save_switching_phase_diagram
from meaqt.pulse_response import simulate_pulse_switching


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate pulse switching phase diagram")
    parser.add_argument("--out-dir", type=str, default="figures")
    parser.add_argument("--amp-min", type=float, default=-1.8)
    parser.add_argument("--amp-max", type=float, default=-0.2)
    parser.add_argument("--amp-steps", type=int, default=17)
    parser.add_argument("--width-min", type=float, default=0.2)
    parser.add_argument("--width-max", type=float, default=2.0)
    parser.add_argument("--width-steps", type=int, default=19)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    amps = np.linspace(args.amp_min, args.amp_max, args.amp_steps)
    widths = np.linspace(args.width_min, args.width_max, args.width_steps)

    matrix = np.zeros((len(amps), len(widths)), dtype=float)
    rows = []
    for i, amp in enumerate(amps):
        for j, width in enumerate(widths):
            result = simulate_pulse_switching(pulse_amp_t=float(amp), pulse_width_ps=float(width))
            switched = 1.0 if bool(result["switched"]) else 0.0
            matrix[i, j] = switched
            rows.append(
                {
                    "pulse_amp_t": float(amp),
                    "pulse_width_ps": float(width),
                    "switched": switched,
                }
            )

    csv_path = out_dir / "pulse_phase_diagram.csv"
    png_path = out_dir / "pulse_phase_diagram.png"
    pd.DataFrame(rows).to_csv(csv_path, index=False)
    save_switching_phase_diagram(widths_ps=widths, amps_t=amps, switching_matrix=matrix, out_path=str(png_path))

    print(f"Saved phase data to {csv_path}")
    print(f"Saved phase figure to {png_path}")


if __name__ == "__main__":
    main()
