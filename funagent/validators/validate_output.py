from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_DIRS = [
    "funmemory",
    "funmemory/domains",
    "funmemory/rules",
    "funmemory/schemas",
    "funmemory/sources",
    "funagent",
    "funagent/agents",
    "funagent/rules",
    "funagent/skills",
    "funagent/skills/stocks",
    "funagent/workflows",
    "funoutput",
    "funoutput/templates",
    "funoutput/sessions",
    "funoutput/reports",
    "funoutput/reviews",
    "funoutput/exports",
    "funoutput/logs",
]

REQUIRED_TEMPLATES = [
    "funoutput/templates/session_summary.md",
    "funoutput/templates/weekly_market_report.md",
    "funoutput/templates/portfolio_review_report.md",
    "funoutput/templates/legal_risk_memo.md",
    "funoutput/templates/strategy_memo.md",
    "funoutput/templates/stock_strategy_report.md",
    "funoutput/templates/stock_strategy_review.md",
]

REQUIRED_STOCK_SKILLS = [
    "funagent/skills/stocks/stock_orchestrator.md",
    "funagent/skills/stocks/stock_intake_scope_skill.md",
    "funagent/skills/stocks/stock_data_collection_skill.md",
    "funagent/skills/stocks/stock_information_event_psychology_skill.md",
    "funagent/skills/stocks/stock_investor_psychology_skill.md",
    "funagent/skills/stocks/stock_market_regime_skill.md",
    "funagent/skills/stocks/stock_universe_screening_skill.md",
    "funagent/skills/stocks/stock_psychology_decision_gate_skill.md",
    "funagent/skills/stocks/stock_intraday_psychology_routine_skill.md",
    "funagent/skills/stocks/stock_leverage_product_risk_skill.md",
    "funagent/skills/stocks/stock_leverage_psychology_warfare_skill.md",
    "funagent/skills/stocks/stock_leverage_risk_gate_skill.md",
    "funagent/skills/stocks/stock_3x_leverage_tactical_skill.md",
    "funagent/skills/stocks/stock_leverage_verification_contract_skill.md",
    "funagent/skills/stocks/stock_short_term_tactical_skill.md",
    "funagent/skills/stocks/stock_value_investing_skill.md",
    "funagent/skills/stocks/stock_portfolio_construction_skill.md",
    "funagent/skills/stocks/stock_execution_risk_skill.md",
    "funagent/skills/stocks/stock_verification_contract_skill.md",
    "funagent/skills/stocks/stock_report_generation_skill.md",
    "funagent/skills/stocks/stock_performance_review_skill.md",
    "funagent/skills/stocks/stock_skill_composition_registry.yaml",
]

REQUIRED_STOCK_SUPPORT_FILES = [
    "funagent/workflows/stock_strategy_cycle.md",
    "funmemory/domains/stock_investor_psychology_playbook.md",
    "funmemory/domains/stock_leverage_3x_playbook.md",
    "funmemory/domains/stock_strategy_playbook.md",
    "funmemory/schemas/stock_leverage_risk_gate.schema.json",
    "funmemory/schemas/stock_psychology_gate.schema.json",
    "funmemory/schemas/stock_strategy_plan.schema.json",
    "funmemory/schemas/stock_strategy_review.schema.json",
    "funmemory/schemas/verification_scorecard.schema.json",
]

REQUIRED_STOCK_TEMPLATE_SECTIONS = [
    "## 투자자 심리 해석 게이트",
    "## 레버리지/3배 단타 게이트",
    "## Verify 평점 계약",
    "## 반복 검증 기록",
]

REQUIRED_TEMPLATE_SECTIONS = [
    "## 입력 데이터와 가정",
    "## 출처",
    "## 검증 체크리스트",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_DIRS:
        path = root / relative
        if not path.is_dir():
            errors.append(f"missing directory: {relative}")

    for relative in REQUIRED_TEMPLATES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing template: {relative}")
            continue

        content = read_text(path)
        for section in REQUIRED_TEMPLATE_SECTIONS:
            if section not in content:
                errors.append(f"missing section '{section}' in {relative}")
        if relative in {
            "funoutput/templates/stock_strategy_report.md",
            "funoutput/templates/stock_strategy_review.md",
        }:
            for section in REQUIRED_STOCK_TEMPLATE_SECTIONS:
                if section not in content:
                    errors.append(f"missing stock verification section '{section}' in {relative}")

    for relative in REQUIRED_STOCK_SKILLS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing stock skill: {relative}")

    for relative in REQUIRED_STOCK_SUPPORT_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing stock support file: {relative}")

    source_registry = root / "funmemory/sources/source_registry.yaml"
    if source_registry.is_file():
        content = read_text(source_registry)
        for token in ["last_verified:", "verification_policy:", "sources:"]:
            if token not in content:
                errors.append(f"missing token '{token}' in funmemory/sources/source_registry.yaml")
    else:
        errors.append("missing source registry: funmemory/sources/source_registry.yaml")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate FunInvestAgent structure and report templates.")
    parser.add_argument("--root", default=".", help="Project root directory.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = validate(root)

    if errors:
        print("FunInvestAgent validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FunInvestAgent validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
