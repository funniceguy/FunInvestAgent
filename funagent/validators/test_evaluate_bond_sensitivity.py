from __future__ import annotations

import unittest

from evaluate_bond_sensitivity import estimate_price_change


class BondSensitivityTests(unittest.TestCase):
    def test_duration_only_rate_increase(self) -> None:
        self.assertAlmostEqual(estimate_price_change(5.0, 100.0), -0.05)

    def test_convexity_adjusts_rate_increase(self) -> None:
        self.assertAlmostEqual(estimate_price_change(5.0, 100.0, 40.0), -0.048)

    def test_convexity_adjusts_rate_decrease(self) -> None:
        self.assertAlmostEqual(estimate_price_change(5.0, -100.0, 40.0), 0.052)

    def test_negative_duration_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            estimate_price_change(-1.0, 100.0)


if __name__ == "__main__":
    unittest.main()

