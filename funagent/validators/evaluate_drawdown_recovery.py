from __future__ import annotations

import argparse
import json
import math


def required_gain_percent(drawdown_percent: float) -> float:
    if drawdown_percent < 0 or drawdown_percent >= 100:
        raise ValueError("drawdown must be at least 0% and less than 100%")
    drawdown = drawdown_percent / 100.0
    return (drawdown / (1.0 - drawdown)) * 100.0


def recovery_years(drawdown_percent: float, annual_return_percent: float) -> float:
    if annual_return_percent <= 0:
        raise ValueError("annual return must be greater than 0%")
    required_gain_percent(drawdown_percent)
    drawdown = drawdown_percent / 100.0
    annual_return = annual_return_percent / 100.0
    return math.log(1.0 / (1.0 - drawdown)) / math.log(1.0 + annual_return)


def position_cap_percent(
    risk_budget_percent: float,
    planned_stop_percent: float,
    stress_loss_percent: float,
) -> float:
    if risk_budget_percent <= 0:
        raise ValueError("risk budget must be greater than 0%")
    effective_loss = max(planned_stop_percent, stress_loss_percent)
    if effective_loss <= 0:
        raise ValueError("planned stop or stress loss must be greater than 0%")
    return (risk_budget_percent / effective_loss) * 100.0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculate the gain and smooth-return time required to recover from a drawdown."
    )
    parser.add_argument("--drawdown", type=float, required=True, help="Peak-to-trough loss in percent, entered as a positive number.")
    parser.add_argument("--annual-return", type=float, help="Illustrative annual return in percent.")
    parser.add_argument("--risk-budget-percent", type=float, help="Maximum portfolio loss allowed for the position.")
    parser.add_argument("--planned-stop-percent", type=float, help="Loss at the planned stop from entry.")
    parser.add_argument("--stress-loss-percent", type=float, help="Gap/slippage stress loss from entry.")
    args = parser.parse_args()

    sizing_values = [args.risk_budget_percent, args.planned_stop_percent, args.stress_loss_percent]
    if any(value is not None for value in sizing_values) and not all(
        value is not None for value in sizing_values
    ):
        parser.error(
            "--risk-budget-percent, --planned-stop-percent, and --stress-loss-percent must be supplied together"
        )

    result = {
        "drawdown_percent": round(args.drawdown, 6),
        "required_gain_percent": round(required_gain_percent(args.drawdown), 6),
        "recovery_years_at_smooth_return": None,
        "annual_return_assumption_percent": args.annual_return,
        "effective_position_loss_percent": None,
        "position_cap_percent": None,
        "policy_note": "Illustrative math only; market recovery speed and returns are not guaranteed.",
    }
    if args.annual_return is not None:
        result["recovery_years_at_smooth_return"] = round(
            recovery_years(args.drawdown, args.annual_return), 6
        )
    if all(value is not None for value in sizing_values):
        result["effective_position_loss_percent"] = round(
            max(args.planned_stop_percent, args.stress_loss_percent), 6
        )
        result["position_cap_percent"] = round(
            position_cap_percent(
                args.risk_budget_percent,
                args.planned_stop_percent,
                args.stress_loss_percent,
            ),
            6,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
