from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class CryptoRiskResult:
    maximum_position: float
    position_fraction_of_investable_assets: float
    stressed_loss: float
    net_expected_value_fraction: float
    decision: str


def evaluate_crypto_risk(
    investable_assets: float,
    crypto_loss_budget: float,
    stress_loss_fraction: float,
    probability_up: float,
    probability_flat: float,
    probability_down: float,
    upside_fraction: float,
    downside_fraction: float,
    round_trip_cost_fraction: float,
) -> CryptoRiskResult:
    values = [investable_assets, crypto_loss_budget, stress_loss_fraction, upside_fraction, downside_fraction, round_trip_cost_fraction]
    if any(value < 0 for value in values):
        raise ValueError("inputs must be non-negative")
    if investable_assets <= 0 or stress_loss_fraction <= 0 or stress_loss_fraction > 1:
        raise ValueError("investable_assets must be positive and stress_loss_fraction must be in (0, 1]")
    probability_sum = probability_up + probability_flat + probability_down
    if any(value < 0 or value > 1 for value in [probability_up, probability_flat, probability_down]):
        raise ValueError("probabilities must be in [0, 1]")
    if abs(probability_sum - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")

    maximum_position = min(investable_assets, crypto_loss_budget / stress_loss_fraction)
    stressed_loss = maximum_position * stress_loss_fraction
    net_ev = probability_up * upside_fraction - probability_down * downside_fraction - round_trip_cost_fraction

    if crypto_loss_budget <= 0:
        decision = "blocked"
    elif net_ev <= 0:
        decision = "safe_asset_preferred"
    else:
        decision = "risk_budget_eligible"

    return CryptoRiskResult(
        maximum_position=round(maximum_position, 2),
        position_fraction_of_investable_assets=round(maximum_position / investable_assets, 6),
        stressed_loss=round(stressed_loss, 2),
        net_expected_value_fraction=round(net_ev, 6),
        decision=decision,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Size a crypto position from a non-guaranteed stress loss budget.")
    parser.add_argument("--json", required=True, help="JSON object containing evaluator inputs")
    args = parser.parse_args()
    result = evaluate_crypto_risk(**json.loads(args.json))
    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

