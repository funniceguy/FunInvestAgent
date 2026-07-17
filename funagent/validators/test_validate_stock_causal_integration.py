from __future__ import annotations

import unittest
from pathlib import Path

from validate_stock_causal_integration import leverage_rebalance_delta, validate


class StockCausalIntegrationValidationTests(unittest.TestCase):
    def test_repository_has_complete_causal_integration(self) -> None:
        root = Path(__file__).resolve().parents[2]
        self.assertEqual([], validate(root))

    def test_two_sided_daily_reset_rebalance_direction(self) -> None:
        self.assertAlmostEqual(20.0, leverage_rebalance_delta(100.0, 2.0, 0.10))
        self.assertAlmostEqual(-20.0, leverage_rebalance_delta(100.0, 2.0, -0.10))
        self.assertAlmostEqual(60.0, leverage_rebalance_delta(100.0, -2.0, 0.10))
        self.assertAlmostEqual(-60.0, leverage_rebalance_delta(100.0, -2.0, -0.10))


if __name__ == "__main__":
    unittest.main()
