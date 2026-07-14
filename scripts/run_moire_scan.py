#!/usr/bin/env python3
from __future__ import annotations

import argparse

import numpy as np

from meaqt.moire_transport import scan_moire_response


def main() -> None:
    parser = argparse.ArgumentParser(description="Run moire transport scan")
    parser.add_argument("--filling", type=float, default=0.0)
    parser.add_argument("--out", type=str, default="moire_scan.csv")
    args = parser.parse_args()

    theta = np.linspace(0.4, 3.0, 9)
    displacement = np.linspace(-0.5, 0.5, 7)
    temp = np.array([10.0, 25.0, 50.0, 100.0])

    df = scan_moire_response(theta, displacement, temp, filling=args.filling)
    print(df.sort_values("power_factor_arb", ascending=False).head(10).to_string(index=False))
    df.to_csv(args.out, index=False)
    print(f"Saved {len(df)} rows to {args.out}")


if __name__ == "__main__":
    main()
