from __future__ import annotations

import argparse
import json
from pathlib import Path


ASSEMBLIES_REQUIRING_CAUSAL_GATE = {
    "dual_track_stock_strategy",
    "short_term_only_strategy",
    "value_only_strategy",
    "long_term_total_return_income_strategy",
    "strategy_review_and_rebuild",
    "leveraged_3x_tactical_strategy",
}


def leverage_rebalance_delta(
    initial_nav: float, leverage: float, underlying_return: float
) -> float:
    """Return the simplified close rebalance exposure; positive is buy, negative is sell."""
    return leverage * initial_nav * underlying_return * (leverage - 1.0)


def _read(root: Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def _parse_assembly_sequences(registry_text: str) -> dict[str, set[str]]:
    sequences: dict[str, set[str]] = {}
    in_assemblies = False
    current: str | None = None

    for line in registry_text.splitlines():
        if line == "assemblies:":
            in_assemblies = True
            current = None
            continue
        if not in_assemblies:
            continue
        if line.startswith("  - id: "):
            current = line.split('"', 2)[1]
            sequences[current] = set()
            continue
        if current and line.startswith('      - "'):
            sequences[current].add(line.split('"', 2)[1])

    return sequences


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    required_files = [
        "funagent/skills/stocks/stock_market_integrity_causal_attribution_skill.md",
        "funmemory/schemas/stock_market_integrity_causal_attribution.schema.json",
        "funagent/skills/stocks/stock_orchestrator.md",
        "funagent/skills/stocks/stock_mechanical_flow_risk_gate_skill.md",
        "funagent/skills/stocks/stock_macro_causal_factor_matrix_skill.md",
        "funagent/skills/stocks/stock_verification_contract_skill.md",
        "funagent/skills/stocks/stock_skill_composition_registry.yaml",
        "funagent/workflows/stock_strategy_cycle.md",
        "funagent/rules/verification_score_contract.md",
        "funoutput/templates/stock_strategy_report.md",
        "funoutput/templates/stock_strategy_review.md",
        "funmemory/schemas/stock_strategy_plan.schema.json",
        "funmemory/schemas/stock_strategy_review.schema.json",
        "funmemory/schemas/verification_scorecard.schema.json",
    ]
    for relative in required_files:
        if not (root / relative).is_file():
            errors.append(f"missing required integration file: {relative}")

    if errors:
        return errors

    packet_schema_path = root / "funmemory/schemas/stock_market_integrity_causal_attribution.schema.json"
    plan_schema_path = root / "funmemory/schemas/stock_strategy_plan.schema.json"
    try:
        packet_schema = json.loads(packet_schema_path.read_text(encoding="utf-8"))
        plan_schema = json.loads(plan_schema_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON schema: {exc}"]

    packet_required = set(packet_schema.get("required", []))
    required_packet_fields = {
        "causal_layers",
        "institutional_flow_breakdown",
        "program_flow",
        "cross_market_counterfactuals",
        "leverage_mechanics",
        "manipulation_hypothesis",
        "money_flow_state",
        "strategy_constraints",
        "source_ids",
        "unknowns",
    }
    missing_packet_fields = required_packet_fields - packet_required
    if missing_packet_fields:
        errors.append(
            "causal attribution schema missing required fields: "
            + ", ".join(sorted(missing_packet_fields))
        )

    expected_rebalance = {
        (2.0, 0.10): 20.0,
        (2.0, -0.10): -20.0,
        (-2.0, 0.10): 60.0,
        (-2.0, -0.10): -60.0,
    }
    for (leverage, underlying_return), expected in expected_rebalance.items():
        actual = leverage_rebalance_delta(100.0, leverage, underlying_return)
        if abs(actual - expected) > 1e-9:
            errors.append(
                "two-sided leverage rebalance direction regression: "
                f"L={leverage}, r={underlying_return}, expected={expected}, actual={actual}"
            )

    scope_modes = (
        plan_schema.get("properties", {})
        .get("scope", {})
        .get("properties", {})
        .get("strategy_modes", {})
        .get("items", {})
        .get("enum", [])
    )
    if "market_integrity_causal_attribution" not in scope_modes:
        errors.append("stock strategy mode does not expose market_integrity_causal_attribution")
    plan_property = plan_schema.get("properties", {}).get("market_integrity_causal_attribution", {})
    if plan_property.get("$ref") != "stock_market_integrity_causal_attribution.schema.json":
        errors.append("stock strategy plan does not reference the causal attribution schema")
    if "market_integrity_causal_attribution" not in json.dumps(plan_schema.get("allOf", [])):
        errors.append("stock strategy plan does not conditionally require the causal packet")

    scorecard_schema = json.loads(
        (root / "funmemory/schemas/verification_scorecard.schema.json").read_text(encoding="utf-8")
    )
    category_names = (
        scorecard_schema.get("properties", {})
        .get("categories", {})
        .get("items", {})
        .get("properties", {})
        .get("name", {})
        .get("enum", [])
    )
    if "market_integrity_causal_attribution_suitability" not in category_names:
        errors.append("verification scorecard cannot store the causal attribution category")

    review_schema = json.loads(
        (root / "funmemory/schemas/stock_strategy_review.schema.json").read_text(encoding="utf-8")
    )
    if "market_integrity_causal_attribution_review" not in review_schema.get("properties", {}):
        errors.append("stock strategy review schema cannot store the causal attribution review")

    skill_text = _read(
        root, "funagent/skills/stocks/stock_market_integrity_causal_attribution_skill.md"
    )
    skill_markers = [
        "structural_vulnerability",
        "trigger",
        "amplifier",
        "consequence",
        "alternative_hypothesis",
        "L × V × r × (L - 1)",
        "confirmed_official",
        "public_flow_only",
        "unproven",
        "mixed_exit_rotation",
        "ADR/원주",
        "공식 조사 발표를 찾지 못한 것은 조작이 없다는 증명이 아니다",
    ]
    for marker in skill_markers:
        if marker not in skill_text:
            errors.append(f"causal attribution skill missing marker: {marker}")

    orchestrator_text = _read(root, "funagent/skills/stocks/stock_orchestrator.md")
    for marker in [
        "stock_market_integrity_causal_attribution_skill.md",
        "시장충격 인과·시장무결성 적합성",
        "구조적 취약성 -> 방아쇠 -> 증폭기 -> 결과",
        "mixed_exit_rotation",
        "causal_attribution_unresolved",
    ]:
        if marker not in orchestrator_text:
            errors.append(f"stock orchestrator missing causal marker: {marker}")

    mechanical_text = _read(root, "funagent/skills/stocks/stock_mechanical_flow_risk_gate_skill.md")
    for marker in [
        "L × V × r × (L-1)",
        "+2배",
        "-2배",
        "투신·사모",
        "설정·환매",
        "정확한 충격액",
    ]:
        if marker not in mechanical_text:
            errors.append(f"mechanical flow gate missing two-sided leverage marker: {marker}")

    registry_text = _read(root, "funagent/skills/stocks/stock_skill_composition_registry.yaml")
    if 'id: "stock_market_integrity_causal_attribution"' not in registry_text:
        errors.append("composition registry missing causal attribution subskill")
    sequences = _parse_assembly_sequences(registry_text)
    for assembly in sorted(ASSEMBLIES_REQUIRING_CAUSAL_GATE):
        if assembly not in sequences:
            errors.append(f"composition registry missing assembly: {assembly}")
        elif "stock_market_integrity_causal_attribution" not in sequences[assembly]:
            errors.append(f"assembly missing causal attribution gate: {assembly}")

    marker_map = {
        "funagent/workflows/stock_strategy_cycle.md": [
            "시장충격 인과·시장무결성",
            "정치·조작 증거등급",
        ],
        "funagent/rules/verification_score_contract.md": [
            "시장충격 인과·시장무결성 적합성",
            "| 96 |",
        ],
        "funagent/skills/stocks/stock_verification_contract_skill.md": [
            "### 시장충격 인과·시장무결성 적합성",
            "## 시장충격 인과·시장무결성 중대 차단 조건",
        ],
        "funoutput/templates/stock_strategy_report.md": [
            "## 시장충격 인과·시장무결성 게이트",
            "political",
        ],
        "funoutput/templates/stock_strategy_review.md": [
            "## 시장충격 인과·시장무결성 게이트",
            "과대·과소 귀속",
        ],
    }
    # The report template uses Korean labels, so accept the explicit evidence-grade marker
    # instead of requiring an English political field.
    marker_map["funoutput/templates/stock_strategy_report.md"][1] = "정치·시세조종 증거등급"
    for relative, markers in marker_map.items():
        content = _read(root, relative)
        for marker in markers:
            if marker not in content:
                errors.append(f"{relative} missing integration marker: {marker}")

    validator_text = _read(root, "funagent/validators/validate_output.py")
    for marker in [
        "stock_market_integrity_causal_attribution_skill.md",
        "stock_market_integrity_causal_attribution.schema.json",
        "## 시장충격 인과·시장무결성 게이트",
    ]:
        if marker not in validator_text:
            errors.append(f"validate_output.py missing causal integration requirement: {marker}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors = validate(root)
    if errors:
        print("Stock causal integration validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Stock causal integration validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
