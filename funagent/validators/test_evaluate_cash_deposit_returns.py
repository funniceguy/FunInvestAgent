from __future__ import annotations

import unittest

from evaluate_cash_deposit_returns import (
    installment_savings_return,
    parking_blended_rate,
    term_deposit_return,
)


class CashDepositReturnTests(unittest.TestCase):
    def test_term_deposit_simple_interest(self) -> None:
        result = term_deposit_return(10_000_000, 0.04, 12)
        self.assertAlmostEqual(result["gross_interest"], 400_000)
        self.assertAlmostEqual(result["net_maturity_amount"], 10_400_000)
        self.assertAlmostEqual(result["annualized_money_weighted_return"], 0.04)

    def test_term_deposit_tax_is_applied_to_interest(self) -> None:
        result = term_deposit_return(10_000_000, 0.04, 12, 0.154)
        self.assertAlmostEqual(result["tax"], 61_600)
        self.assertAlmostEqual(result["net_interest"], 338_400)

    def test_installment_interest_uses_each_deposit_period(self) -> None:
        result = installment_savings_return(1_000_000, 0.06, 12)
        self.assertAlmostEqual(result["gross_interest"], 390_000)
        self.assertAlmostEqual(result["net_simple_return"], 0.0325)
        self.assertGreater(result["annualized_money_weighted_return"], 0.05)

    def test_parking_rate_is_blended_by_tier(self) -> None:
        result = parking_blended_rate(20_000_000, [(5_000_000, 0.05), (None, 0.02)])
        self.assertAlmostEqual(result["annual_interest"], 550_000)
        self.assertAlmostEqual(result["blended_annual_rate"], 0.0275)

    def test_parking_tiers_must_cover_balance(self) -> None:
        with self.assertRaises(ValueError):
            parking_blended_rate(20_000_000, [(5_000_000, 0.05)])


if __name__ == "__main__":
    unittest.main()

