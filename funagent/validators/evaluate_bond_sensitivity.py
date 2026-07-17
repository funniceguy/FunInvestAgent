from __future__ import annotations

import argparse
import json


def estimate_price_change(
    modified_duration: float,
    yield_shock_bp: float,
    convexity: float = 0.0,
) -> float:
    if modified_duration < 0:
        raise ValueError("modified_duration must be non-negative")
    shock = yield_shock_bp / 10_000.0
    return -modified_duration * shock + 0.5 * convexity * shock * shock


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Approximate a bond price change from duration and convexity."
    )
    parser.add_argument("--duration", type=float, required=True)
    parser.add_argument("--shock-bp", type=float, required=True)
    parser.add_argument("--convexity", type=float, default=0.0)
    args = parser.parse_args()

    change = estimate_price_change(args.duration, args.shock_bp, args.convexity)
    print(
        json.dumps(
            {
                "modified_duration": args.duration,
                "yield_shock_bp": args.shock_bp,
                "convexity": args.convexity,
                "estimated_price_change_decimal": round(change, 8),
                "estimated_price_change_pct": round(change * 100, 4),
                "limitations": [
                    "parallel-yield-shift approximation",
                    "does not include credit-spread, call, liquidity, tax, or FX effects",
                ],
            },
            ensure_ascii=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

