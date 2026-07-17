from __future__ import annotations

import argparse
import json
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
    "funagent/skills/bonds",
    "funagent/skills/cash",
    "funagent/skills/crypto",
    "funagent/skills/financial",
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
    "funoutput/templates/bond_strategy_report.md",
    "funoutput/templates/cash_deposit_comparison_report.md",
    "funoutput/templates/financial_strategy_report.md",
    "funoutput/templates/crypto_strategy_report.md",
]

REQUIRED_FINANCIAL_SKILLS = [
    "funagent/skills/financial_strategy_orchestrator.md",
    "funagent/skills/financial/financial_health_liquidity_gate_skill.md",
    "funagent/skills/financial/financial_cross_asset_evidence_synthesis_skill.md",
    "funagent/skills/financial/financial_goal_bucket_design_skill.md",
    "funagent/skills/financial/financial_portfolio_scenario_stress_skill.md",
    "funagent/skills/financial/financial_strategy_learning_loop_skill.md",
    "funagent/skills/financial/financial_strategy_verification_contract_skill.md",
    "funagent/skills/financial/financial_skill_composition_registry.yaml",
]

REQUIRED_FINANCIAL_SUPPORT_FILES = [
    "funagent/workflows/financial_strategy_cycle.md",
    "funmemory/domains/financial_strategy_playbook.md",
    "funmemory/schemas/financial_health_gate.schema.json",
    "funmemory/schemas/financial_strategy_plan.schema.json",
    "funmemory/schemas/financial_verification_scorecard.schema.json",
    "funagent/validators/evaluate_financial_resilience.py",
    "funagent/validators/test_evaluate_financial_resilience.py",
]

REQUIRED_FINANCIAL_TEMPLATE_SECTIONS = [
    "## 재무 체력·유동성 게이트",
    "## 교차자산 근거 카드",
    "## 하위 오케스트레이터 판정",
    "## 목표 버킷",
    "## 통합 자산배분",
    "## 미래 시나리오·복합 스트레스",
    "## 운영 전략",
    "## 전략 학습 루프",
    "## 통합 재무 Verify 평점 계약",
    "## 반복 검증 기록",
]

REQUIRED_CASH_SKILLS = [
    "funagent/skills/cash/cash_deposit_orchestrator.md",
    "funagent/skills/cash/cash_deposit_source_search_skill.md",
    "funagent/skills/cash/cash_deposit_product_normalization_skill.md",
    "funagent/skills/cash/cash_deposit_bond_substitution_gate_skill.md",
    "funagent/skills/cash/cash_deposit_verification_contract_skill.md",
    "funagent/skills/cash/cash_deposit_skill_composition_registry.yaml",
]

REQUIRED_CASH_SUPPORT_FILES = [
    "funmemory/domains/cash_deposit_bond_substitution_playbook.md",
    "funmemory/schemas/cash_deposit_product.schema.json",
    "funmemory/schemas/cash_deposit_bond_comparison.schema.json",
    "funmemory/schemas/cash_deposit_verification_scorecard.schema.json",
    "funagent/validators/evaluate_cash_deposit_returns.py",
    "funagent/validators/test_evaluate_cash_deposit_returns.py",
]

REQUIRED_CASH_TEMPLATE_SECTIONS = [
    "## 공식 정보 검색 커버리지",
    "## 상품 식별·보호 한도",
    "## 실제 세후수익 정규화",
    "## 현금 필요일·유동성 스트레스",
    "## 동일 만기 채권 비교",
    "## 단기·장기 비교 게이트",
    "## 포트폴리오 적용",
    "## 현금성·예적금 Verify 평점 계약",
    "## 반복 검증 기록",
]

REQUIRED_BOND_SKILLS = [
    "funagent/skills/bonds/bond_orchestrator.md",
    "funagent/skills/bonds/bond_intake_scope_skill.md",
    "funagent/skills/bonds/bond_source_search_skill.md",
    "funagent/skills/bonds/bond_evidence_extraction_skill.md",
    "funagent/skills/bonds/bond_market_regime_curve_skill.md",
    "funagent/skills/bonds/bond_security_fund_analysis_skill.md",
    "funagent/skills/bonds/bond_credit_liquidity_risk_gate_skill.md",
    "funagent/skills/bonds/bond_ladder_liability_matching_skill.md",
    "funagent/skills/bonds/bond_portfolio_integration_skill.md",
    "funagent/skills/bonds/bond_verification_contract_skill.md",
    "funagent/skills/bonds/bond_skill_composition_registry.yaml",
]

REQUIRED_BOND_SUPPORT_FILES = [
    "funagent/skills/financial_strategy_orchestrator.md",
    "funagent/workflows/bond_strategy_cycle.md",
    "funmemory/domains/bond_strategy_playbook.md",
    "funmemory/schemas/bond_evidence_card.schema.json",
    "funmemory/schemas/bond_strategy_plan.schema.json",
    "funmemory/schemas/bond_risk_gate.schema.json",
    "funmemory/schemas/bond_verification_scorecard.schema.json",
    "funagent/validators/evaluate_bond_sensitivity.py",
    "funagent/validators/test_evaluate_bond_sensitivity.py",
]

REQUIRED_BOND_TEMPLATE_SECTIONS = [
    "## 현금성·예적금 대체재 비교",
    "## 공식 정보 검색 커버리지",
    "## 채권 근거 카드",
    "## 금리 국면·수익률곡선",
    "## 개별채권·ETF 구조 분석",
    "## 신용·유동성 위험 게이트",
    "## 만기 사다리·현금흐름 매칭",
    "## 주식·채권 장기 포트폴리오",
    "## 복합 스트레스",
    "## 채권 Verify 평점 계약",
    "## 반복 검증 기록",
]

REQUIRED_CRYPTO_SKILLS = [
    "funagent/skills/crypto/crypto_orchestrator.md",
    "funagent/skills/crypto/crypto_intake_capital_survival_gate_skill.md",
    "funagent/skills/crypto/crypto_source_search_evidence_skill.md",
    "funagent/skills/crypto/crypto_market_regime_flow_skill.md",
    "funagent/skills/crypto/crypto_asset_protocol_due_diligence_skill.md",
    "funagent/skills/crypto/crypto_custody_counterparty_stablecoin_gate_skill.md",
    "funagent/skills/crypto/crypto_yield_staking_defi_gate_skill.md",
    "funagent/skills/crypto/crypto_portfolio_execution_skill.md",
    "funagent/skills/crypto/crypto_forecast_learning_loop_skill.md",
    "funagent/skills/crypto/crypto_verification_contract_skill.md",
    "funagent/skills/crypto/crypto_skill_composition_registry.yaml",
]

REQUIRED_CRYPTO_SUPPORT_FILES = [
    "funagent/workflows/crypto_strategy_cycle.md",
    "funmemory/domains/crypto_strategy_playbook.md",
    "funmemory/schemas/crypto_evidence_card.schema.json",
    "funmemory/schemas/crypto_risk_gate.schema.json",
    "funmemory/schemas/crypto_prediction_ledger.schema.json",
    "funmemory/schemas/crypto_strategy_plan.schema.json",
    "funmemory/schemas/crypto_verification_scorecard.schema.json",
    "funagent/validators/evaluate_crypto_risk.py",
    "funagent/validators/test_evaluate_crypto_risk.py",
    "funoutput/logs/crypto_prediction_ledger.jsonl",
]

REQUIRED_CRYPTO_TEMPLATE_SECTIONS = [
    "## 자본 생존 게이트",
    "## 공식 정보 검색 커버리지",
    "## 코인 근거 카드",
    "## 시장 국면·현물/파생 수급",
    "## 자산·프로토콜 실사",
    "## 보관·거래상대방·스테이블코인 게이트",
    "## 스테이킹·렌딩·DeFi 수익 게이트",
    "## 포트폴리오·적립·실행",
    "## 보수·기본·강세 시나리오",
    "## 예측·전략 학습 루프",
    "## 코인 Verify 평점 계약",
    "## 반복 검증 기록",
]

REQUIRED_STOCK_SKILLS = [
    "funagent/skills/stocks/stock_orchestrator.md",
    "funagent/skills/stocks/stock_intake_scope_skill.md",
    "funagent/skills/stocks/stock_capital_preservation_recovery_gate_skill.md",
    "funagent/skills/stocks/stock_data_collection_skill.md",
    "funagent/skills/stocks/stock_cross_market_outcome_audit_skill.md",
    "funagent/skills/stocks/stock_forecast_learning_loop_skill.md",
    "funagent/skills/stocks/stock_forecast_failure_postmortem_skill.md",
    "funagent/skills/stocks/stock_forward_source_search_skill.md",
    "funagent/skills/stocks/stock_forward_evidence_extraction_skill.md",
    "funagent/skills/stocks/stock_forward_outlook_synthesis_skill.md",
    "funagent/skills/stocks/stock_predictive_calibration_skill.md",
    "funagent/skills/stocks/stock_mechanical_flow_risk_gate_skill.md",
    "funagent/skills/stocks/stock_supply_overhang_order_flow_skill.md",
    "funagent/skills/stocks/stock_macro_causal_factor_matrix_skill.md",
    "funagent/skills/stocks/stock_market_integrity_causal_attribution_skill.md",
    "funagent/skills/stocks/stock_information_event_psychology_skill.md",
    "funagent/skills/stocks/stock_investor_psychology_skill.md",
    "funagent/skills/stocks/stock_market_regime_skill.md",
    "funagent/skills/stocks/stock_momentum_rotation_cycle_classifier_skill.md",
    "funagent/skills/stocks/stock_universe_screening_skill.md",
    "funagent/skills/stocks/stock_quality_value_screening_skill.md",
    "funagent/skills/stocks/stock_long_term_return_target_gate_skill.md",
    "funagent/skills/stocks/stock_long_term_valuation_durability_skill.md",
    "funagent/skills/stocks/stock_covered_call_income_gate_skill.md",
    "funagent/skills/stocks/stock_long_term_portfolio_strategy_skill.md",
    "funagent/skills/stocks/stock_long_term_verification_contract_skill.md",
    "funagent/skills/stocks/stock_psychology_decision_gate_skill.md",
    "funagent/skills/stocks/stock_aggressive_short_term_probability_skill.md",
    "funagent/skills/stocks/stock_us_intraday_order_timing_skill.md",
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
    "funmemory/domains/stock_market_microstructure_playbook.md",
    "funmemory/domains/stock_long_term_total_return_playbook.md",
    "funmemory/domains/stock_capital_preservation_recovery_playbook.md",
    "funmemory/schemas/stock_leverage_risk_gate.schema.json",
    "funmemory/schemas/stock_psychology_gate.schema.json",
    "funmemory/schemas/stock_strategy_plan.schema.json",
    "funmemory/schemas/stock_market_integrity_causal_attribution.schema.json",
    "funmemory/schemas/stock_strategy_review.schema.json",
    "funmemory/schemas/stock_prediction_ledger.schema.json",
    "funmemory/schemas/stock_cross_market_outcome_audit.schema.json",
    "funmemory/schemas/stock_supply_overhang_order_flow.schema.json",
    "funmemory/schemas/stock_momentum_rotation_cycle.schema.json",
    "funmemory/schemas/stock_long_term_return_target_gate.schema.json",
    "funmemory/schemas/stock_long_term_valuation_durability.schema.json",
    "funmemory/schemas/stock_covered_call_income_gate.schema.json",
    "funmemory/schemas/stock_long_term_portfolio_strategy.schema.json",
    "funmemory/schemas/stock_long_term_verification_scorecard.schema.json",
    "funmemory/schemas/stock_capital_preservation_recovery_gate.schema.json",
    "funmemory/schemas/verification_scorecard.schema.json",
    "funagent/validators/audit_stock_strategy_history.py",
    "funagent/validators/evaluate_long_term_return_target.py",
    "funagent/validators/test_evaluate_long_term_return_target.py",
    "funagent/validators/evaluate_drawdown_recovery.py",
    "funagent/validators/test_evaluate_drawdown_recovery.py",
    "funagent/validators/validate_stock_causal_integration.py",
    "funagent/validators/test_validate_stock_causal_integration.py",
    "funoutput/logs/stock_prediction_ledger.jsonl",
]

REQUIRED_STOCK_TEMPLATE_SECTIONS = [
    "## 국내·미국 전수 성과 감사",
    "## 자본보전·손실회복 우선 게이트",
    "## 금주 예측 복기·평점 보정 루프",
    "## 전망 실패 사후분석",
    "## 차주/미래 전망 근거 검색·발췌·분석",
    "## 예측 보정·적중 추적",
    "## 기계적 수급·프로그램 매도 게이트",
    "## 시장충격 인과·시장무결성 게이트",
    "잠재 매수·매도 물량·오버행",
    "급등주·순환주 사이클 분류",
    "## 거시 원인 민감도 매트릭스",
    "## 투자자 심리 해석 게이트",
    "## 공격적 단기 매매 확률 게이트",
    "## 레버리지/3배 단타 게이트",
    "## 장기 목표수익률 현실성 게이트",
    "## 장기 밸류에이션·기업 내구성",
    "## 배당·분배·커버드콜 품질 게이트",
    "## 장기 총수익·인컴 포트폴리오",
    "## 장기투자 Verify 평점 계약",
    "## 채권 분석·통합 포트폴리오",
    "## 현금성·예적금·채권 대체재",
    "## Verify 평점 계약",
    "## 반복 검증 기록",
]

REQUIRED_TEMPLATE_SECTIONS = [
    "## 입력 데이터와 가정",
    "## 출처",
    "## 검증 체크리스트",
]

REQUIRED_COMPOSITION_SKILLS = [
    "stock_cross_market_outcome_audit",
    "stock_capital_preservation_recovery_gate",
    "stock_supply_overhang_order_flow",
    "stock_momentum_rotation_cycle_classifier",
]

REQUIRED_LONG_TERM_COMPOSITION_SKILLS = [
    "stock_long_term_return_target_gate",
    "stock_long_term_valuation_durability",
    "stock_covered_call_income_gate",
    "stock_long_term_portfolio_strategy",
    "stock_long_term_verification_contract",
]

REQUIRED_SOURCE_IDS = [
    "nasdaq_open_close_cross_noii",
    "nyse_auction_imbalances",
    "sec_market_activity_metrics",
    "finra_short_interest",
    "sec_form_13f_faq",
    "sec_form_4",
    "sec_order_execution",
    "sec_layering_spoofing",
    "krx_program_trading",
    "krx_volatility_interruption",
    "sec_investor_compound_interest",
    "oic_covered_call_strategy",
    "cboe_index_income_buywrite",
    "sec_fund_return_of_capital_report",
    "sec_investor_etf_nav_spread",
    "sec_investor_fund_fees_2025",
    "krx_covered_call_listing_2026_example",
    "globalx_qyld_official_product",
    "sec_stop_order_execution_risk",
    "sec_investor_guaranteed_return_red_flags",
    "finra_bond_duration",
    "finra_bond_yield_return",
    "finra_bond_liquidity",
    "finra_fixed_income_data",
    "investor_gov_bond_funds",
    "us_treasury_daily_rates",
    "treasurydirect_marketable_securities",
    "treasurydirect_floating_rate_notes",
    "federal_reserve_monetary_policy",
    "korea_treasury_bond_market",
    "fsc_deposit_protection_2025_qa",
    "kdic_protected_institutions_products",
    "fss_financial_products_at_a_glance",
    "kfb_consumer_portal_deposit_rates",
    "bok_financial_institution_rates_snapshot",
    "sec_investor_asset_allocation",
    "cfpb_emergency_fund_guide",
    "cfpb_financial_wellbeing_framework",
    "sec_crypto_etp_risk",
    "cftc_virtual_currency_risk",
    "finra_crypto_asset_risks",
    "sec_crypto_interest_accounts",
    "ethereum_staking_risks",
    "fsc_virtual_asset_user_protection",
    "cftc_bitcoin_cot",
    "upbit_websocket_market_data",
]

REQUIRED_SCORE_CATEGORIES = [
    "cross_market_outcome_audit_suitability",
    "capital_preservation_recovery_suitability",
    "mechanical_flow_risk_suitability",
    "supply_overhang_order_flow_suitability",
    "momentum_rotation_cycle_suitability",
    "long_term_return_target_feasibility",
    "long_term_valuation_durability_suitability",
    "covered_call_income_quality_suitability",
    "long_term_portfolio_stress_suitability",
    "bond_source_structure_suitability",
    "bond_credit_liquidity_suitability",
    "bond_cashflow_portfolio_suitability",
    "deposit_protection_product_accuracy",
    "cash_deposit_bond_substitution_suitability",
    "financial_health_liquidity_suitability",
    "financial_goal_bucket_suitability",
    "cross_asset_evidence_suitability",
    "financial_scenario_stress_suitability",
    "financial_learning_reviewability",
    "crypto_capital_survival_suitability",
    "crypto_market_protocol_suitability",
    "crypto_custody_stablecoin_suitability",
    "crypto_yield_defi_suitability",
    "crypto_execution_learning_suitability",
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
        if relative == "funoutput/templates/bond_strategy_report.md":
            for section in REQUIRED_BOND_TEMPLATE_SECTIONS:
                if section not in content:
                    errors.append(f"missing bond verification section '{section}' in {relative}")
        if relative == "funoutput/templates/cash_deposit_comparison_report.md":
            for section in REQUIRED_CASH_TEMPLATE_SECTIONS:
                if section not in content:
                    errors.append(f"missing cash/deposit verification section '{section}' in {relative}")
        if relative == "funoutput/templates/financial_strategy_report.md":
            for section in REQUIRED_FINANCIAL_TEMPLATE_SECTIONS:
                if section not in content:
                    errors.append(f"missing financial verification section '{section}' in {relative}")
        if relative == "funoutput/templates/crypto_strategy_report.md":
            for section in REQUIRED_CRYPTO_TEMPLATE_SECTIONS:
                if section not in content:
                    errors.append(f"missing crypto verification section '{section}' in {relative}")

    for relative in REQUIRED_STOCK_SKILLS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing stock skill: {relative}")

    for relative in REQUIRED_STOCK_SUPPORT_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing stock support file: {relative}")

    for relative in REQUIRED_BOND_SKILLS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing bond skill: {relative}")

    for relative in REQUIRED_BOND_SUPPORT_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing bond support file: {relative}")

    for relative in REQUIRED_CASH_SKILLS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing cash/deposit skill: {relative}")

    for relative in REQUIRED_CASH_SUPPORT_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing cash/deposit support file: {relative}")

    for relative in REQUIRED_FINANCIAL_SKILLS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing financial skill: {relative}")

    for relative in REQUIRED_FINANCIAL_SUPPORT_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing financial support file: {relative}")

    for relative in REQUIRED_CRYPTO_SKILLS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing crypto skill: {relative}")

    for relative in REQUIRED_CRYPTO_SUPPORT_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing crypto support file: {relative}")

    schema_dir = root / "funmemory/schemas"
    if schema_dir.is_dir():
        for path in schema_dir.glob("*.schema.json"):
            try:
                json.loads(read_text(path))
            except json.JSONDecodeError as exc:
                errors.append(f"invalid JSON schema {path.relative_to(root)}: {exc}")

    composition_registry = root / "funagent/skills/stocks/stock_skill_composition_registry.yaml"
    if composition_registry.is_file():
        content = read_text(composition_registry)
        for skill_id in REQUIRED_COMPOSITION_SKILLS:
            minimum_count = 7 if skill_id in {
                "stock_cross_market_outcome_audit",
                "stock_capital_preservation_recovery_gate",
            } else 5
            if content.count(f'"{skill_id}"') < minimum_count:
                errors.append(f"stock skill is not registered in required assemblies: {skill_id}")
        for skill_id in REQUIRED_LONG_TERM_COMPOSITION_SKILLS:
            if content.count(f'"{skill_id}"') < 3:
                errors.append(f"long-term stock skill is not registered in required assemblies: {skill_id}")
        if 'id: "long_term_total_return_income_strategy"' not in content:
            errors.append("missing long-term total-return assembly")
        for external_skill in [
            "cash_deposit_orchestrator",
            "cash_deposit_bond_substitution_gate",
            "cash_deposit_verification_contract",
        ]:
            if f'id: "{external_skill}"' not in content:
                errors.append(f"missing stock external prerequisite: {external_skill}")

    stock_orchestrator = root / "funagent/skills/stocks/stock_orchestrator.md"
    if stock_orchestrator.is_file():
        content = read_text(stock_orchestrator)
        for token in [
            "cash_deposit_bond_substitution_gate_skill.md",
            "cash_preferred",
            "안전 대체수익",
        ]:
            if token not in content:
                errors.append(f"stock orchestrator does not enforce cash/deposit comparison: {token}")

    bond_registry = root / "funagent/skills/bonds/bond_skill_composition_registry.yaml"
    if bond_registry.is_file():
        content = read_text(bond_registry)
        required_bond_skill_counts = {
            "bond_source_search": 5,
            "bond_evidence_extraction": 5,
            "bond_market_regime_curve": 5,
            "bond_security_fund_analysis": 5,
            "bond_credit_liquidity_risk_gate": 5,
            "bond_portfolio_integration": 5,
            "bond_verification_contract": 5,
            "bond_ladder_liability_matching": 3,
        }
        for skill_id, minimum_count in required_bond_skill_counts.items():
            if content.count(f'"{skill_id}"') < minimum_count:
                errors.append(f"bond skill is not registered in required assemblies: {skill_id}")
        for assembly_id in [
            "individual_bond_ladder",
            "bond_etf_income",
            "duration_tactical",
            "stock_bond_long_term",
            "bond_review_rebuild",
        ]:
            if f'id: "{assembly_id}"' not in content:
                errors.append(f"missing bond assembly: {assembly_id}")
        for external_skill in [
            "cash_deposit_bond_substitution_gate",
            "cash_deposit_verification_contract",
        ]:
            if f'id: "{external_skill}"' not in content:
                errors.append(f"missing bond external prerequisite: {external_skill}")

    cash_registry = root / "funagent/skills/cash/cash_deposit_skill_composition_registry.yaml"
    if cash_registry.is_file():
        content = read_text(cash_registry)
        for skill_id in [
            "cash_deposit_source_search",
            "cash_deposit_product_normalization",
            "cash_deposit_bond_substitution_gate",
            "cash_deposit_verification_contract",
        ]:
            if content.count(f'"{skill_id}"') < 6:
                errors.append(f"cash/deposit skill is not registered in all assemblies: {skill_id}")
        for assembly_id in [
            "short_term_cash_reserve",
            "deposit_ladder",
            "installment_savings_goal",
            "cash_bond_substitution",
            "cash_deposit_review",
        ]:
            if f'id: "{assembly_id}"' not in content:
                errors.append(f"missing cash/deposit assembly: {assembly_id}")

    financial_registry = root / "funagent/skills/financial/financial_skill_composition_registry.yaml"
    if financial_registry.is_file():
        content = read_text(financial_registry)
        for skill_id in [
            "financial_health_liquidity_gate",
            "financial_cross_asset_evidence_synthesis",
            "financial_goal_bucket_design",
            "financial_portfolio_scenario_stress",
            "financial_strategy_verification_contract",
        ]:
            if content.count(f'"{skill_id}"') < 6:
                errors.append(f"financial skill is not registered in all assemblies: {skill_id}")
        for external_id in [
            "stock_strategy_orchestrator",
            "bond_strategy_orchestrator",
            "cash_deposit_orchestrator",
            "crypto_strategy_orchestrator",
        ]:
            if f'id: "{external_id}"' not in content:
                errors.append(f"missing financial external orchestrator: {external_id}")
        for assembly_id in [
            "full_financial_strategy",
            "short_term_financial_stability",
            "long_term_wealth_strategy",
            "retirement_income_strategy",
            "financial_review_rebuild",
        ]:
            if f'id: "{assembly_id}"' not in content:
                errors.append(f"missing financial assembly: {assembly_id}")

    financial_orchestrator = root / "funagent/skills/financial_strategy_orchestrator.md"
    if financial_orchestrator.is_file():
        content = read_text(financial_orchestrator)
        for token in [
            "financial_health_liquidity_gate_skill.md",
            "cash_deposit_orchestrator.md",
            "stock_orchestrator.md",
            "bond_orchestrator.md",
            "crypto_orchestrator.md",
            "financial_strategy_verification_contract_skill.md",
            "가장 낮은 판정",
        ]:
            if token not in content:
                errors.append(f"financial orchestrator missing mandatory contract: {token}")

    crypto_registry = root / "funagent/skills/crypto/crypto_skill_composition_registry.yaml"
    if crypto_registry.is_file():
        content = read_text(crypto_registry)
        required_crypto_skill_counts = {
            "crypto_intake_capital_survival_gate": 7,
            "crypto_source_search_evidence": 7,
            "crypto_custody_counterparty_stablecoin_gate": 7,
            "crypto_portfolio_execution": 7,
            "crypto_verification_contract": 7,
            "crypto_market_regime_flow": 6,
            "crypto_asset_protocol_due_diligence": 5,
            "crypto_forecast_learning_loop": 6,
            "crypto_yield_staking_defi_gate": 4,
        }
        for skill_id, minimum_count in required_crypto_skill_counts.items():
            if content.count(f'"{skill_id}"') < minimum_count:
                errors.append(f"crypto skill is not registered in required assemblies: {skill_id}")
        for assembly_id in [
            "crypto_long_term_core_dca",
            "crypto_spot_tactical",
            "crypto_yield_review",
            "stablecoin_parking_review",
            "crypto_derivatives_hedge",
            "crypto_review_rebuild",
        ]:
            if f'id: "{assembly_id}"' not in content:
                errors.append(f"missing crypto assembly: {assembly_id}")

    crypto_orchestrator = root / "funagent/skills/crypto/crypto_orchestrator.md"
    if crypto_orchestrator.is_file():
        content = read_text(crypto_orchestrator)
        for token in [
            "crypto_intake_capital_survival_gate_skill.md",
            "crypto_custody_counterparty_stablecoin_gate_skill.md",
            "crypto_verification_contract_skill.md",
            "절차 만점",
            "safe_asset_preferred",
        ]:
            if token not in content:
                errors.append(f"crypto orchestrator missing mandatory contract: {token}")

    source_registry = root / "funmemory/sources/source_registry.yaml"
    if source_registry.is_file():
        content = read_text(source_registry)
        for token in ["last_verified:", "verification_policy:", "sources:"]:
            if token not in content:
                errors.append(f"missing token '{token}' in funmemory/sources/source_registry.yaml")
        for source_id in REQUIRED_SOURCE_IDS:
            if f"id: {source_id}" not in content:
                errors.append(f"missing source id '{source_id}' in funmemory/sources/source_registry.yaml")
    else:
        errors.append("missing source registry: funmemory/sources/source_registry.yaml")

    scorecard = root / "funmemory/schemas/verification_scorecard.schema.json"
    if scorecard.is_file():
        content = read_text(scorecard)
        for category in REQUIRED_SCORE_CATEGORIES:
            if category not in content:
                errors.append(f"missing verification category: {category}")

    ledger = root / "funoutput/logs/stock_prediction_ledger.jsonl"
    if ledger.is_file():
        seen_ids: set[str] = set()
        for line_number, line in enumerate(read_text(ledger).splitlines(), start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"invalid prediction ledger JSON at line {line_number}: {exc}")
                continue
            prediction_id = record.get("prediction_id")
            if not prediction_id:
                errors.append(f"missing prediction_id in ledger line {line_number}")
            elif prediction_id in seen_ids:
                errors.append(f"duplicate prediction_id in ledger: {prediction_id}")
            else:
                seen_ids.add(prediction_id)
            probabilities = record.get("probabilities", {})
            try:
                probability_sum = sum(float(probabilities[key]) for key in ("up", "flat", "down"))
            except (KeyError, TypeError, ValueError):
                errors.append(f"invalid probabilities in ledger line {line_number}")
            else:
                if abs(probability_sum - 1.0) > 1e-9:
                    errors.append(f"probabilities do not sum to 1 in ledger line {line_number}")

    crypto_ledger = root / "funoutput/logs/crypto_prediction_ledger.jsonl"
    if crypto_ledger.is_file():
        seen_ids: set[str] = set()
        for line_number, line in enumerate(read_text(crypto_ledger).splitlines(), start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"invalid crypto prediction ledger JSON at line {line_number}: {exc}")
                continue
            prediction_id = record.get("prediction_id")
            if not prediction_id:
                errors.append(f"missing prediction_id in crypto ledger line {line_number}")
            elif prediction_id in seen_ids:
                errors.append(f"duplicate crypto prediction_id: {prediction_id}")
            else:
                seen_ids.add(prediction_id)
            probabilities = record.get("probabilities", {})
            try:
                probability_sum = sum(float(probabilities[key]) for key in ("up", "flat", "down"))
            except (KeyError, TypeError, ValueError):
                errors.append(f"invalid probabilities in crypto ledger line {line_number}")
            else:
                if abs(probability_sum - 1.0) > 1e-9:
                    errors.append(f"crypto probabilities do not sum to 1 in ledger line {line_number}")

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
