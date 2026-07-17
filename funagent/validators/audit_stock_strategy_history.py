from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path


PREDICTION_ID_RE = re.compile(r"\b(?:KR|US)-[A-Z0-9]+-\d{8}-\d+\b")
OUTCOME_MAP = {
    "성공": "success",
    "부분 성공": "partial_success",
    "부분성공": "partial_success",
    "실패": "failure",
    "판정 불가": "unknown",
    "미판정": "unknown",
}
PREDICTIVE_MARKERS = (
    "예측 보정",
    "내일 예측",
    "시장 예측",
    "종목·섹터 예측",
    "시나리오",
)
SUPPLY_MARKERS = (
    "잠재 매수·매도 물량",
    "오버행 게이트",
    "supply_overhang_order_flow",
)
CYCLE_MARKERS = (
    "급등주·순환주 사이클 분류",
    "momentum_rotation_cycle",
)


@dataclass
class FileAudit:
    path: str
    market: str
    prediction_ids: list[str]
    defined_prediction_ids: list[str]
    outcome_rows: dict[str, int]
    outcome_ids: list[str]
    has_predictive_content: bool
    has_supply_contract: bool
    has_cycle_contract: bool


def classify_market(path: Path, content: str) -> str:
    haystack = f"{path.name}\n{content[:6000]}".lower()
    kr_score = sum(haystack.count(term) for term in ("korea", "국내", "한국", "kospi", "krx", "코스피"))
    us_score = sum(haystack.count(term) for term in ("us_", "미국", "nasdaq", "nyse", "qqq", "s&p"))
    if kr_score and us_score and min(kr_score, us_score) >= 2:
        return "MIXED"
    if kr_score > us_score:
        return "KR"
    if us_score > kr_score:
        return "US"
    return "UNKNOWN"


def parse_table_outcomes(content: str) -> tuple[Counter[str], set[str]]:
    counts: Counter[str] = Counter()
    outcome_ids: set[str] = set()
    for line in content.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        statuses = [OUTCOME_MAP[cell] for cell in cells if cell in OUTCOME_MAP]
        if not statuses:
            continue
        for status in statuses:
            counts[status] += 1
        outcome_ids.update(PREDICTION_ID_RE.findall(line))
    return counts, outcome_ids


def parse_defined_prediction_ids(content: str) -> set[str]:
    defined: set[str] = set()
    prediction_table = False
    for line in content.splitlines():
        if not line.lstrip().startswith("|"):
            prediction_table = False
            continue
        cells = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
        if "prediction_id" in cells:
            probability_columns = {"상승 확률", "혼조 확률", "박스권 확률", "하락 확률", "up", "flat", "down"}
            prediction_table = bool(probability_columns.intersection(cells))
            continue
        if prediction_table:
            defined.update(PREDICTION_ID_RE.findall(line))
    return defined


def audit_file(root: Path, path: Path) -> FileAudit:
    content = path.read_text(encoding="utf-8")
    prediction_ids = sorted(set(PREDICTION_ID_RE.findall(content)))
    defined_prediction_ids = sorted(parse_defined_prediction_ids(content))
    outcomes, outcome_ids = parse_table_outcomes(content)
    return FileAudit(
        path=path.relative_to(root).as_posix(),
        market=classify_market(path, content),
        prediction_ids=prediction_ids,
        defined_prediction_ids=defined_prediction_ids,
        outcome_rows=dict(outcomes),
        outcome_ids=sorted(outcome_ids),
        has_predictive_content=any(marker in content for marker in PREDICTIVE_MARKERS),
        has_supply_contract=any(marker in content for marker in SUPPLY_MARKERS),
        has_cycle_contract=any(marker in content for marker in CYCLE_MARKERS),
    )


def load_ledger(root: Path) -> tuple[list[dict[str, object]], list[str]]:
    path = root / "funoutput/logs/stock_prediction_ledger.jsonl"
    if not path.is_file():
        return [], []
    records: list[dict[str, object]] = []
    errors: list[str] = []
    required = {
        "prediction_id",
        "source_report",
        "market",
        "symbol",
        "display_name",
        "created_at",
        "data_as_of",
        "horizon",
        "verification_due_at",
        "probabilities",
        "success_criteria",
        "failure_criteria",
        "status",
    }
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            errors.append(f"line {line_number}: invalid JSON")
            continue
        if isinstance(record, dict):
            records.append(record)
            missing = sorted(required - set(record))
            if missing:
                errors.append(f"line {line_number}: missing fields {', '.join(missing)}")
            prediction_id = str(record.get("prediction_id", ""))
            if prediction_id and not PREDICTION_ID_RE.fullmatch(prediction_id):
                errors.append(f"line {line_number}: invalid prediction_id {prediction_id}")
            probabilities = record.get("probabilities")
            if isinstance(probabilities, dict):
                try:
                    total = sum(float(probabilities[key]) for key in ("up", "flat", "down"))
                except (KeyError, TypeError, ValueError):
                    errors.append(f"line {line_number}: invalid probabilities")
                else:
                    if abs(total - 1.0) > 1e-9:
                        errors.append(f"line {line_number}: probability sum is {total}")
        else:
            errors.append(f"line {line_number}: record is not an object")
    return records, errors


def build_summary(root: Path) -> dict[str, object]:
    paths = []
    for directory in (root / "funoutput/reports", root / "funoutput/reviews"):
        if directory.is_dir():
            paths.extend(path for path in directory.glob("*.md") if path.name.lower() != "readme.md")

    files = [audit_file(root, path) for path in sorted(paths)]
    ledger_records, ledger_validation_errors = load_ledger(root)
    all_ids = [prediction_id for item in files for prediction_id in item.defined_prediction_ids]
    id_counts = Counter(all_ids)
    outcome_counts: Counter[str] = Counter()
    for item in files:
        outcome_counts.update(item.outcome_rows)

    ledger_ids = [str(record.get("prediction_id", "")) for record in ledger_records if record.get("prediction_id")]
    ledger_id_counts = Counter(ledger_ids)
    scored_ids = sorted(
        {prediction_id for item in files for prediction_id in item.outcome_ids}
        | {str(record["prediction_id"]) for record in ledger_records if record.get("status") == "scored"}
    )
    unique_ids = sorted(id_counts)
    predictive_files = [item for item in files if item.has_predictive_content]

    return {
        "artifact_count": len(files),
        "report_count": sum(item.path.startswith("funoutput/reports/") for item in files),
        "review_count": sum(item.path.startswith("funoutput/reviews/") for item in files),
        "market_counts": dict(Counter(item.market for item in files)),
        "unique_prediction_id_count": len(unique_ids),
        "prediction_ids": unique_ids,
        "duplicate_prediction_ids": sorted(key for key, count in id_counts.items() if count > 1),
        "machine_scored_prediction_ids": scored_ids,
        "unscored_prediction_ids": sorted(set(unique_ids) - set(scored_ids)),
        "ledger_record_count": len(ledger_records),
        "ledger_duplicate_prediction_ids": sorted(key for key, count in ledger_id_counts.items() if count > 1),
        "ledger_validation_errors": ledger_validation_errors,
        "report_prediction_ids_missing_from_ledger": sorted(set(unique_ids) - set(ledger_ids)),
        "ledger_prediction_ids_missing_from_reports": sorted(set(ledger_ids) - set(unique_ids)),
        "ledger_records_missing_source_criteria": sum(
            record.get("success_criteria") == "missing_in_source_report"
            or record.get("failure_criteria") == "missing_in_source_report"
            for record in ledger_records
        ),
        "explicit_outcome_rows": dict(outcome_counts),
        "legacy_outcome_row_count": sum(outcome_counts.values()) - len(scored_ids),
        "predictive_artifact_count": len(predictive_files),
        "predictive_artifacts_without_ids": [item.path for item in predictive_files if not item.defined_prediction_ids],
        "supply_contract_artifact_count": sum(item.has_supply_contract for item in files),
        "cycle_contract_artifact_count": sum(item.has_cycle_contract for item in files),
        "files": [asdict(item) for item in files],
    }


def render_text(summary: dict[str, object]) -> str:
    outcomes = summary["explicit_outcome_rows"]
    market_counts = summary["market_counts"]
    lines = [
        "Stock strategy history audit",
        f"- artifacts: {summary['artifact_count']} (reports={summary['report_count']}, reviews={summary['review_count']})",
        f"- markets: {market_counts}",
        f"- unique prediction IDs: {summary['unique_prediction_id_count']}",
        f"- machine-scored prediction IDs: {len(summary['machine_scored_prediction_ids'])}",
        f"- unscored prediction IDs: {len(summary['unscored_prediction_ids'])}",
        f"- ledger records: {summary['ledger_record_count']}",
        f"- report IDs missing from ledger: {len(summary['report_prediction_ids_missing_from_ledger'])}",
        f"- ledger records missing source criteria: {summary['ledger_records_missing_source_criteria']}",
        f"- ledger validation errors: {len(summary['ledger_validation_errors'])}",
        f"- explicit outcome rows: {outcomes}",
        f"- legacy outcome rows without a machine-scored ID: {summary['legacy_outcome_row_count']}",
        f"- predictive artifacts without IDs: {len(summary['predictive_artifacts_without_ids'])}",
        f"- supply-contract artifacts: {summary['supply_contract_artifact_count']}",
        f"- cycle-contract artifacts: {summary['cycle_contract_artifact_count']}",
    ]
    duplicates = summary["duplicate_prediction_ids"]
    if duplicates:
        lines.append(f"- duplicate IDs: {', '.join(duplicates)}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit prediction and outcome coverage in stock strategy Markdown artifacts.")
    parser.add_argument("--root", default=".", help="Project root directory.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    summary = build_summary(root)
    if args.format == "json":
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(render_text(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
