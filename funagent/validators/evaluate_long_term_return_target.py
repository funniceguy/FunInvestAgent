from __future__ import annotations

import argparse
import json


def effective_annual_rate(monthly_rate_percent: float) -> float:
    monthly = monthly_rate_percent / 100.0
    if monthly <= -1.0:
        raise ValueError("monthly rate must be greater than -100%")
    return ((1.0 + monthly) ** 12 - 1.0) * 100.0


def planning_gate(annual_rate_percent: float, guaranteed: bool) -> str:
    if guaranteed:
        return "guarantee_blocked"
    if annual_rate_percent >= 100.0:
        return "target_blocked"
    if annual_rate_percent >= 30.0:
        return "speculative_only"
    if annual_rate_percent >= 15.0:
        return "stretch"
    return "modelable"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compound a monthly return target and apply the repository planning gate."
    )
    parser.add_argument("--monthly-rate", type=float, required=True, help="Monthly target in percent.")
    parser.add_argument("--guaranteed", action="store_true", help="Target is described as guaranteed/certain.")
    args = parser.parse_args()

    annual_rate = effective_annual_rate(args.monthly_rate)
    result = {
        "monthly_rate_percent": round(args.monthly_rate, 6),
        "effective_annual_rate_percent": round(annual_rate, 6),
        "one_year_growth_multiple": round(1.0 + annual_rate / 100.0, 6),
        "gate": planning_gate(annual_rate, args.guaranteed),
        "policy_note": "Planning gate only; not a market forecast or return guarantee.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
