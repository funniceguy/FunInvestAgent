# 스킬: 잠재 매수·매도 물량과 오버행 게이트

## 목적

화면에 쌓인 호가 잔량, 실제 체결 수급, 가격대별 잠재 매물, 경매 불균형, 공시로 예정된 공급을 분리해 매수 흡수력과 매도 오버행을 판정한다. 호가 한 장을 기관 의도나 미래 방향으로 오해하지 않고, 반복 관찰과 실제 체결·가격 반응이 일치할 때만 예측 신호로 사용한다.

상세 시장 자료의 의미와 공식 출처는 `funmemory/domains/stock_market_microstructure_playbook.md`를 따른다.

## 적용 조건

- 신규 진입, 비중 확대, 단타, 급등주, 순환주, 돌파, 눌림, 반등 전략.
- 사용자가 쌓인 매수 물량, 쏟아질 매도 물량, 매물대, 호가벽, 기관 매집·분산을 요청한 경우.
- 오픈·클로징 옥션, 지수 리밸런싱, 대규모 공시 공급, 보호예수 해제, ATM·유상증자·전환증권, 옵션 만기가 관련된 경우.
- `stock_mechanical_flow_risk_gate_skill.md`와 `stock_product_quote_depth_skill.md`를 통과한 뒤 최종 주문 방향을 정하기 전.

## 관측 계층

| 계층 | 확인 데이터 | 해석 제한 |
|---|---|---|
| 표시 호가 | 복수 가격 레벨의 매수·매도 잔량, 스프레드, 잔량 변화 | 취소·수정·허수 주문과 숨은 주문을 포함하지 못함 |
| 실제 체결 | 매수·매도 주도 체결량, 체결 강도, 대량 체결, 잔량 소진·재충전 | 거래소·벤더의 체결 방향 추정 방식 기록 필요 |
| 가격 반응 | VWAP, anchored VWAP, 고가·저가, 돌파 후 유지, 흡수·거부 | 가격만으로 주체 신원 단정 금지 |
| 경매 | Nasdaq NOII, NYSE auction imbalance, KRX 단일가·종가 수급 가능 시 | 특정 시각의 경매 유동성으로 연속장 전체를 예측하지 않음 |
| 잠재 공급 | 거래량 프로파일, 갭·고점 매물대, 보호예수, 증자·ATM·CB/BW·워런트, 내부자 공시, ETF 리밸런싱 | 발행 가능 물량과 실제 매도 물량을 구분 |
| 비표시 유동성 | reserve/iceberg 의심, off-exchange·dark 거래, 내부화 | 공개 호가만으로 총수요·총공급을 완전 측정할 수 없음 |

## 시장별 필수 구분

### 한국

- KRX 정규장과 NXT 선행가격을 분리한다.
- 외국인·기관·금융투자·투신·연기금·프로그램·KOSPI200 선물을 가능한 범위에서 분해한다.
- VI, 사이드카, 시장경보, 투자주의·경고·위험, 공매도·대차, 단일가, 지수·ETF 리밸런싱을 확인한다.
- 유상증자, 전환사채·신주인수권부사채, 보호예수 해제, 자사주 처분, 블록딜 가능 공시를 잠재 공급 캘린더에 넣는다.

### 미국

- 단일 브로커의 Level 2는 전체 시장 호가가 아니다. NBBO, 거래소 depth, off-exchange 비중, 데이터 커버리지를 기록한다.
- Nasdaq/NYSE 오픈·클로징 경매 불균형은 해당 경매 신호로만 사용한다.
- FINRA short interest는 월 2회 스냅샷이며 일일 short sale volume과 동일하지 않다.
- SEC Form 13F는 분기 말 보유를 최대 45일 뒤 보여줄 수 있어 장중 기관 매수 신호로 쓰지 않는다.
- SEC Form 4, 등록서류, ATM·secondary offering, convertibles·warrants, lock-up 해제 가능성을 잠재 공급으로 확인한다.
- 옵션 open interest·put/call·만기 자료는 포지션 방향과 딜러 헤지 부호를 독립 확인하지 못하면 단독 방향 신호로 쓰지 않는다.

## 계산과 확인

- 가중 호가 불균형: `weighted_OBI = (sum(w_i * bid_size_i) - sum(w_i * ask_size_i)) / (sum(w_i * bid_size_i) + sum(w_i * ask_size_i))`.
- 체결 불균형: `executed_imbalance = (aggressive_buy_volume - aggressive_sell_volume) / total_classified_volume`.
- 잔량 지속성: 같은 가격대 잔량이 여러 스냅샷에서 유지·재충전되고 실제 체결을 견딘 비율.
- 흡수: 매도 주도 체결이 이어져도 저가가 내려가지 않으면 매수 흡수 후보, 매수 주도 체결에도 고가가 오르지 않으면 매도 흡수 후보.
- 매물대: 최근 촉매일, 갭 시작점, 대량 거래 고점, 실적 발표일에 anchored VWAP과 volume-at-price를 함께 본다.
- 모든 값에 데이터 기준 시각, 세션, 거래소/벤더 커버리지, 지연 여부를 붙인다.

## 예측 사격 허용 규칙

다음 4개 축 중 3개 이상이 같은 방향이고 중대 차단 조건이 없어야 `flow_confirmed`다.

1. 표시 잔량이 최소 3회 스냅샷과 2개 시간 창에서 지속된다.
2. 실제 매수·매도 주도 체결과 잔량 소진·재충전이 같은 방향이다.
3. 가격이 VWAP/anchored VWAP, 돌파선, 상대강도로 같은 방향을 확인한다.
4. 경매 불균형 또는 공시·리밸런싱·잠재 공급 캘린더가 같은 방향을 지지한다.

한 축만 있으면 `unconfirmed`, 두 축이면 `watch`, 세 축이면 `confirmed`, 네 축이면 `strong_confirmed`로 기록한다. `strong_confirmed`도 수익을 보장하지 않는다.

## 상태 판정

| 상태 | 의미 | 기본 행동 |
|---|---|---|
| demand_absorption | 매도 체결을 받아내며 저점·VWAP 유지 | 제한 진입 후보, 다음 창 재확인 |
| balanced | 호가·체결·가격이 혼조 | 관찰, 추격 금지 |
| supply_overhang | 반복 매도 잔량·매도 체결·가격 거부가 일치 | 신규 진입 금지 또는 비중 축소 |
| hidden_supply_suspected | 표시 잔량은 얇지만 반복 체결에도 고가가 막힘 | 숨은 공급 확인 전 관찰 |
| liquidity_vacuum | 얇은 호가와 큰 가격 점프, 체결 비용 급증 | 시장가 금지, 전략 차단 |
| event_supply_risk | 증자·ATM·전환증권·보호예수·리밸런싱 공급 가능 | 희석·수량·일정 확인 전 차단 |
| unknown | 커버리지·시각·체결 분류 부족 | 공격 매매 금지 |

## 강제 보수화

- 호가 스냅샷만 우호적이면 주방향 확률 가산은 0이다.
- 잔량이 체결 직전 반복 취소되거나 반대편으로 이동하면 `spoofing_or_ephemeral_risk`로 표시하고 호가 신호를 폐기한다. 조작 주체는 단정하지 않는다.
- 미국 호가의 venue coverage가 불명확하거나 한국의 실시간 호가·체결이 없으면 `unknown`이다.
- sell overhang 또는 hidden supply가 확인되면 공격적 단기 매매는 `watch_only` 이하, 신규 돌파 매수는 금지한다.
- demand absorption은 가격 상승 보장이 아니다. 다음 시간 창에서 고점 상승과 VWAP 유지가 없으면 balanced로 되돌린다.
- 잠재 발행 물량의 정확한 수량·행사가·락업 해제일을 확인하지 못하면 희석 위험 종목의 공격 매매를 금지한다.

## 출력

- `supply_overhang_order_flow_packet`
- 시장·세션·데이터 커버리지와 기준 시각.
- 복수 레벨 호가, weighted OBI, 체결 불균형, 잔량 지속성.
- 매수 흡수·매도 흡수·숨은 공급·유동성 공백 판정.
- 가격대별 overhead supply와 anchored VWAP 지도.
- 공시·락업·증자·전환증권·내부자·ETF/지수·옵션 만기 공급 캘린더.
- 예측 사격 확인 축 수와 다음 확인 시각.
- 최종 판정: `flow_clear`, `flow_caution`, `flow_watch_only`, `flow_blocked`, `unknown`.
- 예측 확률·비중·주문 방식에 적용할 상한과 금지 조건.

## 중대 차단 조건

- 한 번 본 매수·매도 잔량으로 기관 매집·분산 또는 다음 가격 방향을 단정한다.
- 표시 호가와 실제 체결 방향, 가격 반응을 교차확인하지 않는다.
- 미국 단일 venue/브로커 depth를 전체 시장 수급으로 표현한다.
- short interest와 일일 short sale volume, 13F와 실시간 기관 매수를 혼동한다.
- 옵션 open interest만으로 딜러 감마 방향이나 다음날 가격 방향을 단정한다.
- 증자·ATM·전환증권·워런트·보호예수·블록딜 가능 공급을 확인하지 않고 급등주를 추격한다.
- `supply_overhang`, `liquidity_vacuum`, `event_supply_risk`, `unknown`인데 공격적 신규 진입을 제시한다.
