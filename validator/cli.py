"""Phase 1.5 validator CLI entrypoint."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__:
    from .phase1_5_validator import (
        HwpxParseError,
        Phase15Validator,
        ValidationReport,
    )
    from .template_loader import TemplateValidationError
else:  # pragma: no cover - script execution from repo root
    from phase1_5_validator import (  # type: ignore
        HwpxParseError,
        Phase15Validator,
        ValidationReport,
    )
    from template_loader import TemplateValidationError  # type: ignore


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Phase 1.5 YAML-driven HWPX validator CLI"
    )
    parser.add_argument(
        "template",
        type=Path,
        help="Path to the YAML template describing expected document structure",
    )
    parser.add_argument(
        "hwpx",
        type=Path,
        help="Path to the generated HWPX file to validate",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Optional path to write a JSON report (defaults to stdout only)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="CLI stdout format (json or text)",
    )
    parser.add_argument(
        "--fail-on",
        choices=["warn", "error"],
        default="error",
        help="Minimum severity that should cause a non-zero exit code",
    )
    return parser.parse_args(argv)


def emit_report(report: ValidationReport, fmt: str) -> None:
    if fmt == "json":
        print(report.to_json())
    else:
        print(report.to_text())


def maybe_write_report(report: ValidationReport, destination: Path | None) -> None:
    if not destination:
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(report.to_json(), encoding="utf-8")


def determine_exit_code(report: ValidationReport, fail_on: str) -> int:
    fail_threshold = {"warn": {"warn", "error"}, "error": {"error"}}
    blocked = fail_threshold[fail_on]
    for finding in report.findings:
        if finding.severity in blocked:
            return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        validator = Phase15Validator(args.template)
    except (TemplateValidationError, FileNotFoundError) as exc:
        print(f"Template error: {exc}", file=sys.stderr)
        return 2
    try:
        report = validator.validate(args.hwpx)
    except HwpxParseError as exc:
        print(f"HWPX error: {exc}", file=sys.stderr)
        return 3
    emit_report(report, args.format)
    maybe_write_report(report, args.report)
    return determine_exit_code(report, args.fail_on)


if __name__ == "__main__":
    sys.exit(main())
