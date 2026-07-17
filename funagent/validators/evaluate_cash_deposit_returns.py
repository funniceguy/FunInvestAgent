from __future__ import annotations

import argparse
import json
from collections.abc import Sequence


def _annualized_irr(cashflows: Sequence[float]) -> float:
    if not cashflows or not any(value < 0 for value in cashflows) or not any(
        value > 0 for value in cashflows
    ):
        raise ValueError("cashflows must include at least one outflow and one inflow")

    def npv(monthly_rate: float) -> float:
        return sum(value / ((1.0 + monthly_rate) ** month) for month, value in enumerate(cashflows))

    low, high = -0.9999, 1.0
    low_value, high_value = npv(low), npv(high)
    if low_value * high_value > 0:
        raise ValueError("cashflows do not produce an IRR in the supported range")

    for _ in range(200):
        mid = (low + high) / 2.0
        mid_value = npv(mid)
        if abs(mid_value) < 1e-12:
            low = high = mid
            break
        if low_value * mid_value <= 0:
            high = mid
            high_value = mid_value
        else:
            low = mid
            low_value = mid_value

    monthly_rate = (low + high) / 2.0
    return (1.0 + monthly_rate) ** 12 - 1.0


def term_deposit_return(
    principal: float,
    annual_rate: float,
    months: int,
    tax_rate: float = 0.0,
) -> dict[str, float]:
    if principal <= 0 or months <= 0:
        raise ValueError("principal and months must be positive")
    if annual_rate < 0 or not 0 <= tax_rate < 1:
        raise ValueError("invalid annual_rate or tax_rate")

    gross_interest = principal * annual_rate * months / 12.0
    tax = gross_interest * tax_rate
    net_interest = gross_interest - tax
    maturity = principal + net_interest
    annualized = (maturity / principal) ** (12.0 / months) - 1.0
    return {
        "total_contributions": principal,
        "gross_interest": gross_interest,
        "tax": tax,
        "net_interest": net_interest,
        "net_maturity_amount": maturity,
        "net_simple_return": net_interest / principal,
        "annualized_money_weighted_return": annualized,
    }


def installment_savings_return(
    monthly_contribution: float,
    annual_rate: float,
    months: int,
    tax_rate: float = 0.0,
) -> dict[str, float]:
    if monthly_contribution <= 0 or months <= 0:
        raise ValueError("monthly_contribution and months must be positive")
    if annual_rate < 0 or not 0 <= tax_rate < 1:
        raise ValueError("invalid annual_rate or tax_rate")

    total_contributions = monthly_contribution * months
    gross_interest = sum(
        monthly_contribution * annual_rate * remaining_months / 12.0
        for remaining_months in range(months, 0, -1)
    )
    tax = gross_interest * tax_rate
    net_interest = gross_interest - tax
    maturity = total_contributions + net_interest
    cashflows = [-monthly_contribution] * months + [maturity]
    annualized = _annualized_irr(cashflows)
    return {
        "total_contributions": total_contributions,
        "gross_interest": gross_interest,
        "tax": tax,
        "net_interest": net_interest,
        "net_maturity_amount": maturity,
        "net_simple_return": net_interest / total_contributions,
        "annualized_money_weighted_return": annualized,
    }


def parking_blended_rate(
    balance: float,
    tiers: Sequence[tuple[float | None, float]],
) -> dict[str, float]:
    if balance <= 0:
        raise ValueError("balance must be positive")
    remaining = balance
    annual_interest = 0.0
    for cap, rate in tiers:
        if rate < 0 or (cap is not None and cap <= 0):
            raise ValueError("invalid parking tier")
        amount = remaining if cap is None else min(remaining, cap)
        annual_interest += amount * rate
        remaining -= amount
        if remaining <= 0:
            break
    if remaining > 0:
        raise ValueError("parking tiers do not cover the full balance")
    return {
        "balance": balance,
        "annual_interest": annual_interest,
        "blended_annual_rate": annual_interest / balance,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize deposit and installment-savings returns.")
    parser.add_argument("--product", choices=["term", "installment"], required=True)
    parser.add_argument("--amount", type=float, required=True)
    parser.add_argument("--annual-rate", type=float, required=True)
    parser.add_argument("--months", type=int, required=True)
    parser.add_argument("--tax-rate", type=float, default=0.0)
    args = parser.parse_args()

    if args.product == "term":
        result = term_deposit_return(args.amount, args.annual_rate, args.months, args.tax_rate)
    else:
        result = installment_savings_return(args.amount, args.annual_rate, args.months, args.tax_rate)

    result["limitations"] = [
        "uses simple-interest timing unless the product terms specify otherwise",
        "does not infer bonus-rate eligibility, early-termination rates, or deposit protection",
        "tax treatment must be verified for the account and investor",
    ]
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

