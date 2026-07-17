from __future__ import annotations

import argparse
import json


def calculate_financial_resilience(
    monthly_net_income: float,
    monthly_essential_spending: float,
    monthly_debt_service: float,
    liquid_assets: float,
    near_term_obligations: float,
    emergency_target_months: float,
    max_debt_service_ratio: float,
    income_shock_percent: float = 0.20,
) -> dict[str, float | bool | None]:
    values = [
        monthly_net_income,
        monthly_essential_spending,
        monthly_debt_service,
        liquid_assets,
        near_term_obligations,
        emergency_target_months,
        max_debt_service_ratio,
        income_shock_percent,
    ]
    if any(value < 0 for value in values) or monthly_essential_spending == 0:
        raise ValueError("inputs must be non-negative and essential spending must be positive")
    if max_debt_service_ratio > 1 or income_shock_percent > 1:
        raise ValueError("ratio inputs must not exceed 1")

    available_liquidity = max(0.0, liquid_assets - near_term_obligations)
    emergency_target = monthly_essential_spending * emergency_target_months
    emergency_months = available_liquidity / monthly_essential_spending
    emergency_shortfall = max(0.0, emergency_target - available_liquidity)
    debt_service_ratio = (
        monthly_debt_service / monthly_net_income if monthly_net_income > 0 else None
    )
    monthly_surplus = monthly_net_income - monthly_essential_spending - monthly_debt_service
    savings_rate = monthly_surplus / monthly_net_income if monthly_net_income > 0 else None
    investable_liquidity = max(0.0, available_liquidity - emergency_target)

    shocked_income = monthly_net_income * (1.0 - income_shock_percent)
    shocked_monthly_surplus = shocked_income - monthly_essential_spending - monthly_debt_service
    monthly_deficit = max(0.0, -shocked_monthly_surplus)
    deficit_runway_months = (
        available_liquidity / monthly_deficit if monthly_deficit > 0 else None
    )

    return {
        "available_liquidity": available_liquidity,
        "emergency_months": emergency_months,
        "emergency_shortfall": emergency_shortfall,
        "debt_service_ratio": debt_service_ratio,
        "monthly_surplus": monthly_surplus,
        "savings_rate": savings_rate,
        "investable_liquidity": investable_liquidity,
        "emergency_target_met": emergency_shortfall == 0,
        "debt_service_within_user_limit": (
            debt_service_ratio is not None and debt_service_ratio <= max_debt_service_ratio
        ),
        "shocked_monthly_surplus": shocked_monthly_surplus,
        "deficit_runway_months": deficit_runway_months,
        "forced_sale_risk": monthly_surplus < 0 or emergency_shortfall > 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate user-configured financial resilience metrics.")
    parser.add_argument("--monthly-net-income", type=float, required=True)
    parser.add_argument("--monthly-essential-spending", type=float, required=True)
    parser.add_argument("--monthly-debt-service", type=float, required=True)
    parser.add_argument("--liquid-assets", type=float, required=True)
    parser.add_argument("--near-term-obligations", type=float, required=True)
    parser.add_argument("--emergency-target-months", type=float, required=True)
    parser.add_argument("--max-debt-service-ratio", type=float, required=True)
    parser.add_argument("--income-shock-percent", type=float, default=0.20)
    args = parser.parse_args()

    result = calculate_financial_resilience(
        args.monthly_net_income,
        args.monthly_essential_spending,
        args.monthly_debt_service,
        args.liquid_assets,
        args.near_term_obligations,
        args.emergency_target_months,
        args.max_debt_service_ratio,
        args.income_shock_percent,
    )
    result["limitations"] = [
        "thresholds are user-configured, not universal financial advice",
        "insurance, taxes, irregular income, and legal obligations require separate evidence",
        "procedure metrics do not guarantee investment returns or financial outcomes",
    ]
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

