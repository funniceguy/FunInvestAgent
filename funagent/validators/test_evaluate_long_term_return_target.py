from __future__ import annotations

import unittest

from evaluate_long_term_return_target import effective_annual_rate, planning_gate


class LongTermReturnTargetTests(unittest.TestCase):
    def test_monthly_ten_percent_is_blocked(self) -> None:
        annual = effective_annual_rate(10.0)
        self.assertAlmostEqual(annual, 213.8428376721, places=8)
        self.assertEqual(planning_gate(annual, guaranteed=False), "target_blocked")

    def test_guaranteed_language_always_blocks(self) -> None:
        annual = effective_annual_rate(1.0)
        self.assertEqual(planning_gate(annual, guaranteed=True), "guarantee_blocked")

    def test_planning_bands(self) -> None:
        self.assertEqual(planning_gate(effective_annual_rate(1.0), False), "modelable")
        self.assertEqual(planning_gate(effective_annual_rate(2.0), False), "stretch")
        self.assertEqual(planning_gate(effective_annual_rate(3.0), False), "speculative_only")

    def test_invalid_negative_one_hundred_percent(self) -> None:
        with self.assertRaises(ValueError):
            effective_annual_rate(-100.0)


if __name__ == "__main__":
    unittest.main()
