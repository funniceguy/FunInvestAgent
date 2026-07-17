import unittest

from evaluate_crypto_risk import evaluate_crypto_risk


class CryptoRiskEvaluatorTests(unittest.TestCase):
    def test_position_is_capped_by_stress_loss_budget(self) -> None:
        result = evaluate_crypto_risk(100_000, 2_000, 0.50, 0.50, 0.20, 0.30, 0.20, 0.15, 0.005)
        self.assertEqual(result.maximum_position, 4_000)
        self.assertEqual(result.stressed_loss, 2_000)
        self.assertEqual(result.decision, "risk_budget_eligible")

    def test_negative_expected_value_prefers_safe_asset(self) -> None:
        result = evaluate_crypto_risk(100_000, 2_000, 0.50, 0.30, 0.20, 0.50, 0.10, 0.20, 0.01)
        self.assertEqual(result.decision, "safe_asset_preferred")

    def test_probabilities_must_sum_to_one(self) -> None:
        with self.assertRaises(ValueError):
            evaluate_crypto_risk(100_000, 2_000, 0.50, 0.50, 0.20, 0.20, 0.20, 0.15, 0.005)


if __name__ == "__main__":
    unittest.main()

