# 스킬: 차주/미래 전망 근거 발췌

## 목적

검색된 출처에서 전략 전망에 필요한 사실, 수치, 일정, 시장 반응, 투자자 심리 신호를 발췌해 `근거 카드`로 만든다. 이 스킬은 정보 요약이 아니라, 예측에 쓸 수 있는 검증 가능한 근거만 구조화한다.

## 적용 조건

- `stock_forward_source_search_skill.md`로 신뢰 출처를 확보한 뒤.
- 세계정세, 경제상황, 기관·외국인·개인 심리, 환율, 수급을 전략 근거로 쓰려는 경우.
- 첨부 자료, 뉴스, 리서치, 보고서를 전망 근거로 변환해야 하는 경우.

## 발췌 원칙

- 사실, 수치, 일정, 발언, 전망, 의견을 분리한다.
- 직접 인용은 짧게만 쓰고, 대부분은 요약한다.
- 출처 원문에 없는 투자 결론을 발췌 카드에 섞지 않는다.
- 같은 주장을 2개 이상 출처가 뒷받침하면 교차확인 표시를 붙인다.
- 단일 뉴스, 단일 리포트, 단일 심리 지표만으로 시장 전망을 확정하지 않는다.

## 근거 카드 필드

| 필드 | 설명 |
|---|---|
| evidence_id | 고유 ID |
| source_id | source_registry 또는 임시 출처 ID |
| source_tier | primary / market_data / trusted_secondary / weak |
| published_at | 발행 시각 |
| data_as_of | 데이터 기준일 |
| extracted_at | 발췌 시각 |
| fact_type | data / schedule / policy / geopolitical / flow / sentiment / earnings / distribution / nav / option_structure / fee_tax / drawdown / liquidity / structural_impairment / opinion |
| extracted_fact | 원문 근거를 요약한 사실 |
| numeric_value | 수치가 있으면 단위와 함께 기록 |
| one_day_change | 예측에 쓰는 데이터이면 1일 변화 |
| three_day_change | 예측에 쓰는 데이터이면 3일 변화 |
| five_day_cumulative | 예측에 쓰는 데이터이면 5일 누적 또는 주간 변화 |
| market_channel | rates / fx / liquidity / earnings / risk_appetite / supply_chain / flows |
| affected_assets | 지수, 섹터, 종목, 원자재, 통화 |
| affected_asset_display_names | 종목·ETF·ETN·ADR은 `한글명/공식 풀네임 (티커)` 형식으로 기록 |
| direction_hint | risk_on / risk_off / mixed / neutral / unknown |
| confidence | high / medium / low |
| contradiction | 충돌하는 근거 또는 반대 시나리오 |

## 발췌 절차

1. 출처별 핵심 수치, 일정, 발표 문장, 시장 반응을 추출한다.
2. 각 근거를 `시장 전달 경로`로 번역한다.
3. 투자자 심리는 개인, 외국인, 기관, 프로그램, 선물/옵션 포지션으로 나눠 기록한다.
4. 환율과 외국인 수급은 한국 주식, ADR, 수출입 섹터에 미치는 방향을 별도 기록한다.
5. 세계정세는 공급망, 원자재, 제재, 리스크 프리미엄, 특정 섹터 수혜/피해로 연결한다.
6. 내일/주간 예측에 쓰는 데이터는 최신값만 발췌하지 말고 1일 변화, 3일 변화, 5일 누적 또는 해당 값을 구할 수 없는 사유를 기록한다.
7. 근거 카드의 영향 자산이 종목·ETF·ETN·ADR이면 티커만 쓰지 말고 `한글명/공식 풀네임 (티커)` 표시명을 붙인다.
8. 각 카드에 신뢰도와 반대 근거를 붙인다.
9. 장기 기업 카드는 trailing/forward/normalized 기준, EPS·FCF 조정, ROE/ROIC, 희석, 배당·순자사주를 분리한다.
10. 커버드콜·인컴 카드는 분배율, SEC yield, 분배 재원·원금환급, 주당 NAV, 분배 재투자 총수익, 옵션 구조를 서로 다른 필드로 발췌한다.
11. 운용사 마케팅 페이지의 분배율은 투자설명서·주주 보고서·19a notice 또는 국내 동등 공시와 교차확인한다.
12. 자본보전 카드는 낙폭, 갭·슬리피지, 유동성, 상관, 회복 재원, 구조적 훼손을 분리하고 보장 표현을 근거로 채택하지 않는다.

## 중대 누락

- source_id, published_at, data_as_of 중 하나라도 없는 카드.
- 사실과 의견을 구분하지 않은 카드.
- 숫자 단위나 기준 기간이 없는 경제지표 카드.
- 내일/주간 예측 핵심 수치인데 최신값, 기준 기간, 변화값 또는 변화값 누락 사유가 없는 카드.
- 세계정세를 섹터/가격 전달 경로 없이 단순 위험 문구로만 기록한 카드.
- 수급과 투자심리를 개인·외국인·기관으로 분리하지 않은 카드.
- 영향 자산에 티커만 있고 한글명 또는 공식 풀네임이 없는 카드.
- 분배율을 총수익 또는 SEC yield로 바꾸어 적은 카드.
- 커버드콜 상품인데 분배 재원, NAV, 옵션 구조, 동일 기초자산 총수익 중 하나라도 누락 사유 없이 빠진 카드.

## 출력

- 근거 카드 목록.
- 출처별 발췌 요약.
- 교차확인된 근거.
- 충돌하거나 약한 근거.
- 전망 합성에 사용할 수 있는 근거와 제외할 근거.
