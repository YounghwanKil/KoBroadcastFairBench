# Dataset Card: KoBroadcastFairBench

## Dataset summary

KoBroadcastFairBench is a planned benchmark for Korean broadcast-script fairness. It targets context-aware detection of discriminatory, stereotypical, derogatory, or otherwise bias-relevant expressions in broadcast scripts.

## Task formulation

### T1. Toxic / non-toxic triage
Classify each broadcast segment as:

- `toxic`
- `nontoxic`
- `uncertain`

### T2. Broadcast risk decision
Classify whether the segment is:

- `acceptable`
- `needs_review`
- `problematic`
- `uncertain`

### T3. Fairness taxonomy category
Multi-label categories include gender, age, disability, racial/ethnic/nationality, regional, religion, LGBTQ+, socioeconomic/class, appearance/body, and family structure.

### T4. Context type
Context labels separate direct harmful expression from legitimate reporting/quotation:

- explicit discrimination,
- implicit stereotype,
- overgeneralization,
- derogatory expression,
- biased humor/sarcasm,
- non-discriminatory context,
- quoted/critical mention,
- unclear.

### T5. Span tagging
Risk/group/context spans are represented as character offsets and can be converted to BIO token labels for token classification.

## Data sources

Core planned sources:

1. AI Hub 71557: News scripts and anchor speech.
2. AI Hub 591: Broadcast script summarization dataset.
3. AI Hub 71314/463: Broadcast conversational ASR datasets.
4. AI Hub 558: Text ethics dataset for auxiliary calibration, not final broadcast test.
5. Public MBC transcript URLs for internal pilot only.

## Labeling workflow

1. Segment real broadcast scripts.
2. Run GPT/Codex silver-labeling.
3. Run an optional second GPT/Codex pass for toxic / uncertain / low-confidence samples.
4. Freeze the GPT/Codex silver-label test set.
5. Use train/dev labels for model tuning and the locked test set for final reporting.

## Known limitations

- Pilot labels are GPT/Codex silver labels, not human gold labels.
- Raw broadcast text is not redistributed here.
- AI Hub access requires dataset approval.
- Broadcast fairness depends on video, tone, and production context; text-only labels can be incomplete.

