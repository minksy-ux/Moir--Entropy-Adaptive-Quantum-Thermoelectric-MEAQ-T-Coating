#!/usr/bin/env python3
from __future__ import annotations

import argparse

import pandas as pd

from meaqt.coating_optimizer import optimize_stacks


ID_COLS = ["protective", "interlayer", "moire", "substrate"]
METRIC_COLS = ["score", "heat_tol", "radiation_tol", "healing_rate", "thermal_kappa_wmk", "coupling"]


def _build_side_by_side(left: pd.DataFrame, right: pd.DataFrame, left_name: str, right_name: str) -> pd.DataFrame:
    left_keyed = left.copy()
    right_keyed = right.copy()
    left_keyed["stack_id"] = left_keyed[ID_COLS].astype(str).agg(" | ".join, axis=1)
    right_keyed["stack_id"] = right_keyed[ID_COLS].astype(str).agg(" | ".join, axis=1)

    left_view = left_keyed[["stack_id", *METRIC_COLS]].rename(
        columns={c: f"{left_name}_{c}" for c in METRIC_COLS}
    )
    right_view = right_keyed[["stack_id", *METRIC_COLS]].rename(
        columns={c: f"{right_name}_{c}" for c in METRIC_COLS}
    )

    merged = left_view.merge(right_view, on="stack_id", how="outer")
    merged[f"delta_{left_name}_minus_{right_name}_score"] = (
        merged[f"{left_name}_score"] - merged[f"{right_name}_score"]
    )
    return merged.sort_values(
        by=[f"{left_name}_score", f"{right_name}_score"],
        ascending=False,
        na_position="last",
    ).reset_index(drop=True)


def _stack_id_col(df: pd.DataFrame) -> pd.Series:
    return df[ID_COLS].astype(str).agg(" | ".join, axis=1)


def _by_rank_table(left: pd.DataFrame, right: pd.DataFrame, left_name: str, right_name: str) -> pd.DataFrame:
    l = left.copy().reset_index(drop=True)
    r = right.copy().reset_index(drop=True)
    rows = min(len(l), len(r))

    return pd.DataFrame(
        {
            "rank": range(1, rows + 1),
            f"{left_name}_stack": _stack_id_col(l.iloc[:rows]),
            f"{left_name}_score": l.iloc[:rows]["score"].to_numpy(),
            f"{right_name}_stack": _stack_id_col(r.iloc[:rows]),
            f"{right_name}_score": r.iloc[:rows]["score"].to_numpy(),
            f"delta_{left_name}_minus_{right_name}_score": l.iloc[:rows]["score"].to_numpy()
            - r.iloc[:rows]["score"].to_numpy(),
        }
    )


def _ranked_view(df: pd.DataFrame, preset_name: str) -> pd.DataFrame:
    out = df.copy()
    out.insert(0, "rank", range(1, len(out) + 1))
    out = out[["rank", *ID_COLS, *METRIC_COLS]]
    out.insert(0, "preset", preset_name)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare top coating candidates for two optimizer presets")
    parser.add_argument("--left", type=str, default="prototype_low_temp")
    parser.add_argument("--right", type=str, default="extreme_uht")
    parser.add_argument("--top-k", type=int, default=12)
    parser.add_argument(
        "--score-mode",
        type=str,
        default="raw",
        choices=["raw", "normalized"],
    )
    parser.add_argument("--min-heat-tol", type=float, default=None)
    parser.add_argument("--min-radiation-tol", type=float, default=None)
    parser.add_argument("--min-healing-rate", type=float, default=None)
    parser.add_argument("--max-thermal-kappa", type=float, default=None)
    parser.add_argument("--min-coupling", type=float, default=None)
    parser.add_argument("--out-side", type=str, default="coating_preset_side_by_side.csv")
    parser.add_argument("--out-by-rank", type=str, default="coating_preset_by_rank.csv")
    parser.add_argument("--out-ranked", type=str, default="coating_preset_ranked.csv")
    args = parser.parse_args()

    common_kwargs = {
        "top_k": args.top_k,
        "score_mode": args.score_mode,
        "min_heat_tol": args.min_heat_tol,
        "min_radiation_tol": args.min_radiation_tol,
        "min_healing_rate": args.min_healing_rate,
        "max_thermal_kappa_wmk": args.max_thermal_kappa,
        "min_coupling": args.min_coupling,
    }
    left = optimize_stacks(preset=args.left, **common_kwargs)
    right = optimize_stacks(preset=args.right, **common_kwargs)

    side = _build_side_by_side(left, right, args.left, args.right)
    by_rank = _by_rank_table(left, right, args.left, args.right)
    ranked = pd.concat([_ranked_view(left, args.left), _ranked_view(right, args.right)], ignore_index=True)

    side.to_csv(args.out_side, index=False)
    by_rank.to_csv(args.out_by_rank, index=False)
    ranked.to_csv(args.out_ranked, index=False)

    print(f"Top {args.top_k} for preset={args.left} (score_mode={args.score_mode})")
    print(left.to_string(index=False))
    print(f"\nTop {args.top_k} for preset={args.right} (score_mode={args.score_mode})")
    print(right.to_string(index=False))
    print(f"\nBy-rank side-by-side rows: {len(by_rank)}")
    print(by_rank.head(15).to_string(index=False))
    print(f"\nSide-by-side overlap rows: {len(side)}")
    print(side[["stack_id", f"{args.left}_score", f"{args.right}_score", f"delta_{args.left}_minus_{args.right}_score"]].head(15).to_string(index=False))
    print(f"\nSaved side-by-side table to {args.out_side}")
    print(f"Saved by-rank table to {args.out_by_rank}")
    print(f"Saved ranked table to {args.out_ranked}")


if __name__ == "__main__":
    main()