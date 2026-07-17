# 주식 전략 리포트

## 메타

- 전략 ID: US-SEMICONDUCTOR-SELL_OFF-NEXT_DAY-2026-07-08
- 작성일: 2026-07-08 KST
- 기준 통화: USD
- 시장 범위: 미국 주식, 미국 상장 반도체 개별주, 미국 ETF
- 전략 모드: 보유 포지션 방어 / 단타 / 공격적 단기 검토 / 내일 재검증

## 입력 데이터와 가정

- 투자 가능 자금: 미제공. 실제 금액 대신 `투자 가능 주식 예산 대비 비중`으로만 제시한다.
- 단타 최대 손실 가능 자금: 미제공. 단타 1회 손실 한도는 단타 슬리브의 0.25-0.50% 이하로 가정한다.
- 가치투자 목표 기간: 미제공. 이번 리포트는 장기 가치투자 결론이 아니라 보유 중인 단기 대응과 내일 전략이다.
- 현재 보유 종목: 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA).
- 비상금/부채/확정 지출: 미제공. 생계자금, 비상금, 1년 내 확정 지출 자금으로 단타하지 않는 것을 기본 가정한다.
- 부족한 정보: 실제 매수가, 보유 비중, 계좌 통화, 세금/수수료, 최대 손실 허용치, 장중 대응 가능 여부, 브로커 연장거래 가능 시간, 실시간 VWAP, 기관·외국인·프로그램 순매수 데이터.
- 사용한 가정: 사용자는 한국 거주자로 가정하고, 2026-07-08 KST는 미국 2026-07-07 정규장 중이다. 7월은 미국 서머타임이므로 ET + 13시간을 적용한다.

## 요약

- 결론: `보류`. 반도체 신규 저점 매수와 물타기는 아직 금지하고, 보유 중인 퀄컴/QUALCOMM Incorporated (QCOM)과 엔비디아/NVIDIA Corporation (NVDA)는 내일 미국장 회복 조건을 확인한 뒤 방어 또는 축소를 결정한다.
- 현재 행동: 반도체 신규 매수 중단, 보유 포지션은 무효화선 기준으로 방어, 내일 10:30-11:30 ET에 회복 품질 재검증.
- 자금 배분: 단타 슬리브 0-3%, 반도체 신규 진입 0%, 현금/대기 70-100%, 기존 보유분은 사용자 평균단가와 손실 허용치에 따라 별도 관리.
- 주요 종목/상품 표시명: 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA), VanEck Semiconductor ETF (SMH), iShares PHLX SOX Semiconductor Sector Index Fund (SOXX), Invesco QQQ Trust, Series 1 (QQQ).
- 가장 큰 리스크: 좋은 실적 뉴스에도 반도체가 팔리는 `기대치 과포화`, 반도체 ETF 지지선 이탈, 내일 FOMC 의사록 전후 금리·나스닥 변동성 확대.
- 다음 검토일: 2026-07-08 10:30 ET, 2026-07-08 14:00 ET FOMC 의사록 전후, 2026-07-08 15:30 ET 종가 전.

## 시장 국면

- 국면: 방어.
- 근거:
  - 2026-07-07 11:16 ET 기준 VanEck Semiconductor ETF (SMH)는 572.09달러, -5.33%로 600달러 회복 실패.
  - iShares PHLX SOX Semiconductor Sector Index Fund (SOXX)는 540.3506달러, -7.08%로 반도체 전반의 매도 압력이 개별 이슈가 아니라 섹터 이슈임을 보여준다.
  - Invesco QQQ Trust, Series 1 (QQQ)는 707.145달러, -2.17%로 이전 단기 반등 무효화 기준 718달러를 이탈했다.
  - 방어 섹터인 State Street Health Care Select Sector SPDR ETF (XLV)는 +1.75%, State Street Consumer Staples Select Sector SPDR ETF (XLP)는 +1.50%로 기술주에서 방어 섹터로 자금 회전이 확인된다.
- 자금 투입 강도: 신규 공격 0, 제한적 관찰 1, 보유 방어 4, 현금 5.
- 경계 이벤트: 2026-07-08 ET FOMC 의사록, 반도체 실적 시즌 진입, 아시아 반도체 선행 반응, 장중 ETF 프로그램 매도.

## 차주/미래 전망 근거 검색·발췌·분석

- 적용 여부: 예.
- 전망 기간: next_week.
- 검색 기준 시각: 2026-07-08 00:00-00:25 KST.
- 최종 판정: `conditional_outlook`.
- 전망 점수: 82/100.
- 전략 방향: 방어.
- 결론 제한 사유: 실시간 기관·외국인·프로그램 순매수와 VWAP를 직접 확인하지 못했고, ETF NAV/IOPV 괴리율도 실시간 확인하지 못했다. 따라서 신규 진입은 `진행 가능`이 아니라 `보류`다.

### 검색 커버리지

| 영역 | 핵심 출처 | source_tier | 기준일 | 사용 가능 여부 |
|---|---|---|---|---|
| 세계정세 | Investors Business Daily, MarketWatch: DeepSeek 자체 칩 개발 보도와 AI 칩 경쟁 우려 | trusted_secondary | 2026-07-07 | 조건부 사용 |
| 경제상황 | FRED 10년물 국채금리 DGS10 | primary / market_data | 2026-07-02, 4.49% | 사용 |
| 유동성/환율 | FRED DGS10, 나스닥 ETF 가격 반응 | market_data | 2026-07-07 | 조건부 사용 |
| 원자재 | 해당 없음. 이번 하락은 원자재보다 AI·반도체 기대치와 수급 재가격화가 핵심 | primary / market_data | 2026-07-08 | 제한적 |
| 투자자 심리 | 삼성전자 공식 가이던스 + 보조 뉴스의 주가 반응 해석 | primary / trusted_secondary | 2026-07-07 | 사용 |
| 이벤트 캘린더 | Federal Reserve FOMC 일정, Nasdaq 거래시간·휴장 정보 | primary | 2026-07-07/08 | 사용 |

### 근거 카드

| evidence_id | source_id | fact_type | 발췌 사실 | 시장 전달 경로 | 영향 자산 표시명 | 방향 | 신뢰도 | 반대 근거 |
|---|---|---|---|---|---|---|---|---|
| E1 | samsung_q2_2026_guidance | earnings | 삼성전자/Samsung Electronics (005930.KS)는 2026년 2분기 매출 171조원, 영업이익 89.4조원 가이던스를 발표했다. | earnings / supply_chain | 삼성전자/Samsung Electronics (005930.KS), 마이크론/Micron Technology (MU), 엔비디아/NVIDIA Corporation (NVDA), VanEck Semiconductor ETF (SMH) | mixed | high | 숫자는 강하지만 주가 반응은 약했다. |
| E2 | marketwatch_samsung_reaction | sentiment | 삼성전자/Samsung Electronics (005930.KS) 주가는 강한 실적에도 약 7% 하락했고, SK하이닉스/SK hynix Inc. (000660.KS)도 동반 약세였다. | risk_appetite / supply_chain / flows | VanEck Semiconductor ETF (SMH), iShares PHLX SOX Semiconductor Sector Index Fund (SOXX) | risk_off | medium | 장기 메모리 업황 자체는 여전히 강하다는 의견도 존재한다. |
| E3 | ibd_chip_fall | sentiment | 미국 반도체는 삼성전자/Samsung Electronics (005930.KS) 실적 호조에도 하락했다. 기대치가 이미 높았고, 삼성 발표에는 향후 가이던스와 세부 반도체 설명이 부족했다는 해석이 나왔다. | expectations / earnings / flows | 마이크론/Micron Technology (MU), 브로드컴/Broadcom Inc. (AVGO), 엔비디아/NVIDIA Corporation (NVDA) | risk_off | medium | 공식 공시가 아니라 보조 해석이다. |
| E4 | ibd_deepseek | geopolitical / competition | DeepSeek의 자체 AI 칩 개발 보도가 외부 칩 공급업체의 장기 멀티플에 부담으로 작용했다. | supply_chain / valuation | 엔비디아/NVIDIA Corporation (NVDA), 브로드컴/Broadcom Inc. (AVGO), Advanced Micro Devices, Inc. (AMD) | risk_off | medium | 단기 실적 영향은 아직 불확실하다. |
| E5 | nasdaq_quotes_2026_07_07_1116 | market_data | VanEck Semiconductor ETF (SMH) -5.33%, iShares PHLX SOX Semiconductor Sector Index Fund (SOXX) -7.08%, Invesco QQQ Trust, Series 1 (QQQ) -2.17%. | price / flows / relative_strength | VanEck Semiconductor ETF (SMH), iShares PHLX SOX Semiconductor Sector Index Fund (SOXX), Invesco QQQ Trust, Series 1 (QQQ) | risk_off | high | 장중 데이터라 종가 확정 전이다. |
| E6 | nasdaq_hours | schedule | Nasdaq 정규장은 09:30-16:00 ET, 프리마켓은 04:00-09:30 ET, 애프터마켓은 16:00-20:00 ET다. | execution | 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA) | neutral | high | 브로커별 연장거래 가능 시간은 다를 수 있다. |
| E7 | fred_dgs10 | rates | FRED DGS10은 2026-07-02 기준 4.49%로 표시됐다. | rates / valuation | Invesco QQQ Trust, Series 1 (QQQ), 엔비디아/NVIDIA Corporation (NVDA) | mixed | high | 당일 장중 금리와는 시차가 있다. |

### 시나리오 합성

| 시나리오 | 조건 | 예상 심리/수급 | 유리한 섹터 | 불리한 섹터 | 확인 트리거 | 무효화 조건 |
|---|---|---|---|---|---|---|
| 기본 | 반도체가 장중 반등해도 VanEck Semiconductor ETF (SMH) 580-590 회복에 그침 | 개인: 저점매수 충동, 외국인/글로벌펀드: 확인 전 대기, 기관/프로그램: ETF 리밸런싱 매도 우세 | 헬스케어, 필수소비재, 현금성 대기 | 반도체, AI 하드웨어, 메모리 | Invesco QQQ Trust, Series 1 (QQQ) 712 회복, VanEck Semiconductor ETF (SMH) 580 회복 | Invesco QQQ Trust, Series 1 (QQQ) 707 이탈 지속, VanEck Semiconductor ETF (SMH) 572 미회복 |
| 강세 | 내일 10:30-11:30 ET에 VanEck Semiconductor ETF (SMH) 590 회복, 종가 600 근접 | 개인: 안도 매수, 외국인/글로벌펀드: 숏커버, 기관/프로그램: ETF 매도 완화 | 엔비디아/NVIDIA Corporation (NVDA) 같은 상대강도 우위 대형주 | 과도하게 무너진 장비·메모리 추격 | 엔비디아/NVIDIA Corporation (NVDA) 196-200 회복, 퀄컴/QUALCOMM Incorporated (QCOM) 184-186 회복 | 종가에 다시 긴 윗꼬리와 ETF 재이탈 |
| 약세 | 삼성전자/Samsung Electronics (005930.KS) 호재 매도 이후 미국 반도체 ETF가 추가 저점 갱신 | 개인: 손실 복구 물타기, 외국인/글로벌펀드: 위험 축소, 기관/프로그램: 섹터 ETF 매도 지속 | 현금, 단기채, 방어 섹터 | 반도체 전반, 특히 메모리·장비 | VanEck Semiconductor ETF (SMH) 566 하향 이탈, iShares PHLX SOX Semiconductor Sector Index Fund (SOXX) 536 이탈 | VanEck Semiconductor ETF (SMH) 600 종가 회복 |

### 전망 기반 전략 연결

- 세계정세 영향: DeepSeek 등 자체 칩 개발 흐름은 엔비디아/NVIDIA Corporation (NVDA)와 브로드컴/Broadcom Inc. (AVGO)의 장기 독점 기대치를 낮추는 재료로 해석될 수 있다. 단, 단기 실적 훼손은 아직 확인되지 않았다.
- 경제상황 영향: 10년물 4.49%는 성장주 밸류에이션에 부담이 될 수 있다. 금리 자체보다 FOMC 의사록 전후의 해석 변화가 내일 장중 변동성을 키울 수 있다.
- 환율/금리/원자재 영향: 환율은 직접 확인 부족으로 공격적 단기 진입 근거에서 제외한다. 금리 이벤트 전에는 반도체 멀티플 재확대보다 리스크 관리가 우선이다.
- 개인 투자심리 예측: 급락한 대형 반도체를 싸게 보려는 저점매수 충동과 본전 심리가 강해질 수 있다.
- 외국인 투자심리 예측: 미국장에서는 외국인 순매수 통계를 직접 확인하기 어렵다. 글로벌 펀드 관점에서는 아시아 반도체 약세와 미국 ETF 약세가 동시 발생해 신규 매수보다 위험 축소 가능성이 높다.
- 기관 투자심리 예측: 삼성전자/Samsung Electronics (005930.KS) 호재에도 매도된 것은 실적 숫자보다 `다음 분기 기대치`와 `포지션 혼잡도`를 더 중시하는 기관성 반응으로 본다.
- 차주 우선 관찰 지표: VanEck Semiconductor ETF (SMH) 600 회복 여부, Invesco QQQ Trust, Series 1 (QQQ) 718 회복 여부, 엔비디아/NVIDIA Corporation (NVDA) 200 회복 여부, 퀄컴/QUALCOMM Incorporated (QCOM) 186 회복 여부.
- 다음 검색/재검증 시각: 2026-07-08 08:30 ET 프리마켓, 10:30 ET, 14:00 ET, 15:30 ET.

## 투자자 심리 해석 게이트

- 정보 등급: B. 삼성전자 공식 가이던스는 A급 공식 데이터이나, 미국 반도체 하락 원인 해석 중 DeepSeek·기관 포지션 관련 내용은 보조 출처와 가격 반응 기반 추론이다.
- 핵심 흐름: 정보 -> 기대치 -> 포지션 -> 가격 반응 -> 수급 지속성
  - 정보: 삼성전자/Samsung Electronics (005930.KS)의 강한 실적 가이던스, DeepSeek 자체 칩 개발 보도, 반도체 ETF 급락.
  - 기대치: AI·메모리 호황은 이미 시장에 상당 부분 선반영되어 있었다.
  - 포지션: 2026년 반도체·AI 칩 랠리 후 포지션이 혼잡했을 가능성이 높다.
  - 가격 반응: 좋은 뉴스에도 삼성전자와 미국 반도체 ETF가 하락했다.
  - 수급 지속성: 장중 기준 반도체 ETF와 주요 반도체주가 동반 하락해 분산 또는 리스크 축소 가능성이 높다.
- 기대치 상태: in_line_to_under_expected. 숫자는 강하지만 시장의 기대 허들을 크게 넘지 못했다.
- 포지션 상태: crowded.
- 가격 반응: weak_intraday.
- 수급 지속성: weak.
- 심리 플래그: FOMO, 공포, 본전 심리, 처분효과, 과잉확신.
- 게이트 평균 점수: 5.6/10.
- 중대 위험: 호재에도 가격 반응이 약함, 섹터 ETF 동반 급락, 개인 저점매수 충동, 실시간 기관·프로그램 수급 미확인.
- 최종 판정: `watch_only`.

| 항목 | 점수(0-10) | 근거 |
|---|---:|---|
| 정보 신선도 | 8 | 삼성전자 공식 2분기 가이던스와 당일 미국장 반응. |
| 실적 연결성 | 7 | 메모리·AI 수요와 연결되지만 미국 개별 종목별 실적 민감도는 다르다. |
| 기대 대비 | 4 | 강한 숫자에도 매도된 것은 기대치가 더 높았음을 의미한다. |
| 선반영 위험 | 3 | 반도체·AI 체인이 이미 급등해 선반영 위험이 컸다. |
| 가격 반응 | 3 | VanEck Semiconductor ETF (SMH), iShares PHLX SOX Semiconductor Sector Index Fund (SOXX), 퀄컴/QUALCOMM Incorporated (QCOM)이 동반 약세. |
| 거래량 해석 | 5 | 거래량은 충분하지만 매집보다 리스크 축소에 가까운 가격 반응. |
| 수급 지속성 | 4 | 직접 수급은 미확인이나 ETF·개별주 동반 하락은 지속 매도 압력 신호. |
| 개인 과열 | 6 | 급락 후 저점매수 심리가 커질 수 있어 중립 이하. |
| 매물대 부담 | 6 | 반등 시 전일·당일 손실 매물대가 부담. |
| 선발대 여부 | 3 | 지금 신규 진입은 선발대가 아니라 후발 저점매수에 가깝다. |

## 데이터 수집 결과

| 카테고리 | 핵심 데이터 | 기준일 | 출처 | 사용 가능 여부 |
|---|---|---|---|---|
| 가격/거래 | 미국 ETF·개별주 장중 가격, 호가, 거래량 | 2026-07-07 11:16 ET | Nasdaq API | 사용 |
| 공시 | 삼성전자 2026년 2분기 가이던스 | 2026-07-07 | Samsung Global Newsroom | 사용 |
| 재무 | 삼성전자 매출 171조원, 영업이익 89.4조원 가이던스 | 2026-07-07 | Samsung Global Newsroom | 사용 |
| 수급 | ETF·개별주 동반 하락, 방어 섹터 상대강세 | 2026-07-07 11:16 ET | Nasdaq API | 조건부 사용 |
| 거시 | 미국 10년물 DGS10 4.49% | 2026-07-02, updated 2026-07-06 | FRED | 사용 |

## 실제 상품·호가 분석

- 호가 기준 시각: 2026-07-07 11:16 ET / 2026-07-08 00:16 KST.
- 호가 상태: real_time for Nasdaq quote fields, 단 실시간 VWAP와 Level 2 호가 잔량은 미확인.
- 상품 선정 기준: 보유 종목, 반도체 섹터 대표 ETF, 나스닥100 ETF, 방어 섹터 비교 ETF.
- 호가 미확인 시 결론 제한: ETF NAV/IOPV 괴리율과 VWAP 미확인으로 ETF 신규 매수 결론은 `보류`다.

| 용도 | 표시명 | 상품명 | 티커 | 거래소 | 통화 | 유형 | 현재가/최근 종가 | 매수호가 | 매도호가 | 스프레드% | 거래량 | 유동성 판정 | 실행 판정 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 보유 방어 | 퀄컴/QUALCOMM Incorporated (QCOM) | QUALCOMM Incorporated Common Stock | QCOM | NASDAQ-GS | USD | 보통주 | 180.30 | 180.23 | 180.41 | 0.10% | 4,120,421 | high | 신규 매수 보류, 보유 방어 |
| 보유 방어 | 엔비디아/NVIDIA Corporation (NVDA) | NVIDIA Corporation Common Stock | NVDA | NASDAQ-GS | USD | 보통주 | 193.00 | 193.00 | 193.03 | 0.02% | 42,251,207 | high | 신규 매수 보류, 194/196 회복 확인 |
| 섹터 기준 | VanEck Semiconductor ETF (SMH) | VanEck Semiconductor ETF | SMH | Nasdaq/ETF | USD | ETF | 572.09 | 571.84 | 572.08 | 0.04% | 5,971,648 | high | 600 회복 전 방어 |
| 섹터 기준 | iShares PHLX SOX Semiconductor Sector Index Fund (SOXX) | iShares PHLX SOX Semiconductor Sector Index Fund | SOXX | Nasdaq/ETF | USD | ETF | 540.3506 | 540.37 | 540.56 | 0.04% | 5,239,753 | high | 신규 매수 보류 |
| 지수 기준 | Invesco QQQ Trust, Series 1 (QQQ) | Invesco QQQ Trust, Series 1 | QQQ | Nasdaq/ETF | USD | ETF | 707.145 | 707.12 | 707.17 | 0.01% | 17,838,044 | high | 718 회복 전 위험 |
| 비교 방어 | State Street Health Care Select Sector SPDR ETF (XLV) | Health Care Select Sector SPDR Fund | XLV | NYSE Arca/ETF | USD | ETF | 164.79 | 164.78 | 164.81 | 0.02% | 4,694,580 | high | 반도체 대비 방어 우위 |
| 비교 방어 | State Street Consumer Staples Select Sector SPDR ETF (XLP) | Consumer Staples Select Sector SPDR Fund | XLP | NYSE Arca/ETF | USD | ETF | 85.365 | 85.37 | 85.38 | 0.01% | 5,334,196 | high | 반도체 대비 방어 우위 |

### ETF/ETN 상세

| 표시명 | 상품명 | 티커 | 기초지수/자산 | NAV/IOPV | 시장가격 | 괴리율 | 총보수 | 추적오차 | LP/시장조성 | 레버리지 배율 | 판정 |
|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---|
| VanEck Semiconductor ETF (SMH) | VanEck Semiconductor ETF | SMH | 반도체 주식 바스켓 | 미확인 | 572.09 | 미확인 | 미확인 | 미확인 | 호가 스프레드는 좁음 | 1x | ETF 신규 매수 보류 |
| iShares PHLX SOX Semiconductor Sector Index Fund (SOXX) | iShares PHLX SOX Semiconductor Sector Index Fund | SOXX | PHLX SOX 계열 반도체 지수 | 미확인 | 540.3506 | 미확인 | 미확인 | 미확인 | 호가 스프레드는 좁음 | 1x | ETF 신규 매수 보류 |
| Invesco QQQ Trust, Series 1 (QQQ) | Invesco QQQ Trust, Series 1 | QQQ | Nasdaq-100 | 미확인 | 707.145 | 미확인 | 미확인 | 미확인 | 호가 스프레드는 좁음 | 1x | 기준 지표로만 사용 |

### 상품별 주문 메모

| 표시명 | 주문 방식 | 진입 조건 | 지정가 기준 | 손절 기준 | 청산 기준 | 최대 비중 | 주문 금지 조건 |
|---|---|---|---|---|---|---:|---|
| 퀄컴/QUALCOMM Incorporated (QCOM) | 관찰 / 보유 방어 | 내일 10:30 ET 이후 184 회복, VanEck Semiconductor ETF (SMH) 580 회복, Invesco QQQ Trust, Series 1 (QQQ) 712 회복이 동시에 필요 | 추격 금지, 회복 후 되눌림 지정가만 | 179 이탈 또는 180 미회복 지속 시 단기 논리 훼손 | 184-186 회복 실패 시 단기 물량 축소 검토 | 단타 슬리브 0-3% 신규 한도 | 182.5 아래에서 물타기 금지 |
| 엔비디아/NVIDIA Corporation (NVDA) | 관찰 / 보유 방어 | 194 회복 후 196 안착, VanEck Semiconductor ETF (SMH) 580 회복 필요 | 194 위 추격보다 194 재지지 확인 | 191.15 이탈 또는 190 이탈 시 단기 논리 훼손 | 197.5-200 회복 실패 시 단기 물량 축소 검토 | 단타 슬리브 0-3% 신규 한도 | 194 아래 신규 단타 진입 금지 |
| VanEck Semiconductor ETF (SMH) | 기준 지표 | 580 회복은 단기 안도, 590 회복은 반등 품질 개선, 600 종가 회복은 리스크 재개 가능성 | ETF 자체 신규 매수는 NAV/IOPV 확인 전 보류 | 566 이탈 | 600 미회복 시 반도체 추격 금지 | 0% | NAV/IOPV 미확인 신규 ETF 매수 금지 |

## 미국 장중 시간대별 주문 전략

- 적용 여부: 예.
- 현재 시간: 2026-07-07 11:16 ET / 2026-07-08 00:16 KST.
- 서머타임/표준시간: EDT.
- 시장 구간: 점심시간 진입 직전, 1차 신뢰 구간 후반.
- 휴장·조기폐장 확인: Nasdaq 기준 2026-07-07은 정규 거래일. 2026-07-03은 Independence Day observed로 휴장, 현재일은 휴장 아님.
- 브로커 연장거래 가능 시간 확인: 브로커별 차이 미확인. Nasdaq 기준 프리마켓 04:00-09:30 ET, 애프터마켓 16:00-20:00 ET.
- 한국 거주자 피로 게이트: caution. KST 00:16으로 신규 판단 품질 저하 전환 구간에 접근 중.
- 기본 행동: 관찰 / 보유 방어 / 신규 추격 금지.
- 주문 방식 제한: 지정가 또는 관찰만. 시장가 신규 진입 금지.

| ET | KST | 구간 | 핵심 관찰값 | 주문 판단 | 금지 행동 |
|---|---|---|---|---|---|
| 04:00-09:30 | 17:00-22:30 | 프리마켓 | 아시아 반도체 종가, 삼성전자/Samsung Electronics (005930.KS), SK하이닉스/SK hynix Inc. (000660.KS), 대만반도체/Taiwan Semiconductor Manufacturing Company Limited (TSM) ADR, VanEck Semiconductor ETF (SMH) 프리마켓 | 시나리오 작성 | 프리마켓 급락 저점매수 |
| 09:30-09:45 | 22:30-22:45 | 오픈 15분 | 고가, 저가, 시초가, VWAP, 첫 거래대금 | 기록·관찰 | 신규 추격 |
| 09:45-10:30 | 22:45-23:30 | 방향성 검증 | 시초가 회복, VWAP 유지, 거래대금 지속성 | 약한 종목 제거 | 숏커버를 진짜 매수로 단정 |
| 10:30-11:30 | 23:30-00:30 | 1차 신뢰 구간 | 섹터 동조화, 상대강도, VWAP 위 유지 | 오늘은 신규보다 보유 방어 | 손절 없는 진입 |
| 11:30-13:30 | 00:30-02:30 | 점심시간 | 거래량 둔화, 저점 상승, 보유 품질 | 새 진입 최소화 | 얇은 거래 돌파 추격 |
| 13:30-14:30 | 02:30-03:30 | 오후 재평가 | 지수 반등 대비 상대강도 | 강한 종목만 유지 | 거래대금 없는 고점 돌파 추격 |
| 14:30-15:30 | 03:30-04:30 | 종가 전 정리 | 리밸런싱, 옵션/헤지 영향 | 보유·축소 판단 | 신규 진입 우선 |
| 15:30-16:00 | 04:30-05:00 | 클로징 옥션 | 종가 고가권, 윗꼬리, VWAP 이탈 | 종가 판정 | 계획 없는 신규 진입 |
| 16:00-20:00 | 05:00-09:00 | 애프터마켓 | 실적 후 반응, 얇은 호가 | 다음날 관찰 재료 | 확정 매매 근거 단독 사용 |

### 시간대 주문 결론

- 정보 -> 기대치 -> 포지션 -> 가격 반응 -> 수급 지속성: 강한 삼성전자 실적 정보가 기대치 과포화와 포지션 혼잡에 부딪혔고, 가격 반응이 약했으며, ETF·개별주 동반 하락으로 수급 지속성도 약하다.
- VWAP/시초가 기준: 실시간 VWAP 미확인. 대신 당일 고가 대비 밀린 가격과 주요 기준선 이탈로 약한 가격 반응을 판정한다.
- 거래대금/스프레드 기준: 유동성은 충분하고 스프레드는 좁다. 문제는 체결 가능성이 아니라 방향성 확률이다.
- 다음 확인 시간: 2026-07-08 08:30 ET 프리마켓, 10:30 ET 정규장 1차 신뢰 구간, 14:00 ET FOMC 의사록, 15:30 ET 종가 전.
- 다음날 관찰 조건: VanEck Semiconductor ETF (SMH) 580/590/600, Invesco QQQ Trust, Series 1 (QQQ) 712/718, 퀄컴/QUALCOMM Incorporated (QCOM) 184/186, 엔비디아/NVIDIA Corporation (NVDA) 194/196/200.

## 공격적 단기 매매 확률 게이트

- 적용 여부: 예.
- 최종 판정: `blocked`.
- 확률 점수: 54/100.
- 정렬 카운트: 2/7.
- 1회 손실 한도: 신규 단타는 보류. 보유분 방어 시 단타 슬리브 기준 0.25-0.50% 손실 한도.
- 최대 포지션 비중: 신규 0%, 기존 보유분은 사용자 평균단가와 총 포트폴리오 비중 확인 전 확대 금지.
- 다음 확인 시간: 2026-07-08 10:30 ET.

| 항목 | 점수(0-10) | 상태 | 근거 |
|---|---:|---|---|
| 기대치 갭 | 4 | under / crowded | 삼성전자 숫자는 좋았지만 기대치를 크게 넘지 못했고 주가는 매도 반응. |
| 가격 반응 품질 | 3 | weak | VanEck Semiconductor ETF (SMH), iShares PHLX SOX Semiconductor Sector Index Fund (SOXX), 퀄컴/QUALCOMM Incorporated (QCOM) 동반 약세. |
| 거래대금 확장 | 7 | expanding | 거래량은 충분하나 상승 흡수가 아니라 하락 거래로 해석. |
| 기관/외국인 정렬 | 4 | unknown_to_conflicting | 직접 수급 미확인. ETF 동반 하락은 기관·프로그램 매도 가능성. |
| 수급 지속성 | 4 | weak | 섹터 전반 하락 지속. |
| 환율 순풍 | 5 | unknown | USD/KRW·DXY 장중 확인 부족. |
| 섹터/지수 상대강도 | 2 | weak | 반도체가 Invesco QQQ Trust, Series 1 (QQQ)보다 훨씬 약함. |
| 유동성/스프레드 | 9 | high | 대형주와 ETF 모두 스프레드가 좁고 거래량 충분. |
| 손익비/무효화 | 6 | R:R conditional | 손절선은 명확하나 현재 위치가 지지선 붕괴 후라 신규 진입 손익비가 불리. |
| 심리 청결도 | 5 | crowded / loss_recovery | 급락 후 저점매수·본전심리 위험. |

### 공격적 단기 결론

- 진입 조건: 오늘은 없음. 내일 10:30-11:30 ET 이후 VanEck Semiconductor ETF (SMH) 580 회복, Invesco QQQ Trust, Series 1 (QQQ) 712 회복, 보유 종목별 회복선 돌파가 동시에 확인될 때만 `조건부 검토`.
- 손절 조건: 퀄컴/QUALCOMM Incorporated (QCOM) 179 이탈, 엔비디아/NVIDIA Corporation (NVDA) 191.15/190 이탈, VanEck Semiconductor ETF (SMH) 566 이탈.
- 1차/2차 청산 조건: 안도 반등이 나와도 VanEck Semiconductor ETF (SMH) 590/600 회복 실패, Invesco QQQ Trust, Series 1 (QQQ) 718 회복 실패 시 단기 물량 축소 검토.
- 무효화 조건: 퀄컴/QUALCOMM Incorporated (QCOM) 184-186 미회복, 엔비디아/NVIDIA Corporation (NVDA) 196-200 미회복, VanEck Semiconductor ETF (SMH) 600 종가 미회복.
- 수급·환율 충돌 여부: 수급은 가격 반응 기준 충돌, 환율은 확인 부족. 공격적 매수 불가.
- 중대 차단 조건: 실시간 VWAP·기관/외국인/프로그램 수급·환율 미확인, 호재 후 약한 가격 반응, 섹터 ETF 이탈.

## 단타 전략

- 실행 여부: 신규 실행 보류.
- 후보 종목: 보유 방어 관점의 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA)만 추적한다. 신규 반도체 확장 후보는 보류한다.
- 진입 조건:
  - 퀄컴/QUALCOMM Incorporated (QCOM): 184 회복 후 186 돌파 시도, VanEck Semiconductor ETF (SMH) 580 이상, Invesco QQQ Trust, Series 1 (QQQ) 712 이상.
  - 엔비디아/NVIDIA Corporation (NVDA): 194 회복 후 196 안착, VanEck Semiconductor ETF (SMH) 580 이상, Invesco QQQ Trust, Series 1 (QQQ) 712 이상.
  - 섹터 확인: VanEck Semiconductor ETF (SMH) 590 회복 전에는 반도체 신규 진입을 단타 슬리브 0-3%로 제한하고, 600 종가 회복 전에는 오버나이트 확대 금지.
- 손절 조건:
  - 퀄컴/QUALCOMM Incorporated (QCOM): 179 이탈 또는 180 미회복 지속.
  - 엔비디아/NVIDIA Corporation (NVDA): 191.15 이탈, 더 보수적으로는 190 이탈.
  - 섹터: VanEck Semiconductor ETF (SMH) 566 이탈, Invesco QQQ Trust, Series 1 (QQQ) 704.90 이탈.
- 청산 조건:
  - 안도 반등에서 퀄컴/QUALCOMM Incorporated (QCOM) 184-186 회복 실패 시 단기 보유분 축소 검토.
  - 안도 반등에서 엔비디아/NVIDIA Corporation (NVDA) 196-200 회복 실패 시 단기 보유분 축소 검토.
  - FOMC 의사록 전 14:00 ET 근처에는 수익·손실 여부와 무관하게 포지션 크기를 줄이는 것을 우선 검토.
- 단타 슬리브 비중: 신규 0%, 조건부 회복 시 0-3%, daily close 확인 후에도 최대 5% 이하.
- 1회 거래 손실 한도: 단타 슬리브의 0.25-0.50%.
- 금지 행동: 물타기, 프리마켓 추격, 09:30-09:45 ET 신규 추격, 15:30 이후 계획 없는 신규 진입, FOMC 의사록 직전 신규 확대.

## 내일 2026-07-08 미국장 실행 트리

| 시간 | 체크 조건 | 판단 |
|---|---|---|
| 04:00-09:30 ET 프리마켓 | 아시아 반도체 종가, 대만반도체/Taiwan Semiconductor Manufacturing Company Limited (TSM) ADR, VanEck Semiconductor ETF (SMH), Invesco QQQ Trust, Series 1 (QQQ) 프리마켓 | VanEck Semiconductor ETF (SMH) 572 아래 또는 Invesco QQQ Trust, Series 1 (QQQ) 707 아래면 신규 매수 금지 |
| 09:30-09:45 ET | 갭 방향, 첫 고가/저가, 오픈 거래대금 | 관찰만. 강한 갭상승도 추격 금지 |
| 09:45-10:30 ET | 시초가 회복, 전일 저점 방어, 반도체 ETF 동조화 | 약한 종목 제거. 퀄컴/QUALCOMM Incorporated (QCOM) 184, 엔비디아/NVIDIA Corporation (NVDA) 194 미회복이면 신규 금지 |
| 10:30-11:30 ET | 1차 신뢰 구간. VanEck Semiconductor ETF (SMH) 580/590, Invesco QQQ Trust, Series 1 (QQQ) 712/718 | 세 지표가 모두 회복되면 소액 조건부 단타. 하나라도 실패하면 보유 방어만 |
| 11:30-13:30 ET | 점심시간 거래량 둔화 | 신규 진입 최소화. 이미 진입한 포지션만 손절선 관리 |
| 14:00 ET | FOMC 의사록 | 의사록 전후 15-30분 신규 확대 금지. 금리·달러 반응 확인 |
| 14:30-15:30 ET | 오후 재평가 | 지수 반등 때 엔비디아/NVIDIA Corporation (NVDA)가 더 강하고 퀄컴/QUALCOMM Incorporated (QCOM)이 184 위면 유지 검토 |
| 15:30-16:00 ET | 종가 판정 | VanEck Semiconductor ETF (SMH) 600, Invesco QQQ Trust, Series 1 (QQQ) 718 종가 회복 실패 시 오버나이트 확대 금지 |

## 한 박자 늦는 원인 특정

1. `확인 후 진입` 전략의 구조적 지연: 안전한 확인을 기다리면 기관과 알고리즘이 선반영한 뒤에 들어가게 된다. 확인형 전략은 손실 회피에는 유리하지만, 급등 초입 포착에는 느리다.
2. 아시아 반도체 선행 신호 누락: 삼성전자/Samsung Electronics (005930.KS)와 SK hynix Inc. (000660.KS)가 먼저 흔들리면 미국 반도체도 프리마켓에서 이미 가격 조정을 시작한다. 기존 전략은 미국 정규장 중심이라 아시아 선행 반응을 최상위 중단 조건으로 쓰지 못했다.
3. `좋은 뉴스 = 좋은 매수` 오류: 오늘처럼 삼성전자 실적이 좋아도 주가가 밀리면 핵심은 실적이 아니라 기대치 과포화다. 기관은 숫자보다 다음 분기 기대, 포지션 혼잡, 가이던스 부족을 먼저 본다.
4. 장중 반등과 종가 회복을 같은 신호로 취급한 문제: 장중 반등은 숏커버일 수 있고, 종가 회복은 기관 수급 지속성 확인이다. 기존 전략은 장중 회복을 너무 빨리 유효 신호로 인정했다.
5. 반도체 상관 리스크 과소평가: 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA), 브로드컴/Broadcom Inc. (AVGO), 마이크론/Micron Technology (MU)은 사업이 달라도 ETF와 프로그램 매매에서는 한 바구니로 팔릴 수 있다.
6. 개인 심리의 후행성: 개인은 급등을 확인한 뒤 사고, 급락을 본 뒤 저점매수를 고민한다. 기관은 기대치와 포지션을 먼저 조정한다. 이 차이가 `항상 한 발 늦다`는 느낌으로 나타난다.
7. 무효화선의 실행 지연: 퀄컴/QUALCOMM Incorporated (QCOM) 182.5, 엔비디아/NVIDIA Corporation (NVDA) 194, Invesco QQQ Trust, Series 1 (QQQ) 718, VanEck Semiconductor ETF (SMH) 600 같은 기준선이 깨졌을 때 즉시 결론을 낮춰야 했다.

## 개선 방안

1. 아시아/프리마켓 반도체 게이트 신설:
   - 삼성전자/Samsung Electronics (005930.KS), SK하이닉스/SK hynix Inc. (000660.KS), 대만반도체/Taiwan Semiconductor Manufacturing Company Limited (TSM) ADR, ASML Holding N.V. (ASML), VanEck Semiconductor ETF (SMH), Invesco QQQ Trust, Series 1 (QQQ)를 프리마켓 전에 확인한다.
   - 아시아 대장주가 호재에도 -5% 이상이면 미국 반도체 신규 매수를 자동 보류한다.
2. `호재 매도 게이트` 신설:
   - 공식 실적이 좋은데 주가가 밀리면 호재 점수를 0점 처리하고, 기대치 과포화로 분류한다.
   - `좋은 숫자`보다 `좋은 숫자에 대한 가격 반응`을 우선한다.
3. 장중 회복과 종가 회복 분리:
   - 장중 580/590 회복은 단타 안도 반등.
   - VanEck Semiconductor ETF (SMH) 600 종가 회복과 Invesco QQQ Trust, Series 1 (QQQ) 718 종가 회복 전에는 오버나이트 확대 금지.
4. 무효화선 자동 실행:
   - 퀄컴/QUALCOMM Incorporated (QCOM) 182.5 이탈: 신규 매수 중단.
   - 엔비디아/NVIDIA Corporation (NVDA) 194 이탈: 신규 매수 중단.
   - VanEck Semiconductor ETF (SMH) 600 이탈: 반도체 전체 보수화.
   - Invesco QQQ Trust, Series 1 (QQQ) 718 이탈: 나스닥 성장주 보수화.
5. 후보 수 축소:
   - 같은 반도체 체인에서 3개 이상 동시에 들고 있으면 실제로는 같은 포지션을 여러 번 산 것이다.
   - 내일은 퀄컴/QUALCOMM Incorporated (QCOM)과 엔비디아/NVIDIA Corporation (NVDA)만 관리하고, 신규로 Advanced Micro Devices, Inc. (AMD), 마이크론/Micron Technology (MU), Lam Research Corporation (LRCX), Applied Materials, Inc. (AMAT)를 추가하지 않는다.
6. 이벤트 전 비중 축소 규칙:
   - FOMC 의사록, 주요 반도체 실적, CPI/PPI, 옵션만기 전에는 신규 확대를 하지 않는다.
   - 이벤트 전 수익 포지션은 일부 현금화, 손실 포지션은 손절선 재확인.
7. 알림 기준:
   - Invesco QQQ Trust, Series 1 (QQQ) 712/718.
   - VanEck Semiconductor ETF (SMH) 580/590/600.
   - 퀄컴/QUALCOMM Incorporated (QCOM) 179/184/186.
   - 엔비디아/NVIDIA Corporation (NVDA) 191.15/194/196/200.

## 확장 유니버스 섹터 스크리닝

- 적용 여부: 제한적 예.
- 유니버스 범위: 전체 시장 자동 스크리닝 아님. 보유 종목과 미국 반도체·나스닥 대형 유동성 후보 중심.
- 사용자 언급 종목: 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA).
- 보유 종목: 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA).
- 추가로 본 섹터: 반도체 ETF, 나스닥100, 헬스케어, 필수소비재.
- 데이터 기준일: 2026-07-07 11:16 ET.
- 한계: 전체 미국 상장 종목 자동 스크리닝이 아니다.

| 분류 | 섹터 | 대표 후보 표시명 | 티커 | OPM/대체 수익성 | 촉매 | 저평가/성장 판단 | 7일 가격 반응/거래대금 | 리스크 | 판정 |
|---|---|---|---|---|---|---|---|---|---|
| 보유 방어 | 통신·AI 엣지 반도체 | 퀄컴/QUALCOMM Incorporated (QCOM) | QCOM | 미확인 | AI PC/모바일, 자동차 반도체 | 저평가 여부 미검증 | 당일 -3.31%, 거래량 충분 | 182.5 이탈, 섹터 약세 | 보유 방어 |
| 보유 방어 | AI 가속기 | 엔비디아/NVIDIA Corporation (NVDA) | NVDA | 미확인 | AI 데이터센터 수요 | 성장 품질이나 진입가 과열 가능 | 당일 -1.30%, 거래량 충분 | 194 이탈, 기대치 과포화 | 보유 방어 |
| 제외/보류 | 메모리 | 마이크론/Micron Technology (MU) | MU | 미확인 | 메모리 가격 | 실적은 강할 수 있으나 호재 매도 국면 | 당일 -6.71%, 거래량 충분 | 삼성전자/Samsung Electronics (005930.KS) 호재 매도 직격 | 제외/보류 |
| 제외/보류 | 반도체 장비 | Lam Research Corporation (LRCX) | LRCX | 미확인 | HBM/메모리 투자 | 사이클 민감 | 당일 -8.59%, 거래량 충분 | 섹터 ETF보다 더 약함 | 제외/보류 |
| 제외/보류 | 반도체 장비 | Applied Materials, Inc. (AMAT) | AMAT | 미확인 | 장비 투자 | 사이클 민감 | 당일 -9.94%, 거래량 충분 | 섹터 ETF보다 더 약함 | 제외/보류 |
| 비교 방어 | 헬스케어 | State Street Health Care Select Sector SPDR ETF (XLV) | XLV | ETF | 방어 로테이션 | 반도체 대체 피난처 | 당일 +1.75% | 성장주 반등 시 상대 열위 | 관찰 |

### 확장 후보 결론

- 좋은 산업이지만 좋은 진입가가 아닌 후보: 엔비디아/NVIDIA Corporation (NVDA)는 장기 성장성이 좋아도 194/196 회복 전 단기 진입가는 좋지 않다.
- 좋은 기업이지만 저평가가 아닌 후보: 엔비디아/NVIDIA Corporation (NVDA), 브로드컴/Broadcom Inc. (AVGO)는 성장 품질은 높지만 기대치와 밸류에이션 허들이 높다.
- 위험 신호 4개 이상으로 랭킹 제외한 후보: 이번 리포트에서는 재무 전수 검증을 하지 않아 저평가 우량주 랭킹 자체를 만들지 않는다.
- 싸 보이지만 가치함정 가능성이 큰 후보: 당일 급락한 장비·메모리주는 싸 보일 수 있으나 호재 매도 국면이라 신규 저점매수는 보류한다.
- 사용자 언급 종목 외 새로 편입된 관찰 후보: 방어 비교용 State Street Health Care Select Sector SPDR ETF (XLV), State Street Consumer Staples Select Sector SPDR ETF (XLP).
- 제외 후보와 이유: 마이크론/Micron Technology (MU), Sandisk Corporation (SNDK), Lam Research Corporation (LRCX), Applied Materials, Inc. (AMAT)는 당일 하락률이 과도하고 섹터 ETF 회복 전 단타 손익비가 낮아 신규 제외.

## 저평가 우량주/GARP 스크리닝

- 적용 여부: 아니오. 이번 요청은 보유 중인 미국 반도체 급락 원인과 내일 단기 전략이 핵심이며, 재무제표·컨센서스 기반 저평가 우량주 랭킹은 별도 작업이 필요하다.
- 스크리닝 기준일: 해당 없음.
- 시장/섹터 범위: 해당 없음.
- 주도 섹터 가설: 반도체는 장기 주도 섹터일 수 있으나, 단기 가격 반응은 주도 섹터가 아니라 위험 축소 국면이다.
- 최신 검증 근거: 상대강도와 거래대금은 확인. 이익 추정치 변화와 기관·외국인 순매수는 미확인.
- 결론 제한 사유: 저평가 판정을 위한 성장성, ROE/ROIC, 현금흐름, 부채, PEG, 촉매, 주주환원 데이터를 후보별로 검증하지 않았다.

| 후보 표시명 | 티커 | 거래소 | 성장성 | OPM/금융 대체 지표 | ROE/ROIC | 부채/현금흐름 | 촉매/환원/수급 | PEG/대체 밸류에이션 | 위험 신호 수 | 예외 후보 | 랭킹 자격 | 점수 | 가치함정 플래그 | 판정 |
|---|---|---|---|---|---|---|---|---|---:|---|---|---:|---|---|
| 퀄컴/QUALCOMM Incorporated (QCOM) | QCOM | NASDAQ-GS | 미검증 | 미검증 | 미검증 | 미검증 | 단기 수급 약함 | 미검증 | 미산정 | no | watch | 미산정 | medium | 추가 검증 |
| 엔비디아/NVIDIA Corporation (NVDA) | NVDA | NASDAQ-GS | 강할 가능성 | 미검증 | 미검증 | 미검증 | 단기 수급 혼재 | 미검증 | 미산정 | no | watch | 미산정 | medium | 추가 검증 |

### 가치함정 차단

- 저PER/저PBR 단독 통과 여부: 없음.
- `PBR = ROE x PER` 분해: 이번 리포트 범위 밖.
- 성장률 출처와 기간: 이번 리포트 범위 밖.
- 위험 신호 카운트: 재무 데이터 미검증으로 산정하지 않음.
- 판정 기준 적용: 저평가 우량주 랭킹 미작성.
- 영업현금흐름 품질: 미검증.
- 부채/희석 위험: 미검증.
- 리레이팅 촉매 2개 이상: 미검증.

## 레버리지/3배 단타 게이트

- 사용 여부: 아니오.
- 상품 유형: 해당 없음.
- 배율: 해당 없음.
- 기초자산: 해당 없음.
- 일일 리셋 이해 여부: 해당 없음.
- 괴리율/NAV 또는 지표가치 확인: 해당 없음.
- 유동성/스프레드 확인: 해당 없음.
- 오버나이트 허용 여부: 해당 없음.
- 최대 보유 시간: 해당 없음.
- 1회 손실 한도: 해당 없음.
- 하루 손실 한도: 해당 없음.
- 최종 판정: `blocked` for leverage. 레버리지 신규 전략 없음.

| 항목 | 점수(0-10) | 최소 | 근거 |
|---|---:|---:|---|
| 상품 이해 | 0 | 9 | 레버리지 요청 아님 |
| 기초자산 방향 | 0 | 8 | 반도체 방향 약세 |
| 변동성 환경 | 0 | 8 | 고변동성 |
| 유동성 | 0 | 9 | 레버리지 상품 미확인 |
| 심리 상태 | 0 | 9 | 손실 복구 심리 위험 |
| 진입 위치 | 0 | 8 | 지지선 이탈 |
| 손절 계획 | 0 | 10 | 해당 없음 |
| 손실 한도 | 0 | 10 | 해당 없음 |
| 보유 시간 | 0 | 9 | 해당 없음 |
| 검증 기록 | 0 | 9 | 레버리지 미사용 |

- 중대 차단 조건: 반도체 방향 약세, 변동성 확대, 상품별 NAV/괴리율 미확인.
- 보완 조건: 레버리지 상품을 쓰지 않는다.

## 가치투자 전략

- 실행 여부: 신규 실행 보류.
- 후보 종목: 퀄컴/QUALCOMM Incorporated (QCOM), 엔비디아/NVIDIA Corporation (NVDA)는 장기 검토 후보일 수 있으나 이번 리포트에서는 장기 매수 결론을 내리지 않는다.
- 투자 논리: 장기 AI·반도체 성장 논리는 존재하지만 오늘 하락은 좋은 산업과 좋은 진입가가 다르다는 점을 보여준다.
- 밸류에이션 근거: 미검증.
- 분할 매수 조건: 최소 VanEck Semiconductor ETF (SMH) 600 종가 회복, Invesco QQQ Trust, Series 1 (QQQ) 718 종가 회복, 개별 종목 회복선 회복 후 별도 재검증.
- 목표 비중: 사용자 총자산·위험한도 미제공으로 확정 불가.
- 논리 훼손 조건: AI 수요 둔화, 주요 고객 자체 칩 전환 가속, 마진 하락, 실적 가이던스 하향, 반도체 ETF 중기 추세 훼손.
- 실적 발표 후 확인 항목: 매출 성장률, 데이터센터/모바일/자동차 부문, 총마진, 재고, CAPEX, 고객 집중, 가이던스.

## 포트폴리오 운영안

| 슬리브 | 비중 | 역할 | 검토 주기 | 리스크 |
|---|---:|---|---|---|
| 현금/대기 | 70-100% | 변동성 방어, 내일 확인 후 대응 | 장중 2-4회 | 반등 놓침 |
| 단타 | 0-3% | 회복 확인 시 소액 실험 | 10:30 ET, 14:00 ET, 15:30 ET | 손실 복구 심리 |
| 가치투자 코어 | 신규 0% | 장기 후보 재평가 | 실적 발표 후 | 밸류에이션 과열 |
| 가치투자 위성 | 신규 0% | 반도체 외 방어 섹터 관찰 | 주간 | 반도체 급반등 시 상대 열위 |

## 실행 리스크

- 시장 리스크: 반도체 ETF 급락, 나스닥100 하락, FOMC 의사록 전후 금리 변동성.
- 종목 리스크: 퀄컴/QUALCOMM Incorporated (QCOM)는 182.5 이탈로 단기 반등 논리 훼손, 엔비디아/NVIDIA Corporation (NVDA)는 194 회복 전까지 단기 강세 판정 불가.
- 유동성 리스크: 대형주는 스프레드가 좁아 체결 리스크는 낮으나, 급락장에서 시장가 주문은 슬리피지 위험이 커진다.
- 세금/수수료: 미국 주식 양도소득세, 환전 스프레드, 매매 수수료는 사용자 계좌별 확인 필요.
- 법률/규제 확인: 미공개정보 사용 없음. 공개 자료와 장중 가격 반응만 사용.
- 중단 조건:
  - VanEck Semiconductor ETF (SMH) 566 이탈.
  - Invesco QQQ Trust, Series 1 (QQQ) 704.90 이탈.
  - 퀄컴/QUALCOMM Incorporated (QCOM) 179 이탈.
  - 엔비디아/NVIDIA Corporation (NVDA) 190 이탈.
  - 2026-07-08 FOMC 의사록 후 금리 상승과 나스닥 약세가 동시 발생.

## 성과 검토 계획

- 단타 검토: 2026-07-08 10:30 ET, 14:00 ET, 15:30 ET.
- 가치투자 검토: 퀄컴/QUALCOMM Incorporated (QCOM)과 엔비디아/NVIDIA Corporation (NVDA)의 다음 실적 발표 및 가이던스 후.
- 포트폴리오 검토: 반도체 전체 비중이 총 주식 예산의 20%를 넘는지 확인. 넘으면 상관 리스크 과다로 분류.
- 성공 기준:
  - 무효화선 이탈 시 신규 매수를 하지 않는다.
  - 반등이 와도 VanEck Semiconductor ETF (SMH) 600과 Invesco QQQ Trust, Series 1 (QQQ) 718 회복 전에는 오버나이트 확대하지 않는다.
  - 손실 복구 심리로 물타기하지 않는다.
- 실패 기준:
  - 182.5 아래 퀄컴/QUALCOMM Incorporated (QCOM)를 물타기.
  - 194 아래 엔비디아/NVIDIA Corporation (NVDA)를 단타 신규 매수.
  - 09:30-09:45 ET 또는 15:30-16:00 ET에 계획 없이 신규 진입.
- 수정 규칙:
  - 오늘 같은 호재 매도 사례가 나오면 섹터 전체를 즉시 방어로 낮춘다.
  - 다음 전략부터는 아시아 반도체 선행 반응을 미국장 전략의 최상위 게이트로 둔다.
  - 장중 회복과 종가 회복을 분리해 스윙/오버나이트 판단을 종가 기준으로 늦춘다.

## Verify 평점 계약

- 최종 판정: 조건부 통과. 행동 결론은 `보류`.
- 전체 가중 점수: 91/100.
- 중대 차단 조건: 있음. 공격적 단기 신규 진입에는 VWAP, 기관·외국인·프로그램 수급, 환율 확인 부족과 섹터 ETF 약세가 중대 차단 조건이다.
- 반복 검증 회차: 2회.

| 카테고리 | 1차 점수 | 2차 점수 | 최종 점수 | 통과 기준 | 판정 |
|---|---:|---:|---:|---:|---|
| 입력 적합성 | 78 | 84 | 84 | 80 | 통과 |
| 데이터 신뢰도 | 88 | 92 | 92 | 90 | 통과 |
| 상품·호가 실행 상세 | 87 | 91 | 91 | 90 | 통과 |
| 투자자 심리 해석 | 88 | 92 | 92 | 90 | 통과 |
| 전망 근거 검색·발췌·분석 적합성 | 86 | 92 | 92 | 92 | 통과 |
| 저평가 우량주 스크리닝 적합성 | 70 | 90 | 90 | 90 | 범위 제한 통과 |
| 공격적 단기 매매 적합성 | 82 | 93 | 93 | 92 | 통과, 단 결론 blocked |
| 미국 장중 시간대 주문 적합성 | 88 | 93 | 93 | 90 | 통과 |
| 레버리지 상품 적합성 | 95 | 95 | 95 | 95 | 해당 없음, blocked |
| 분석 논리 | 86 | 91 | 91 | 80 | 통과 |
| 전략 완성도 | 84 | 90 | 90 | 85 | 통과 |
| 리스크 통제 | 88 | 94 | 94 | 90 | 통과 |
| 실행 가능성 | 82 | 89 | 89 | 80 | 통과 |
| 성과 검토성 | 84 | 90 | 90 | 85 | 통과 |
| 표현 안전성 | 90 | 95 | 95 | 90 | 통과 |

## 반복 검증 기록

- 1차 Verify 결과: 공격적 단기 매매와 내일 주문 전략에 필요한 호가, 시간대, 기준선은 있었으나 ETF NAV/IOPV와 VWAP, 기관·외국인 수급 직접 데이터가 부족했다.
- 1차 수정 내역: 신규 진입 결론을 `조건부 검토`가 아니라 `보류/blocked`로 낮추고, 내일 확인 조건을 시간대별로 분리했다.
- 2차 Verify 결과: 오케스트레이터의 표시명 규칙, 미국장 시간대 게이트, 심리 게이트, 공격적 단기 매매 게이트, 출처·기준일 표기를 충족했다.
- 2차 수정 내역: `한 박자 늦는 원인`을 구조적 지연, 아시아 선행 신호 누락, 호재 매도 게이트 부재, 종가 확인 부재로 특정했다.
- 3차 Verify 결과: 수행하지 않음.
- 남은 약점: 실시간 VWAP, 기관·외국인·프로그램 수급, ETF NAV/IOPV, 사용자 평균단가·보유비중·최대 손실 한도가 없다.

## 출처

- samsung_q2_2026_guidance: Samsung Global Newsroom, "Samsung Electronics Announces Earnings Guidance for Second Quarter 2026", published_at 2026-07-07, data_as_of 2026 Q2 guidance, source_checked_at 2026-07-08 KST, URL: https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-second-quarter-2026
- ibd_chip_fall: Investors Business Daily, "Micron, Chip Stocks Fall Despite Samsung Profit Surge", published_at 2026-07-07, source_checked_at 2026-07-08 KST, URL: https://www.investors.com/news/technology/chip-stocks-fall-despite-samsung-profit-surge/
- marketwatch_chip_selloff: MarketWatch, "Bounce in chip stocks is wiped out by another big, broad selloff", published_at 2026-07-07, source_checked_at 2026-07-08 KST, URL: https://www.marketwatch.com/livecoverage/stock-market-today-dow-53000-first-time-s-p-500-nasdaq-tech-stocks/card/bounce-in-chip-stocks-is-wiped-out-by-a-another-big-broad-selloff-FJZHE7IGBxpaZ56csJ9u
- nasdaq_quotes_2026_07_07_1116: Nasdaq API quote fields, data_as_of 2026-07-07 11:16 ET, source_checked_at 2026-07-08 00:16 KST, URL examples: https://api.nasdaq.com/api/quote/QCOM/info?assetclass=stocks, https://api.nasdaq.com/api/quote/NVDA/info?assetclass=stocks
- nasdaq_hours: Nasdaq U.S. Stock Market Holiday Schedule and Trading Hours, source_checked_at 2026-07-08 KST, URL: https://www.nasdaq.com/market-activity/stock-market-holiday-schedule
- fed_fomc_calendar: Federal Reserve FOMC calendars, source_checked_at 2026-07-08 KST, URL: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- fred_dgs10: FRED DGS10, 2026-07-02 4.49%, updated 2026-07-06, source_checked_at 2026-07-08 KST, URL: https://fred.stlouisfed.org/series/DGS10

## 검증 체크리스트

- [x] 당일 가격/시장 데이터 또는 최신성 한계 표시
- [x] 실제 상품명, 티커, 거래소, 통화, 상품 유형 포함
- [x] 요약, 근거 카드, 후보 설명의 종목·ETF·ETN·ADR은 한글명/공식 풀네임 (티커) 형식으로 표시
- [x] 호가, 스프레드, 거래대금, 기준 시각 포함
- [x] ETF/ETN 후보의 NAV/IOPV, 괴리율, 총보수, 시장조성 상태 한계 표시
- [x] 호가 미확인 또는 지연 데이터일 때 신규 주문 결론 제한
- [x] 차주/미래 전망 요청이면 신뢰 출처 검색, 근거 카드 발췌, 시나리오 합성 포함
- [x] 전망 근거의 source_id, published_at, data_as_of, source_checked_at 포함
- [x] 세계정세, 경제상황, 유동성/환율, 원자재, 투자자 심리, 이벤트 캘린더 검색 커버리지 포함
- [x] 기본/강세/약세 시나리오와 확인 트리거, 무효화 조건 포함
- [x] 개인·외국인·기관·프로그램 심리 예측 분리
- [x] 투자자 심리 해석 게이트 포함
- [x] 정보, 기대치, 포지션, 가격 반응, 수급 지속성 5단계 해석
- [x] 공격적 단기 매매 요청이면 확률 게이트 포함
- [x] 공격적 단기 매매의 기대치, 가격 반응, 거래대금, 기관/외국인/프로그램 수급, 환율, 상대강도, 손익비 점수화
- [x] 기관/외국인 수급과 환율이 단기 방향성과 충돌하면 watch_only 또는 blocked 판정
- [x] 공격적 단기 매매의 손절, 손익비, 1회 손실 한도, 포지션 상한 포함
- [x] 저평가/성장형/미래형 요청 범위가 아니므로 범위 제한 명시
- [x] 사용자 언급 종목 외 대체 후보와 제외 후보 포함
- [x] 좋은 산업, 좋은 기업, 좋은 진입가를 분리
- [x] 저평가 우량주/GARP 후보의 재무 스크리닝 미수행 한계 명시
- [x] 미국장 전략이면 ET/KST 시간대, 서머타임, 휴장·조기폐장, 브로커 연장거래 가능 시간 확인
- [x] 미국 프리마켓/애프터마켓 주문은 호가, 스프레드, 거래대금, 지정가 제한 포함
- [x] 한국 시간 00:30 이후 피로 게이트와 실시간 대응 가능성 확인
- [x] 레버리지 사용 시 레버리지/3배 단타 게이트 포함
- [x] 레버리지 사용 시 신규 전략 blocked 판정
- [x] 단타와 가치투자 자금 분리
- [x] 진입, 손절, 청산, 논리 훼손 조건 포함
- [x] 실제 금액 부재 시 비중으로만 제시
- [x] 세금, 수수료, 유동성, 공시 리스크 포함
- [x] 성공/실패 검토 기준 포함
- [x] Verify 평점 계약 최소 2회 수행
- [x] 전체 가중 점수 88점 이상 또는 보류/중단 판정
- [x] 기준 미달 항목 수정 내역 기록
