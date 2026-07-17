# 국내·미국 주식 전략 전수 감사 및 오케스트레이터 재구축

## 메타

- 리뷰 ID: `2026-07-10-cross-market-strategy-outcome-audit`
- 감사 기준 시각: 2026-07-10 KST
- 감사 대상: 이 리뷰 생성 전 `funoutput/reports` 40개, `funoutput/reviews` 1개
- 감사 도구: `funagent/validators/audit_stock_strategy_history.py`
- 결론: 전략 문서의 자가 교정은 발전했지만 실제 예측 성능을 계산할 불변 원장이 없었다. 11건을 원장에 이관했으나 5건은 원보고서 판정 기준이 빠져 감사 판정은 `audit_conditional`, 실현 예측 품질은 `N/A`다. 신규 전수 감사·잠재 물량·급등/순환 사이클 계약을 상위 게이트로 승격했다.

## 전수 감사 결과

| 항목 | 결과 | 판정 |
|---|---:|---|
| 전략 보고서 | 40 | 전체 검색 완료 |
| 기존 정식 리뷰 | 1 | 성과 리뷰 밀도 부족 |
| 고유 prediction_id | 11 | 최근 2개 보고서에만 존재 |
| 불변 원장 이관 | 11 | `funoutput/logs/stock_prediction_ledger.jsonl`에 open 상태로 이관 |
| 원보고서 성공·실패 기준 누락 | 5 | 금융, HD현대, QQQ, TSM, MSFT 예측에 차단 플래그 |
| ID와 실제 결과가 연결된 예측 | 0 | 실현 예측 품질 산출 불가 |
| 예측성 내용이 있으나 ID가 없는 산출물 | 21 | legacy_unscorable |
| 문장형 결과 행 | 13 | 성공 6, 부분 성공 4, 실패 2, 판정 불가 1 |
| 정식 잠재 물량 계약 적용 보고서 | 0 | 신규 게이트 필요 |
| 정식 급등·순환 사이클 분류 보고서 | 0 | 신규 분류기 필요 |

문장형 결과 13건은 보고서 자체 기록 기준이다. prediction_id와 원래 확률·검증 시각·원천시장 결과가 연결되지 않아 정식 적중률의 분모나 분자로 사용하지 않는다.

## 현재 열린 구조화 예측

| 시장 | prediction_id | 출처 | 상태 |
|---|---|---|---|
| KR | `KR-KOSPI-20260713-01` | `2026-07-10_korea_next_regular_session_profit_max_strategy.md` | 2026-07-13 만기 전 |
| KR | `KR-SEMI-20260713-01` | 동일 | 2026-07-13 만기 전 |
| KR | `KR-AUTO-20260713-01` | 동일 | 2026-07-13 만기 전 |
| KR | `KR-FIN-20260713-01` | 동일 | 2026-07-13 만기 전 |
| KR | `KR-HDH-20260713-01` | 동일 | 2026-07-13 만기 전 |
| US | `US-QQQ-20260710-01` | `2026-07-10_next_session_profit_max_strategy.md` | 2026-07-10 16:00 ET 만기 예정 |
| US | `US-SMH-20260710-01` | 동일 | 2026-07-10 16:00 ET 만기 예정 |
| US | `US-QCOM-20260710-01` | 동일 | 2026-07-10 16:00 ET 만기 예정 |
| US | `US-NVDA-20260710-01` | 동일 | 2026-07-10 16:00 ET 만기 예정 |
| US | `US-TSM-20260710-01` | 동일 | 2026-07-10 16:00 ET 만기 예정 |
| US | `US-MSFT-20260710-01` | 동일 | 2026-07-10 16:00 ET 만기 예정 |

이 11건은 만기 뒤 `stock_prediction_ledger.schema.json`에 원래 확률을 동결한 채 실제 결과를 연결해야 한다. 결과가 나온 뒤에도 미채점이면 `matured_unscored`다.

## 성공·실패 데이터에서 확인한 패턴

### 유지할 성공 규칙

- NXT·프리마켓·장초반 급등을 확정 매수 신호로 쓰지 않고 09:30~10:30 또는 10:30 ET 이후 VWAP과 수급으로 재검증하는 규칙.
- 반도체 ETF 강세를 모든 종목 강세로 일반화하지 않고 엔비디아/NVIDIA Corporation (NVDA), 퀄컴/QUALCOMM Incorporated (QCOM) 등 종목별 상대강도를 분리하는 규칙.
- 강한 종목도 보호 가격과 이익 실현 구간을 올리며 추격보다 손익비를 관리하는 규칙.
- 폭락 뒤 현금 보유자의 선진입보다 선물·프로그램 매도 둔화와 가격 회복을 기다리는 규칙.

### 반복 실패·부분 성공 패턴

| 실패 모드 | 보고서에서 확인된 현상 | 강화 규칙 |
|---|---|---|
| 숨은 기대치 오판 | 좋은 실적·뉴스에도 삼성전자/Samsung Electronics (005930) 가격 반응 부진 | 공식 컨센서스와 선반영 기대를 분리하고 발표 후 VWAP을 우선 |
| 장전·장초반 신호 과신 | NXT 강세 뒤 KRX 정규장 되밀림 | 선행가격은 온도계로만 쓰고 정규장 체결·수급으로 재판정 |
| 상위 수급 누락 | 개별 호재보다 외국인·기관·프로그램·ETF 매도가 강함 | 시장·섹터 기계적 수급을 종목 뉴스보다 상위 게이트로 적용 |
| 섹터 내부 분산 오판 | ETF는 강하지만 대장주와 후발주의 방향이 갈림 | 대장·준대장·후발·ETF 상대강도를 따로 분류 |
| 진입 품질 미검증 | 방향 판단은 맞아도 호가·슬리피지·체결 결과가 없음 | 예측 성공과 실행 성공을 분리 |
| 사이클 단계 누락 | 급등·순환 표현은 있으나 ignition/exhaustion, accumulation/distribution 정식 판정이 없음 | 확률형 사이클 분류와 단계별 보유 기간 강제 |

## 잠재 매수·매도 물량 감사

기존 보고서 40개 중 호가·잔량·매물 관련 언급은 일부 있었지만 다음 항목을 한 계약으로 묶은 보고서는 없었다.

- 복수 가격 레벨과 최소 3회 호가 스냅샷.
- 표시 잔량의 유지·취소·재충전과 실제 체결 방향.
- 매수·매도 흡수, VWAP/anchored VWAP, volume-at-price.
- Nasdaq/NYSE 오픈·클로징 경매 불균형 또는 KRX 단일가·프로그램 흐름.
- 증자, ATM, CB/BW, 워런트, 보호예수, 내부자 거래, 블록딜, ETF·지수 리밸런싱 잠재 공급.
- 미국 depth의 venue coverage와 숨은·off-exchange 유동성 한계.

따라서 기존 보고서의 호가 점수가 높더라도 `쌓인 물량 또는 쏟아질 물량 예측 적중`은 검증 완료로 볼 수 없다.

## 급등주·순환주 감사

기존 산출물에는 급등주 위험 검토와 섹터 순환 해석이 있었지만, 두 유형을 확률과 신뢰도로 구분하는 공통 분류기는 없었다.

| 클래스 | 필요한 구분 |
|---|---|
| parabolic_event_momentum | 단일 촉매, 비정상 RVOL·회전율, 좁은 유통물량, 희석·숏커버 위험 |
| rotational_cyclical | 섹터 폭 확장, 대장→후발 순환, 이익·산업 사이클, 기관성 수급 지속 |
| structural_trend_leader | 장기 상대강도, 실적·추정치 상향, 구조적 수요 |
| mean_reversion_rebound | 급락 뒤 기술적 복원과 숏커버, 추세 전환 미확정 |
| distribution_markdown | 호재 반응 약화, 고점 매도 흡수, VWAP 이탈, 섹터 폭 축소 |

급등주와 순환주의 최고 확률 차이가 15%p 미만이면 hybrid로 처리하고, 가격·거래량만으로 분류하면 신뢰도는 60을 넘길 수 없도록 계약했다.

## 새 오케스트레이터 계약

1. 전수 감사: 모든 보고서와 리뷰를 prediction_id 원장으로 대조한다.
2. 최근 학습: 금주 복기는 전체 원장의 이동 창으로만 사용한다.
3. 시장구조: 기계적 수급 뒤에 잠재 매수·매도 물량 게이트를 통과한다.
4. 유형 판정: 시장 국면 뒤 급등·순환 사이클을 확률로 분류한다.
5. 예측 보정: 전수 Brier·미채점 비율, 물량 상태, 사이클 신뢰도를 확률 상한에 반영한다.
6. 실행: 예측 적중, 체결·비용 후 수익, 손절·비중 준수를 각각 결산한다.
7. 점수 무결성: 모든 Verify 점수는 evidence_id와 연결하고 unknown 또는 matured_unscored가 있으면 100점을 금지한다.

## 대표 보고서 재검증

| 보고서 | 새 계약 판정 | 누락 |
|---|---|---|
| `2026-07-10_korea_next_regular_session_profit_max_strategy.md` | conditional | 국내·미국 전수 감사, 잠재 물량·오버행, 급등·순환 사이클 분류 |
| `2026-07-10_next_session_profit_max_strategy.md` | conditional | 국내·미국 전수 감사, 잠재 물량·오버행, 급등·순환 사이클 분류 |

두 보고서의 기존 최종 판정이 이미 `조건부 검토`였으므로 결론을 소급 변경하지 않았다. 다만 새 계약에서는 세 신규 게이트를 채우기 전 `진행 가능`이나 공격적 신규 진입으로 승격할 수 없다.

## 표본·승격 기준

- 성숙·채점 20개 미만: `insufficient_sample`.
- 20~49개: `provisional`. 기준 완화 금지.
- 50개 이상이며 불리한 국면 10개 이상: champion 규칙 승격 검토 가능.
- matured_unscored 3개 이상 또는 10% 초과: 최종 결론 `조건부 검토` 이하.
- matured_unscored 5개 이상 또는 20% 초과: 공격적 신규 진입 차단.

## 점수 판정

| 점수 영역 | 현재 판정 | 이유 |
|---|---|---|
| 전략 절차·구조 | 개선 완료 | 신규 스킬·스키마·템플릿·검증 계약 연결 |
| 실현 예측 품질 | N/A | ID와 실제 결과가 연결된 성숙 표본 0건 |
| 실행 품질 | N/A | 체결가·슬리피지·비용·MFE/MAE 원장 없음 |
| 리스크 준수 | N/A | 실제 주문·손절 준수 기록 없음 |
| 수익 보장 여부 | 금지 | 미래 수익과 무손실은 어떤 점수로도 보장할 수 없음 |

## 공식 시장구조 근거

- KRX 프로그램 거래: https://global.krx.co.kr/contents/GLB/06/0602/0602010204/GLB0602010204T4.jsp
- KRX VI: https://global.krx.co.kr/contents/GLB/06/0602/0602020204/GLB0602020204T7.jsp
- Nasdaq Opening/Closing Cross와 NOII: https://nasdaqtrader.com/Trader.aspx?id=OpenClose
- NYSE Auctions와 Order Imbalances: https://www.nyse.com/trade/auctions
- SEC market activity와 hidden/cancel 지표: https://www.sec.gov/securities-topics/market-structure-analytics/market-activity-data-visualizations
- FINRA short interest와 short sale volume 구분: https://www.finra.org/investors/insights/short-interest
- SEC Form 13F 제출 지연: https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f
- SEC 주문 체결 설명: https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/executing-order

## 최종 결론

오케스트레이터는 이제 `좋은 분석 문서`를 반복 생성하는 수준이 아니라, 과거 예측을 빠짐없이 결산하고 물량·사이클·실행 오류를 다음 확률과 Verify 기준에 되먹임하는 구조를 갖췄다. 다만 최고의 수익 성능은 아직 입증되지 않았다. 첫 검증 과제는 현재 열린 11개 prediction_id를 만기 뒤 원장에 결산해 실제 Brier score, 범위 오차, 비용 후 실행 결과를 만드는 것이다.
