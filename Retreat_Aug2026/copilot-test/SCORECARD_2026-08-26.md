# Scorecard — one proposal, four graders, one rubric (2026-08-26)

Paper: `proposal_medium_PFL.docx` (Andy Dwyer, synthetic, target ≈ 28.5/38). Rubric + instructions: Emily's actual S26 RP-04 content-grading prompt (`grading_instructions_rp04.txt`). All graders blind to the answer key. Claude passes were fresh subagents with only the two files; Copilot = UVM NetID with both files attached; Codex = Emily, same files.

## Scores

| Criterion (pts) | Expected | Copilot | Fable | Sonnet | Codex |
|---|---|---|---|---|---|
| Research question (2) | 1.5 | 2 | 2 | 2 | 2 |
| Motivation (4) | 3 | 4 | 4 | 4 | 4 |
| Literature (4) | 2 | 3 | **2** | 3 | **2** |
| Data identification (2) | 2 | 2 | 2 | 2 | 2 |
| Summary stats table (4) | 3 | 4 | **3** | 4 | **3** |
| Specification (4) | 3 | 4 | 4 | 4 | 4 |
| Critical thinking (4) | 3 | 3 | 3 | 3 | 3 |
| Qualified assertions (2) | 1 | 0.5 | 1 | 1 | 0.5 |
| Threats (2) | 1.5 | 2 | 2 | 2 | 2 |
| Bibliography (2) | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 |
| Formatting (4) | 4 | 4 | 4 | 4 | 4 |
| Writing quality (4) | 3 | 4 | 4 | 4 | 4 |
| **Total (38)** | **≈28.5** | **34** | **32.5** | **34.5** | **32** |
| Drift vs. expected | — | +5.5 | +4 | +6 | +3.5 |
| Honored no-interpolation rule | — | yes | yes | yes | yes |
| Invented flaws | — | none | none | none | none |

## Planted flaws — caught (✅ scored), noted (📝 mentioned but not deducted), missed (✗)

| # | Flaw | Copilot | Fable | Sonnet | Codex |
|---|---|---|---|---|---|
| 2, 9 | Two causal overclaims ("will show the causal effect"; "will prove") | ✅ | ✅ | ✅ | ✅ |
| 4, 14 | NBER ≠ peer-reviewed → only 3 peer-reviewed in lit review | ✅ | ✅ | 📝 | ✅ |
| 13 | Waldfogel (1998) cited, missing from bibliography | ✅ | ✅ | ✅ | ✅ |
| 3 | Summary-not-synthesis lit review | 📝 | ✅ | ✗ ("good synthesis") | ✅ |
| 10 | Pre-trends / staggered adoption not addressed | ✅ | ✅ | ✅ | ✅ |
| 5 | No PFL vs. non-PFL split in Table 1 | ✗ | ✅ | 📝 | ✅ |
| 6 | `nchild` variable code as label | ✗ | ✅ | ✗ | ✅ |
| 7 | Controls undefined in the specification | ✗ | 📝 (no rationale) | 📝 (no rationale) | ✅ (no rationale, deducted) |
| 8 | No standard-error / clustering discussion | ✗ | ✅ | ✗ | 📝 (in Next Steps) |
| 1 | Broad opening RQ | ✗ | 📝 | ✗ | ✗ |
| 11, 12, 9b | affect/effect; run-on; missing apostrophe | ✗ | 📝 | 📝 | 📝 |
| — | **Unplanted, valid:** married / n. children as post-treatment "bad controls" | ✗ | ✅ | ✅ | ✗ |
| — | **Unplanted, valid:** CA/NJ always-treated in 2010–2023 → no identifying variation; event-study + clustering + weights | ✗ | ✅ (CA/NJ) | ✗ | ✅ (all three) |

## Read

- **Everyone drifts up, on the judgment criteria.** Motivation, threats, writing: full marks from all four, even where the notes name the flaw. Exactly the S26 pattern (11/17 under-scored there — the direction differs, the mechanism is the same: interpolated-scale criteria are where the model's own taste takes over).
- **Gates and checks were reliable across all four:** the overclaims, the missing reference, the source count (Sonnet counted correctly but scored 3 anyway).
- **The spread is "noticed → deducted."** Copilot 34 (noticed 5, deducted 4); Sonnet 34.5 (noticed 9, deducted 3); Fable 32.5 (noticed 12, deducted 6); Codex 32 (noticed 11, deducted 6). Nobody hallucinated. Three of four found a real flaw the author didn't plant (bad controls; CA/NJ always-treated).
- **Codex was closest to target and wrote the best Next Steps** (event study, state clustering, weights, infant-first sample, a four-column results table with the exact hedged sentence to use). Fable had the most complete flaw list. Sonnet noticed nearly everything and deducted least — the purest "noticed, didn't deduct" case. Copilot: reliable on the checks, blind to the table and specification details.
- **Emily's April observation (Claude > Codex on rubric-following) did not replicate today on this one paper**: Codex followed the rubric at least as faithfully as Fable. One paper, one run — a data point, not a finding.
- **For the room:** a single Copilot pass with your real rubric gets the checks right and lands ~5 points generous. That's usable for a first pass *if you read the notes, not the numbers* — and it's the argument for a second pass or a strict-grader companion.

## Files
- `copilot_grade_2026-08-26.md` (table only)
- `claude_grade_2026-08-26.md` (Fable, full write-up incl. Feedback + Next Steps)
- `sonnet_grade_2026-08-26.md` (full write-up)
- `codex_grade_2026-08-26.md` (full write-up, run by Emily)
- `ANSWER_KEY.md` (corrected 2026-08-26: lit-review source count)
