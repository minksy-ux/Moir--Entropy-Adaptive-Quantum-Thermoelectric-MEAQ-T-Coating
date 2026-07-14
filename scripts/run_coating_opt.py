#!/usr/bin/env python3
from __future__ import annotations

import argparse

from meaqt.coating_optimizer import WEIGHT_PRESETS, optimize_stacks, pareto_front


def main() -> None:
    parser = argparse.ArgumentParser(description="Run coating stack optimization")
    parser.add_argument("--top-k", type=int, default=12)
    parser.add_argument(
        "--preset",
        type=str,
        default="balanced",
        choices=sorted(WEIGHT_PRESETS.keys()),
        help="Objective weighting preset",
    )
    parser.add_argument(
        "--score-mode",
        type=str,
        default="raw",
        choices=["raw", "normalized"],
        help="Use raw composite score or min-max normalized objective score",
    )
    parser.add_argument("--min-heat-tol", type=float, default=None)
    parser.add_argument("--min-radiation-tol", type=float, default=None)
    parser.add_argument("--min-healing-rate", type=float, default=None)
    parser.add_argument("--max-thermal-kappa", type=float, default=None)
    parser.add_argument("--min-coupling", type=float, default=None)
    parser.add_argument("--out", type=str, default="coating_ranked.csv")
    parser.add_argument("--out-pareto", type=str, default="coating_pareto.csv")
    args = parser.parse_args()

    ranked = optimize_stacks(
        top_k=args.top_k,
        preset=args.preset,
        score_mode=args.score_mode,
        min_heat_tol=args.min_heat_tol,
        min_radiation_tol=args.min_radiation_tol,
        min_healing_rate=args.min_healing_rate,
        max_thermal_kappa_wmk=args.max_thermal_kappa,
        min_coupling=args.min_coupling,
    )
    print(ranked.to_string(index=False))
    ranked.to_csv(args.out, index=False)

    pf = pareto_front(
        ranked,
        maximize=["heat_tol", "radiation_tol", "healing_rate", "coupling"],
        minimize=["thermal_kappa_wmk"],
    )
    pf.to_csv(args.out_pareto, index=False)
    print(
        f"Saved preset={args.preset}, score_mode={args.score_mode}, ranked={len(ranked)} to {args.out}, "
        f"pareto={len(pf)} to {args.out_pareto}"
    )


if __name__ == "__main__":
    main()
