#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from meaqt.dft_adapters import parse_dft_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract DFT summary fields from output text")
    parser.add_argument("input", type=str, help="Path to VASP/QE output text")
    parser.add_argument("--code", type=str, default="auto", choices=["auto", "vasp", "qe"])
    parser.add_argument("--out", type=str, default="dft_summary.csv")
    args = parser.parse_args()

    path = Path(args.input)
    text = path.read_text(encoding="utf-8", errors="ignore")
    report = parse_dft_report(text, code=args.code)
    summary = report.summary

    df = pd.DataFrame(
        [
            {
                "source": str(path),
                "code": summary.code,
                "fermi_ev": summary.fermi_ev,
                "total_energy_ev": summary.total_energy_ev,
                "band_gap_ev": summary.band_gap_ev,
                "confidence": report.confidence,
                "missing_fields": ";".join(report.missing_fields),
                "notes": " | ".join(report.notes),
            }
        ]
    )
    df.to_csv(args.out, index=False)
    print(df.to_string(index=False))
    print(f"Saved summary to {args.out}")


if __name__ == "__main__":
    main()
