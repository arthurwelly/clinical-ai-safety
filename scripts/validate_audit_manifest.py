#!/usr/bin/env python3
"""Validate case audit manifests against committed report and transcript paths."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TOP_LEVEL = {
    "case_id",
    "title",
    "risk_category",
    "simulated_case",
    "patient_data",
    "translation_available",
    "test_date",
    "report_path",
    "models",
}
REQUIRED_MODEL_FIELDS = {
    "model_name",
    "provider_surface",
    "access_mode",
    "transcript_path",
    "outcome_label",
    "verdict",
}


def validate_manifest(path: Path) -> None:
    case_dir = path.parent
    data = json.loads(path.read_text(encoding="utf-8"))

    missing = REQUIRED_TOP_LEVEL - data.keys()
    if missing:
        raise ValueError(f"{path}: missing top-level fields: {sorted(missing)}")

    if data["simulated_case"] is not True:
        raise ValueError(f"{path}: simulated_case must be true")
    if data["patient_data"] is not False:
        raise ValueError(f"{path}: patient_data must be false")

    report_path = case_dir / data["report_path"]
    if not report_path.is_file():
        raise ValueError(f"{path}: report_path does not exist: {data['report_path']}")

    models = data["models"]
    if not isinstance(models, list) or not models:
        raise ValueError(f"{path}: models must be a non-empty list")

    seen_transcripts: set[str] = set()
    for index, model in enumerate(models, start=1):
        missing_model_fields = REQUIRED_MODEL_FIELDS - model.keys()
        if missing_model_fields:
            raise ValueError(
                f"{path}: model {index} missing fields: {sorted(missing_model_fields)}"
            )

        transcript = model["transcript_path"]
        transcript_path = case_dir / transcript
        if not transcript_path.is_file():
            raise ValueError(f"{path}: transcript_path does not exist: {transcript}")
        if transcript in seen_transcripts:
            raise ValueError(f"{path}: duplicate transcript_path: {transcript}")
        seen_transcripts.add(transcript)


def main() -> None:
    manifests = sorted(ROOT.glob("*/audit_manifest.json"))
    if not manifests:
        raise SystemExit("no audit_manifest.json files found")

    for manifest in manifests:
        validate_manifest(manifest)

    print(f"ok: {len(manifests)} audit manifest(s)")


if __name__ == "__main__":
    main()
