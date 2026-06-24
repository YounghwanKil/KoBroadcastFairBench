# Benchmark construction task board

## Phase 0: Repository and release hygiene

- [x] Create benchmark page/repository.
- [x] Exclude raw text, raw HTML, audio, and credentials.
- [x] Publish taxonomy, schema, prompt, and pilot metadata.

## Phase 1: Data acquisition

- [ ] Request AI Hub approval for dataset 71557.
- [ ] Request AI Hub approval for dataset 591.
- [ ] Request AI Hub approval for dataset 558.
- [ ] Optional: request approval for datasets 71314 and 463.
- [ ] Download label zip files only first.
- [ ] Inspect JSON schema and write ingestion adapters.

## Phase 2: Benchmark data creation

- [ ] Normalize scripts into `sample_id`, `source`, `genre`, `speaker`, `text`, `metadata`.
- [ ] Segment scripts into 3-15 turn units or paragraph units.
- [ ] Run GPT/Codex silver-label toxic/non-toxic + taxonomy silver-labeling.
- [ ] Export human annotation sheets.
- [ ] Adjudicate labels and freeze locked test split.

## Phase 3: Modeling

- [ ] Convert labels to BIO tagging format.
- [ ] Add `--use_swa false` baseline to legacy RoBERTa training code.
- [ ] Train base/large non-SWA baselines.
- [ ] Train base/large SWA variants.
- [ ] Evaluate span F1, macro-F1, worst-group accuracy, subgroup gap, context confusion.

## Phase 4: Reporting

- [ ] Build benchmark leaderboard table.
- [ ] Add error analysis examples without exposing raw restricted text.
- [ ] Prepare software registration materials.
- [ ] Prepare final progress-check slides.

