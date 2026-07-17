from __future__ import annotations

import unittest

from evaluate_financial_resilience import calculate_financial_resilience


class FinancialResilienceTests(unittest.TestCase):
    def test_clear_liquidity_metrics(self) -> None:
        result = calculate_financial_resilience(5_000_000, 2_000_000, 500_000, 20_000_000, 2_000_000, 6, 0.30)
        self.assertAlmostEqual(result["available_liquidity"], 18_000_000)
        self.assertAlmostEqual(result["emergency_months"], 9.0)
        self.assertAlmostEqual(result["investable_liquidity"], 6_000_000)
        self.assertTrue(result["emergency_target_met"])

    def test_near_term_obligations_reduce_investable_cash(self) -> None:
        result = calculate_financial_resilience(4_000_000, 2_000_000, 500_000, 10_000_000, 4_000_000, 4, 0.30)
        self.assertAlmostEqual(result["available_liquidity"], 6_000_000)
        self.assertAlmostEqual(result["emergency_shortfall"], 2_000_000)
        self.assertEqual(result["investable_liquidity"], 0)

    def test_user_debt_limit_is_applied(self) -> None:
        result = calculate_financial_resilience(4_000_000, 2_000_000, 1_400_000, 20_000_000, 0, 6, 0.30)
        self.assertAlmostEqual(result["debt_service_ratio"], 0.35)
        self.assertFalse(result["debt_service_within_user_limit"])

    def test_income_shock_runway(self) -> None:
        result = calculate_financial_resilience(3_000_000, 2_000_000, 700_000, 6_000_000, 0, 0, 0.40, 0.30)
        self.assertAlmostEqual(result["shocked_monthly_surplus"], -600_000)
        self.assertAlmostEqual(result["deficit_runway_months"], 10.0)

    def test_invalid_ratio_rejected(self) -> None:
        with self.assertRaises(ValueError):
            calculate_financial_resilience(3_000_000, 2_000_000, 0, 1_000_000, 0, 3, 1.1)


if __name__ == "__main__":
    unittest.main()

