# 스킬: 국내·미국 전략 전수 성과 감사

## 목적

`funoutput/reports`와 `funoutput/reviews`의 국내·미국 주식 전략을 빠짐없이 원장화하고, 예측 품질·주문 실행 품질·리스크 준수 품질을 분리 평가한다. 최근 성공 사례만 골라 보는 편향, 결과가 나온 예측만 채점하는 편향, 한국과 미국의 서로 다른 수급 의미를 섞는 오류를 차단한다.

## 적용 조건

- 과거 주식 전략 보고서가 1개 이상 존재하는 모든 신규 주식 전략.
- 성공률, 실패 감소, 반복 개선, 최고의 전략, 만점 전략을 요청한 경우.
- 국내와 미국 전략 결과를 함께 비교하거나 한 시장의 규칙을 다른 시장에 전이하려는 경우.
- 금주 예측 복기, 전망 실패 사후분석, 성과 검토를 수행하기 전.

## 핵심 계약

- 모든 예측은 원래 작성 시점의 `prediction_id`, 확률, 범위, 무효화 조건을 동결한다. 수정 예측은 원본을 덮지 않고 `parent_prediction_id`를 가진 새 레코드로 남긴다.
- 보고서 전체를 검색한다. 성공 사례, 실패 사례, 미성숙 예측, 판정 불가 예측을 모두 포함한다.
- `prediction_id`가 없는 과거 문장은 `legacy_unscorable`로 보존하되 적중률 분모·분자에 넣지 않는다.
- ID가 있어도 성공·실패 기준, 검증 시각, 원확률 중 하나가 빠지면 `invalid_prediction_contract`로 표시하고 신규 전략의 성능 근거로 쓰지 않는다.
- 검증 시각이 지났지만 실제 결과가 없는 예측은 `matured_unscored`로 남긴다. 삭제하거나 판정 불가로 숨기지 않는다.
- 방향 예측의 성공과 실제 거래 수익을 분리한다. 방향이 맞아도 진입 미체결, 과도한 슬리피지, 손절 위반이면 실행 성공이 아니다.
- 한국과 미국, 장중·다음날·주간, 급등·순환·방어 국면을 한 적중률로 합치지 않는다.
- 한국의 외국인·기관·프로그램 순매수와 미국의 ETF·경매·옵션·공시 포지션 자료를 같은 지표처럼 취급하지 않는다.
- 사후 정보로 당시 확률을 바꾸는 룩어헤드, 결과에 맞춘 성공 기준 변경, 후보 탈락 종목 삭제를 금지한다.
- 100점은 증거와 절차 완결성 점수일 뿐 수익 가능성이나 미래 적중을 뜻하지 않는다.

## 원장 필수 필드

원장 경로는 `funoutput/logs/stock_prediction_ledger.jsonl`로 고정하고 한 줄에 한 JSON 레코드를 저장한다. 기존 레코드는 수정 예측으로 덮지 않으며 만기 결과 필드만 결산한다.

| 묶음 | 필드 |
|---|---|
| 식별 | prediction_id, parent_prediction_id, source_report, strategy_id, market, venue, symbol, display_name |
| 시간 | created_at, data_as_of, horizon, verification_due_at, scored_at |
| 원예측 | 상승·혼조·하락 확률, 예상 범위, 성공 기준, 실패 기준, 무효화 조건, position_action |
| 당시 상태 | market_regime, cycle_class, supply_demand_state, source_ids, missing_data |
| 실제 결과 | actual_direction, actual_range, close_vs_vwap, benchmark_relative_return, flow_result, fx_result |
| 실행 결과 | order_status, fill_price, slippage_bps, fees_tax_fx, MFE, MAE, realized_return, stop_followed |
| 판정 | forecast_outcome, execution_outcome, risk_outcome, failure_modes, adjudication_notes |

원장 레코드는 `funmemory/schemas/stock_prediction_ledger.schema.json`을 따른다.

## 감사 절차

1. 전체 보고서·리뷰 파일 목록과 작성 시각을 고정한다.
2. 각 파일을 `KR`, `US`, `MIXED`, `UNKNOWN`과 `intraday`, `next_day`, `next_week`, `swing`, `long_term`으로 분류한다.
3. prediction_id와 원예측을 추출한다. ID 없는 예측성 문장은 `legacy_unscorable`로 목록화한다.
4. 중복 ID, 수정본의 원본 덮어쓰기, 검증 시각 누락, 결과 기준 변경을 탐지한다.
5. 검증 기한이 지난 모든 예측에 실제 데이터를 연결한다. 당시 정의한 기준을 그대로 사용한다.
6. `forecast_outcome`, `execution_outcome`, `risk_outcome`을 각각 판정한다.
7. 시장·기간·국면·사이클·전략 버전별 지표를 계산한다.
8. 성공 요인은 유지 후보, 실패 요인은 제거·강화 후보로 분리한다.
9. 최근 표본만이 아니라 전체 표본과 최근 이동 창을 함께 비교해 성능 악화를 찾는다.
10. 현재 전략에 적용할 확률 상한, 금지 조건, Verify 점수 강화안을 만든다.

## 필수 성과 지표

| 영역 | 지표 |
|---|---|
| 데이터 완결성 | 전체 보고서 수, ID 보유 보고서 비율, 성숙 예측 수, 미채점 수, 중복 ID 수 |
| 방향 품질 | 방향 적중률, 클래스별 적중률, 상승 편향, 하락 누락률 |
| 확률 품질 | 다중 클래스 Brier score, log loss, 신뢰구간별 실제 발생률, calibration error |
| 범위 품질 | 예상 범위 포함률, 중심값 MAE, 상·하단 이탈률 |
| 선택 품질 | 거래 허용률, watch_only 비율, 선택적 적중률, 기회 누락률 |
| 실행 품질 | 체결률, 슬리피지, 비용 후 기대값, MFE/MAE, 손절 준수율 |
| 위험 품질 | 최대낙폭, 1회 손실 한도 위반, 집중도 위반, 무효화 후 추가매수 건수 |

다중 클래스 Brier score는 `sum((p_i - y_i)^2)`로 계산하고 확률은 0~1을 사용한다. 표본이 부족하면 숫자를 만들지 않고 `insufficient_sample`로 남긴다.

## 표본과 승격 규칙

- 성숙·채점 예측 20개 미만인 시장·기간 버킷은 `insufficient_sample`이다.
- 20~49개는 `provisional`이며 규칙 완화와 모델 승격 근거로 쓰지 않는다.
- 50개 이상이고 불리한 국면 표본이 10개 이상일 때만 `promotion_eligible`로 본다.
- 새 규칙은 같은 기간의 과거 자료에 맞춰 튜닝한 뒤 같은 자료로 승격하지 않는다. 이후 시점의 champion-challenger 표본으로 검증한다.
- 단일 성공, 단일 급등장, 한 종목의 성공으로 다른 시장·기간의 기준을 낮추지 않는다.
- 시장·기간 버킷의 `matured_unscored`가 3개 이상 또는 10% 초과면 최종 결론은 `조건부 검토` 이하로 낮춘다.
- `matured_unscored`가 5개 이상 또는 20% 초과면 공격적 신규 진입을 `blocked`로 낮춘다.

## 점수 보정

- 동일 실패 모드 2회: 관련 Verify 최소 점수 +3 및 누락 데이터 필수화.
- 동일 실패 모드 3회 또는 critical 1회: +5 및 중대 차단 조건 승격.
- 성공 규칙은 두 시장에서 동시에 통했다고 합치지 않는다. 각 시장·기간에서 독립적으로 검증한다.
- Brier score나 calibration error가 악화되면 방향 적중률이 높아도 확률 상한을 낮춘다.
- watch_only만 늘려 선택적 적중률이 높아진 경우 거래 허용률을 함께 표시해 과도한 회피를 감춘 개선으로 인정하지 않는다.

## 출력

- `cross_market_outcome_audit_packet`
- 전체 파일 수와 시장별·기간별 커버리지.
- machine_scoreable, legacy_unscorable, matured_unscored 목록.
- invalid_prediction_contract와 원보고서 누락 필드 목록.
- 시장·기간·국면별 성과표와 표본 등급.
- forecast/execution/risk 결과 분리표.
- 반복 성공 규칙, 반복 실패 모드, 시장 간 전이 금지 규칙.
- 현재 전략의 확률·비중 상한과 Verify 강화안.
- 최종 판정: `audit_clear`, `audit_provisional`, `audit_conditional`, `audit_blocked`.

## 중대 차단 조건

- 일부 보고서나 성공 사례만 골라 전수 성과로 표현한다.
- ID 없는 문장을 적중률 표본으로 계산한다.
- 성공·실패 기준이 빠진 ID를 완전한 검증 예측으로 취급한다.
- 검증 기한이 지난 예측을 누락하거나 삭제한다.
- 원예측 확률·범위·성공 기준을 실제 결과를 본 뒤 변경한다.
- 국내와 미국, 장중과 주간, 급등과 순환 국면을 단일 적중률로 합친다.
- 예측 적중과 거래 수익·손절 준수를 같은 성공으로 처리한다.
- 표본이 부족한데 만점, 최고, 검증 완료, 수익 가능성 향상을 단정한다.
