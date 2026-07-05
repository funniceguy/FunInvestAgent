# funagent

`funagent`는 FunInvestAgent의 행동 계층입니다. 각 에이전트의 책임, 워크플로우, 스킬, 판단 규칙, 검증기를 관리합니다.

## 하위 구조

```text
funagent/
  agents/       역할별 에이전트 정의
  config/       에이전트 매니페스트
  rules/        판단 정책, 리스크 점수, 검증 체크리스트
  skills/       재무 진단, 도메인 리서치, 법률 이슈 스팟팅, 리포트 생성
    stocks/     주식 단타/가치투자 오케스트레이터와 하위 스킬
  validators/   산출물 검증 도구
  workflows/    세션, 시장조사, 포트폴리오, 법률 검토, 주식 전략 흐름
```

## 실행 흐름

1. `Session Manager Agent`가 사용자 입력과 작업 범위를 정리한다.
2. `Financial Partner Agent`가 목표와 재무 체력을 진단한다.
3. `Market Research Agent`가 자산군별 데이터를 수집한다.
4. `Portfolio Strategy Agent`가 시나리오별 전략을 만든다.
5. `Risk & Compliance Agent`와 `Legal Review Agent`가 위험과 법률 이슈를 점검한다.
6. `Report Writer Agent`가 `funoutput/templates` 형식으로 산출한다.
7. 검증기가 필수 섹션과 출처 최신성 필드를 확인한다.

## 주식 전략 스킬

주식 요청은 `funagent/skills/stocks/stock_orchestrator.md`를 중심으로 조립한다. 오케스트레이터는 데이터 수집, 시장 국면, 후보군 선별, 저평가 우량주 정밀 스크리닝, 단타 전술, 가치투자 전략, 포트폴리오 구성, 실행 리스크, 성과 검토 스킬을 필요에 따라 조합한다.

주식 전략과 최종 리포트는 `stock_verification_contract_skill.md`와 `funagent/rules/verification_score_contract.md`의 평점 계약을 통과해야 한다. 최소 2회 반복 검증하고, 전체 가중 점수 88점 미만 또는 중대 차단 조건이 있으면 결론을 보류/중단으로 낮춘다.

차주 또는 미래 전망 기반 전략은 `stock_forward_source_search_skill.md`, `stock_forward_evidence_extraction_skill.md`, `stock_forward_outlook_synthesis_skill.md`를 순서대로 통과해야 한다. 세계정세, 경제상황, 개인·외국인·기관 심리는 공식/시장 데이터 출처와 근거 카드, 기본/강세/약세 시나리오로 검증한 뒤 전략에 반영한다.

투자자 심리 해석은 필수 게이트다. 주식 전략은 정보 등급, 기대치, 포지션, 가격 반응, 수급 지속성을 해석하고 `stock_psychology_decision_gate_skill.md` 결과가 신규 진입을 허용할 때만 실행 전략으로 승격한다.

공격적 단기 매매는 `stock_aggressive_short_term_probability_skill.md`를 통과해야 한다. 기대치, 가격 반응, 거래대금, 기관/외국인/프로그램 수급, 환율, 상대강도, 손익비가 정렬되지 않으면 신규 진입은 관찰 또는 차단으로 낮춘다.

저평가 우량주, GARP, 밸류업 수혜주 후보는 `stock_quality_value_screening_skill.md`를 통과해야 한다. 저PER·저PBR·고배당 단독 통과는 금지하며, 성장성, ROE/ROIC, 현금흐름, 부채, PEG 또는 대체 밸류에이션, 촉매, 가치함정 플래그를 검증한다.

미국 주식 장중 수익화·단타·분할 주문 전략은 `stock_us_intraday_order_timing_skill.md`를 통과해야 한다. ET/KST 시간대, 서머타임, 휴장·조기폐장, 프리마켓·애프터마켓 유동성 위험, 한국 시간 피로 게이트를 확인한 뒤 주문 행동을 제한한다.
