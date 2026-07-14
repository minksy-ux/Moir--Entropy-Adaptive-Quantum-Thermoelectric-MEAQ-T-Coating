#!/usr/bin/env python3
from __future__ import annotations

import argparse

from meaqt.composition import screen_compositions


def main() -> None:
    parser = argparse.ArgumentParser(description="Run high-entropy composition screening")
    parser.add_argument("--n-elements", type=int, default=5)
    parser.add_argument("--top-k", type=int, default=20)
    parser.add_argument("--out", type=str, default="composition_screen.csv")
    args = parser.parse_args()

    df = screen_compositions(n_elements=args.n_elements, top_k=args.top_k)
    print(df.head(10).to_string(index=False))
    df.to_csv(args.out, index=False)
    print(f"Saved {len(df)} rows to {args.out}")


if __name__ == "__main__":
    main()
