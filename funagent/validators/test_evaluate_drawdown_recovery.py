from __future__ import annotations

import unittest

from evaluate_drawdown_recovery import (
    position_cap_percent,
    recovery_years,
    required_gain_percent,
)


class DrawdownRecoveryTests(unittest.TestCase):
    def test_required_gain_is_asymmetric(self) -> None:
        expected = {10.0: 11.111111, 20.0: 25.0, 30.0: 42.857143, 50.0: 100.0}
        for drawdown, gain in expected.items():
            self.assertAlmostEqual(required_gain_percent(drawdown), gain, places=6)

    def test_recovery_years_at_seven_percent(self) -> None:
        self.assertAlmostEqual(recovery_years(20.0, 7.0), 3.298079, places=6)

    def test_zero_drawdown_needs_no_recovery(self) -> None:
        self.assertEqual(required_gain_percent(0.0), 0.0)
        self.assertEqual(recovery_years(0.0, 7.0), 0.0)

    def test_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            required_gain_percent(100.0)
        with self.assertRaises(ValueError):
            recovery_years(20.0, 0.0)

    def test_position_size_uses_larger_stress_loss(self) -> None:
        self.assertAlmostEqual(position_cap_percent(0.5, 5.0, 10.0), 5.0)


if __name__ == "__main__":
    unittest.main()
