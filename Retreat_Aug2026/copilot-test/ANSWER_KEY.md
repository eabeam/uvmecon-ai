# Answer key — synthetic RP-04 proposal (`proposal_medium_PFL.docx`)

Fictional author ("Andy Dwyer"), fictional numbers, real citations. Written 2026-08-26 to test Copilot grading at the department retreat, using Emily's actual S26 RP-04 grading prompt (`COPILOT_PROMPT.md`). Modeled on the S26 RP-04 rubric guidance and the common deductions in the S26 grading reports; the topic is deliberately unlike any S26 student's.

**Target: ~28.5/38 (class median was 31.25; mean 30.05).**

## Planted flaws (what a good grader should catch)

| # | Where | Flaw | Rubric line hit |
|---|---|---|---|
| 1 | Intro, first sentence | RQ opens broad ("How does paid family leave affect mothers?") before narrowing — reader has to wait for the specific question | RQ specific & answerable (2) |
| 2 | Intro, last sentence | "This paper **will show the causal effect**" from a two-way-FE OLS with no discussion of identification | Qualified assertions (2) |
| 3 | Lit review, structure | Four paragraphs that each summarize one paper in isolation; synthesis is one sentence at the end; no "what is unknown" | Literature (4) — summary vs. synthesis |
| 4 | Lit review, last paragraph | Calls them "five peer-reviewed studies" — Bailey et al. (2019) is an NBER working paper | Literature (4) — source counting |
| 5 | Table 1 | No split of means by PFL vs. non-PFL states even though the whole design is a group comparison | Summary stats (4) |
| 6 | Table 1 | Variable labeled with the code `nchild` instead of "Number of own children" | Summary stats (4) — formatting |
| 7 | Equation section | *X* defined only as "a vector of individual controls" (controls are listed earlier in Data, but not in the specification) | Specification (4) — variables defined |
| 8 | Equation section | No mention of standard errors / clustering at the state level | Specification / critical thinking |
| 9 | Planned analysis, last sentence | "this will **prove** that paid leave increases mothers employment" — overclaim + missing apostrophe | Qualified assertions (2); writing (4) |
| 10 | Threats | Names the omitted variable (state economic/political conditions) and its bias direction, and proposes FE — good — but never mentions staggered adoption, pre-trends, state-specific trends, or the small number of treated states; "reverse causality unlikely" is asserted, not argued | Threats (2) |
| 11 | Threats, para 1 | "does not **effect** whether her state passes a law" (affect/effect) | Writing (4) |
| 12 | Threats, para 2 | Run-on with ", however I expect this to be small" | Writing (4) |
| 13 | References | **Waldfogel (1998)** is cited in the introduction but missing from the bibliography | Bibliography (2) |
| 14 | Lit review | **Only 3 peer-reviewed sources in the lit review** (Rossin-Slater; Baum & Ruhm; Byker) + 1 NBER — fails the 4-peer-reviewed rule. *(Key originally said this was met — corrected 2026-08-26 after both Copilot and Claude counted correctly.)* Intro has 3 sources (Blau & Kahn; Goldin; Waldfogel) — fine. | Literature (4) — source count |

## What is genuinely fine (a grader should NOT deduct for)

- Dataset named, cited, unit of observation / sample restriction / years stated; cleaning step mentioned (thinly).
- Equation is in proper form with subscripts, fixed effects, and an error term; β₁ interpreted substantively.
- State and year FE are explained in plain language with a concrete example.
- Heterogeneity plan (youngest child < 1; by education) is motivated by the literature.
- ~1,300 words excluding references, paragraphs, clear section headings.
- All seven bibliography entries are real papers with correct venues.

## Expected score by criterion (my estimate — on Emily's 5-level scale, no interpolation)

Valid scores: 4-pt criteria → 0/1/2/3/4; 2-pt criteria → 0/0.5/1/1.5/2.

| Component | Criterion | Pts | Expected |
|---|---|---|---|
| Intro | Research question | 2 | 1.5 |
| Intro | Motivation (≥2 sources) | 4 | 3 |
| Lit | Literature (linked; ≥4 peer-reviewed distinct) | 4 | 2 |
| Data | Data identification | 2 | 2 |
| Data | Summary stats table | 4 | 3 |
| Empirical | Specification | 4 | 3 |
| Empirical | Critical thinking | 4 | 3 |
| Empirical | Qualified assertions | 2 | 1 |
| Threats | Threats discussion | 2 | 1.5 |
| Presentation | Bibliography | 2 | 1.5 |
| Presentation | Formatting | 4 | 4 |
| Presentation | Writing quality | 4 | 3 |
| | **Total** | **38** | **≈ 28.5** |

## What to look for in Copilot's output

- Does it catch #2 and #9 (overclaiming)? This is the single most common failure mode in the class and the rubric says so explicitly.
- Does it catch #13 (missing Waldfogel)? This is what the Turn-2 citation pass exists for; see whether the content pass alone finds it.
- Does it catch #4 (NBER ≠ peer-reviewed)? Requires knowing the rubric's rule.
- Does it hedge toward 30–32 (drift upward) or penalize everything (drift downward)? Compare to the ~28.5 estimate.
- Does it invent flaws that aren't there (e.g., "no error term," "no data source")? That's the hallucination check.

## Turn 2 / Turn 3 expectations

- **Citation pass** should find: Waldfogel (1998) in-text but not in bibliography; Bailey et al. (2019) = NBER working paper (not peer-reviewed); only 3 peer-reviewed in the lit review (Rossin-Slater et al.; Baum & Ruhm; Byker) → requirement NOT met. All bibliography entries are real; a grader that says otherwise is hallucinating.
- **Data pass** should find: IPUMS CPS ASEC exists and covers 2010–2023; N = 112,430 is plausible for women 20–45 with a child under 5 over 14 ASEC years; all binary means in [0,1]; the table omits nothing from the equation except the "vector of controls" is only listed in prose; subscripts *ist* match individual-state-year; `nchild` should be flagged as a variable code. Nothing internally inconsistent — a red flag on the numbers is a false positive.
