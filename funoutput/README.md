# funoutput

`funoutput`은 FunInvestAgent의 산출물 계층입니다. 세션 요약, 시장 보고서, 포트폴리오 리뷰, 법률 리스크 메모, 전략 메모, 내보내기 파일, 로그를 관리합니다.

## 하위 구조

```text
funoutput/
  exports/    외부 공유용 내보내기 파일
  logs/       검증 로그와 실행 로그
  reports/    정식 보고서
  reviews/    전략 성과 검토와 재수정 기록
  sessions/   세션별 작업 기록
  templates/  보고서 템플릿
```

## 파일명 규칙

```text
YYYY-MM-DD_topic_report-type.md
```

예시:

```text
2026-06-28_monthly-portfolio-review_portfolio-review.md
```

## 산출물 원칙

- 보고서에는 입력 데이터와 가정이 먼저 있어야 한다.
- 출처 ID와 데이터 기준일을 반드시 남긴다.
- 투자 실행 액션은 조건과 리스크를 함께 쓴다.
- 법률/세금 판단은 전문가 검토 필요 여부를 분리한다.
