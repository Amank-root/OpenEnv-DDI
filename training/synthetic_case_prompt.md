# Synthetic DDI Case Prompt (Low-Noise Expansion)

Use this prompt to generate **candidate** synthetic cases for the DDI benchmark.  
Goal: expand by `+20/+20/+20` (easy/medium/hard) with high diversity and low leakage.

## Generator Prompt (copy into your LLM)

You are generating deterministic synthetic clinical DDI triage cases.

Output constraints:
- Return only valid JSON.
- Output format must be:
  {
    "easy": [ ...cases... ],
    "medium": [ ...cases... ],
    "hard": [ ...cases... ]
  }
- Generate exactly 20 new cases per level.
- Do not reuse any existing case_id or template_family strings from seed examples.

Required schema per case:
- case_id: string
- template_family: string namespace like "train::..." or "validation::..."
- split: "train" or "validation"
- age: integer
- labs: object with numeric values (must include egfr, creatinine, potassium, inr; optional alt/ast)
- diagnoses: list[string]
- medications: list[string]
- interactions: list of objects with fields:
  - interaction_id (unique in case)
  - drug_a
  - drug_b
  - severity in {"contraindicated", "major", "moderate", "minor"}
  - evidence
- required_regimens: list[string]
- substitution_options: list of objects with fields:
  - regimen_id
  - replace_drug
  - with_drug
  - target_condition
  - expected_risk_delta (float)
  - rationale

Difficulty rules:
- easy:
  - at least 3 interactions
  - include at least one contraindicated or major
  - required_regimens must be []
  - substitution_options must be []
- medium:
  - at least 4 interactions
  - include context-sensitive moderate interactions near decision boundaries
  - required_regimens must be []
  - substitution_options must be []
- hard:
  - at least 4 interactions
  - include substitution trade-offs
  - required_regimens must have at least 2 entries
  - substitution_options must have at least 3 entries
  - every required_regimen must exist in substitution_options.regimen_id

Diversity targets:
- elderly cohorts (80+)
- renal extremes (egfr near 45 and severe CKD values)
- hepatic stress (alt/ast elevated)
- comorbidity bundles (AF + CKD + HF + diabetes variants)
- decision-boundary flips (moderate interactions that become high-risk due to age/labs)

Anti-noise constraints:
- No duplicate case_id globally.
- No duplicate interaction_id within a case.
- No duplicate regimen_id within a case.
- Avoid near-duplicates (same medication list + same interaction graph + same required regimens).
- Ensure evidence text is specific and clinically plausible.
- Keep values deterministic and realistic.

Split guidance:
- Include both train and validation cases.
- Do not repeat the same template_family string.
- Use stable namespaced families, e.g.:
  - train::elderly-renal-bundle-001
  - validation::hepatic-threshold-flip-003

Return strict JSON only.

## Recommended Workflow

1. Generate candidates into:
   - `training/data/generated_cases_batch_01.json`
2. Run validator:
   - `python training/validate_generated_cases.py --input training/data/generated_cases_batch_01.json --min_new_per_level 20`
3. Fix rejected cases and rerun until validator passes.
4. Human spot-audit 10-20% before merging.
5. Merge approved cases into `task_cases/*.py`.

## Quality Checklist (before merge)

- Schema valid for all cases
- No case/template leakage collisions
- No ID collisions
- Near-duplicate ratio acceptable
- Hard cases have coherent required_regimens/substitution_options mapping
- Mix of train/validation present
- Clinical plausibility spot-checked
