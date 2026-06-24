#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

TOXICITY = {"toxic", "nontoxic", "uncertain"}
RISK_DECISIONS = {"acceptable", "needs_review", "problematic", "uncertain"}
BIAS_CATEGORIES = {
    "gender_bias", "ageism", "disability_bias", "racial_ethnic_nationality_bias",
    "regional_bias", "religious_bias", "lgbtq_bias", "socioeconomic_class_bias",
    "appearance_bias", "family_structure_bias", "no_bias",
}
CONTEXT_TYPES = {
    "explicit_discrimination", "implicit_stereotype", "overgeneralization",
    "derogatory_expression", "humor_sarcasm_with_bias", "non_discriminatory_context",
    "quoted_critical_mention", "unclear",
}


def read_jsonl(path: Path):
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if line.strip():
                yield line_no, json.loads(line)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--labels", default="data/pilot/mbc_public_codex_toxic_taxonomy_labels_v0.jsonl")
    parser.add_argument("--source", default="data/pilot/mbc_public_segment_manifest.jsonl")
    args = parser.parse_args()

    labels_path = Path(args.labels)
    source_path = Path(args.source)
    manifest = {obj["sample_id"]: obj for _, obj in read_jsonl(source_path)}
    counts = Counter()

    for line_no, obj in read_jsonl(labels_path):
        sid = obj.get("sample_id")
        if sid not in manifest:
            raise ValueError(f"line {line_no}: unknown sample_id {sid}")
        if "text" in obj:
            raise ValueError(f"line {line_no}: raw text must not be included in public labels")
        if obj.get("toxicity_label") not in TOXICITY:
            raise ValueError(f"line {line_no}: invalid toxicity_label")
        if obj.get("broadcast_risk_decision") not in RISK_DECISIONS:
            raise ValueError(f"line {line_no}: invalid broadcast_risk_decision")
        invalid_bias = set(obj.get("bias_categories", [])) - BIAS_CATEGORIES
        if invalid_bias:
            raise ValueError(f"line {line_no}: invalid bias_categories {sorted(invalid_bias)}")
        invalid_context = set(obj.get("context_types", [])) - CONTEXT_TYPES
        if invalid_context:
            raise ValueError(f"line {line_no}: invalid context_types {sorted(invalid_context)}")
        text_len = int(manifest[sid].get("text_length", 0))
        for span in obj.get("risk_spans", []):
            start, end = int(span["start"]), int(span["end"])
            if not (0 <= start <= end <= text_len):
                raise ValueError(f"line {line_no}: invalid span {start}:{end} for {sid}")
        counts[(obj["toxicity_label"], obj["broadcast_risk_decision"])] += 1

    print(json.dumps({
        "labels": str(labels_path),
        "manifest": str(source_path),
        "num_manifest_samples": len(manifest),
        "num_labels": sum(counts.values()),
        "summary": {str(k): v for k, v in counts.items()},
    }, ensure_ascii=False, indent=2))
    print("KOBROADCASTFAIRBENCH_LABELS_VALID")


if __name__ == "__main__":
    main()
