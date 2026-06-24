# KoBroadcastFairBench

**KoBroadcastFairBench** is a work-in-progress benchmark project for evaluating context-aware fairness in Korean broadcast scripts.

The immediate goal is practical and narrow:

> Build a real Korean broadcast-script benchmark, use Codex-assisted toxic/non-toxic and fairness-taxonomy pre-labeling, human-adjudicate a locked test set, and evaluate whether the existing RoBERTa + SWA baseline outperforms a non-SWA baseline.

## Why this benchmark?

Existing project code under the related broadcast task is based on KLUE-NER with `klue/roberta-base`, `klue/roberta-large`, SWA, and ensemble evaluation. It does not yet contain real broadcast-script fairness labels. KoBroadcastFairBench fills that gap by turning real broadcast scripts into a benchmark for:

- toxic vs. non-toxic triage,
- bias category classification,
- context-aware distinction between direct harmful expression and quoted/critical reporting,
- span tagging compatible with the legacy KLUE-NER/RoBERTa/SWA pipeline,
- subgroup fairness metrics such as worst-group accuracy and subgroup gap.

## Current status

- [x] Taxonomy v1 drafted.
- [x] Codex-assisted label schema/prompt drafted.
- [x] Pilot labels generated on 23 public MBC broadcast-news transcript segments without redistributing raw text.
- [x] Priority real-data sources identified.
- [ ] AI Hub dataset download approval pending.
- [ ] AI Hub 71557 / 591 ingestion.
- [ ] Human adjudication protocol and locked test set.
- [ ] RoBERTa non-SWA vs SWA benchmark table.

## Priority data sources

| Priority | Dataset | Role | Status |
|---:|---|---|---|
| 1 | AI Hub 71557: 뉴스 대본 및 앵커 음성 데이터 | Core news broadcast script benchmark | API file tree checked; web approval required |
| 2 | AI Hub 591: 방송 콘텐츠 대본 요약 데이터 | General broadcast script benchmark | API file tree checked; web approval required |
| 3 | AI Hub 71314: 방송콘텐츠 대화체 음성인식 데이터 | Dialogue/speaker metadata extension | API file tree checked; web approval required |
| 4 | AI Hub 463: 방송 콘텐츠 대화체 음성인식 데이터 | ASR transcript extension | API file tree checked; web approval required |
| 5 | AI Hub 558: 텍스트 윤리검증 데이터 | Toxicity/ethics auxiliary calibration | API file tree checked; web approval required |

Raw AI Hub data is **not** included in this repository. Follow each dataset's terms of use.

## Repository contents

```text
.
├── DATASET_CARD.md
├── BENCHMARK_TASKS.md
├── README.md
├── data/pilot/                       # label metadata only, no raw broadcast text
├── docs/                             # GitHub Pages site
├── guidelines/                       # annotation guideline
├── prompts/                          # Codex-assisted labeling prompt
├── schemas/                          # label JSON schema
├── scripts/                          # validation helpers
└── taxonomy/                         # fairness taxonomy
```

## Quick validation

```bash
python scripts/validate_labels.py \
  --labels data/pilot/mbc_public_codex_toxic_taxonomy_labels_v0.jsonl \
  --source data/pilot/mbc_public_segment_manifest.jsonl
```

Expected pilot summary:

- 23 real public broadcast-news segments in the manifest,
- 22 nontoxic pre-labels,
- 1 toxic mention pre-label,
- 1 regional-bias candidate requiring human review.

## Important release policy

This repository intentionally excludes:

- AI Hub raw data,
- broadcaster raw transcript text,
- MBC raw HTML/text cache,
- API keys, credentials, `.secret/`, and private files.

The public artifacts here are benchmark definitions, schemas, prompts, metadata, label offsets/hashes, and scripts.

## Planned evaluation

| Model | Training | Main comparison |
|---|---|---|
| KLUE RoBERTa-base | standard fine-tuning | non-SWA baseline |
| KLUE RoBERTa-base | SWA fine-tuning | SWA effect |
| KLUE RoBERTa-large | standard fine-tuning | non-SWA baseline |
| KLUE RoBERTa-large | SWA fine-tuning | SWA effect |
| SWA ensemble | logit averaging | optional best model |

