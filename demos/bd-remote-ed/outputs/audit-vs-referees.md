# AI Audit vs. Actual Referee Reports: Side-by-Side Comparison

**Paper:** "Lowering Barriers to Remote Education: Experimental Impacts on Parental Responses and Learning"
**AI Tool:** Claude (Opus 4.6), simulating `/econ-audit` skill (~60 seconds)
**Referee reports:** AER (2 referees), REStud (desk reject), AEJ:App (desk reject), RESTAT (2 referees), JHR (3 referees), JEBO (2 referees + AE) -- 8 submissions, 11 referee reports + 4 editor letters with substantive comments

---

## 1. Comparison Table: Major Referee Criticisms

### Tier 1: Near-Universal Criticisms

| # | Referee Criticism | Flagged by AI? | AI Finding(s) | Notes |
|---|---|---|---|---|
| 1 | **High attrition (~35-50%) and differential attrition** | Yes | C1 (Critical) | AI flagged differential attrition, called it "serious," noted p<0.001, suggested Lee bounds. Close match to referees' core concern. |
| 2 | **Results don't tell a coherent story / mechanisms unconvincing** | Partial | A1 (Critical), A2 (Important) | AI identified that the mediation chain is "not identified" and that non-tutoring channels are not ruled out. But it framed this as an econometric identification problem. Referees went further: they pointed out specific *internal contradictions* (e.g., data intervention increased tutoring more than info did, yet only info improved learning; general info had same format but no effect). The AI missed these devastating within-paper inconsistencies that multiple referees independently highlighted. |
| 3 | **Theoretical model not useful / poorly integrated** | Yes | D2 (Minor) | AI noticed the commented-out framework and noted its absence weakens the mechanism story. But it rated this as Minor and suggested *including* the model. Referees were harsher: they wanted it *cut entirely* because it adds pages but generates no testable predictions. The AI's recommendation was the opposite of what referees wanted. |
| 4 | **Short intervention duration (4-8 weeks)** | No | -- | Not flagged. The AI never mentioned that 4-8 weeks is unusually short for an education intervention. This requires field knowledge about typical intervention durations in development economics -- exactly the kind of domain judgment an AI lacks. |
| 5 | **Noisy/inadequate learning measures (8-question phone test)** | Yes | C3 (Important) | AI flagged the 8-item phone assessment, noted it falls below recommended IRT minimums, and raised the phone-familiarity confound. Good match. Referees made the same points (JHR R1 was particularly sharp on the phone-familiarity issue). |

### Tier 2: Frequently Raised Criticisms

| # | Referee Criticism | Flagged by AI? | AI Finding(s) | Notes |
|---|---|---|---|---|
| 6 | **Paper too long and hard to follow** | Yes | E1 (Minor) | AI flagged length and commented-out material, suggested cutting 20-30%. Referees said the same, with several noting it was confusing on first read. JEBO R2 recommended a 5-6 page short note. |
| 7 | **Multiple hypothesis testing issues** | Yes | B1 (Critical), B2 (Critical), B3 (Critical) | AI flagged MHT aggressively -- no adjustment across domains/treatments, learning result below MDE, and underpowered heterogeneity. Referees raised similar concerns (q-values not applied to subsamples, FWER vs. FDR switch). Strong match. |
| 8 | **Limited external validity / COVID-specific context** | Partial | C4 (Minor) | AI noted the smartphone-ownership sample restriction. But it did not engage with the deeper external validity concern that referees emphasized: whether findings from pandemic school closures generalize to normal schooling at all, and that the bar for "another COVID edtech paper" is now very high. |
| 9 | **Deviations from pre-analysis plan** | Yes | B5 (Important) | AI flagged the late PAP registration and noted apparent deviations. JHR R1 was more specific (dropped Bangla outcomes, omitted pre-registered domains, switched from FWER to FDR). AI caught the spirit but not the specifics. |
| 10 | **Complex randomization hard to interpret** | Yes | D1 (Important), A3 (Important), A4 (Important) | AI flagged the 9-coefficient specification, the confounded teacher-support comparison, and the bundled data package. Referees raised the same issues (RESTAT R1 couldn't tell what the coefficients meant). Strong match. |

---

## 2. What the AI Caught That Referees Did NOT Emphasize

These represent potential "bonus points" for the demo -- issues where the AI adds value beyond what human reviewers focused on.

| AI Finding | Severity | Why referees may not have flagged it |
|---|---|---|
| **B4. Lasso-selected covariates and researcher degrees of freedom** | Important | No referee mentioned lasso covariate selection. Referees focused on bigger-picture problems; covariate selection is a methodological detail that requires reading the specification section carefully. |
| **D3. Cost-effectiveness excludes induced private costs** | Minor | JHR R2 and JEBO R2 actually did flag this -- so this is a match, not a unique AI catch. But the AI's framing was more precise: it quantified the misleading comparison ($5.44 vs. $0.89 per $100). |
| **E2. Headline framing rests on the most fragile result** | Minor | Only AER R2 hinted at this. The AI explicitly recommended reframing around the parental investment results, which is close to what JEBO R2 recommended. The AI's strategic advice was surprisingly aligned with the most constructive referee. |
| **E3. "Widened inequality" claim overstated** | Minor | No referee specifically challenged the "widened inequality" language vs. "differential benefit." The AI made a technically precise distinction that referees did not. |
| **B2. Winner's curse / Type M error** | Critical | No referee used the language of winner's curse or Type M error. AER R1 noted the result is insignificant after MHT adjustment, but the AI's framing in terms of the MDE exceeding the point estimate is a distinct statistical insight. |
| **A2. Non-tutoring channels not ruled out** | Important | Referees focused on the tutoring channel's internal contradictions rather than on the exclusion-restriction logic for other channels. The AI's point -- that information could change motivation, monitoring, or interaction quality -- is valid and distinct. |

---

## 3. What Referees Caught That the AI Missed

These are important for honest framing -- the "you still need a human" slide.

| Referee Concern | Who raised it | Why the AI likely missed it |
|---|---|---|
| **Short intervention duration (4-8 weeks)** | AER R1, AER R2, JEBO R1, RESTAT R2 | Requires knowing that education RCTs typically run 1-3 years. This is domain knowledge about field norms, not something extractable from the manuscript alone. |
| **Internal contradictions in the mechanism story** | AER R1, AER R2, JHR R1, JHR R2 | Referees noticed that if tutoring is the mechanism, the data intervention (which increased tutoring *more*) should also improve learning -- but it doesn't. They noticed general info (same format) had no effect. These are logical tests that require reading the results tables against the paper's own claims. The AI identified the identification problem abstractly but did not run these specific falsification-style checks. |
| **COVID generalizability / "another COVID paper" fatigue** | RESTAT Editor, REStud Editor, AER R1 | Requires knowing the publication landscape -- how many similar papers exist, editorial appetite for the topic, and how much the field has moved on. This is publication strategy, not econometrics. |
| **The paper should be a short note** | JEBO R2/JHR R3 | The most constructive referee advice was to radically restructure the paper into a 5-6 page methodological note. The AI suggested trimming but did not propose a fundamentally different paper format. This requires understanding genre conventions and strategic positioning. |
| **Missing pre-registered outcomes (Bangla, student engagement domains)** | JHR R1 | The AI noted the late PAP in general terms. JHR R1 identified *specific* pre-registered outcomes that were dropped without adequate justification (Bangla scores, domains 5 and 7). This requires comparing the paper to the actual PAP. |
| **Specific alternative robustness checks** | Multiple referees | Referees requested Oster-style selection-on-unobservables analysis, Ghanem et al. (2023) attrition framework, Goldsmith-Pinkham et al. (2024) contamination bias test, and specification curves. The AI suggested Lee bounds but did not reference these newer methods. |
| **Data package could be sold/transferred** | JHR R3 | A creative "threat to identification" -- parents might sell the 100GB data to others and use the cash for tutoring. This kind of context-specific institutional knowledge is hard for an AI to generate. |
| **Smartphone ownership vs. access distinction** | JHR R3 | Sharing a phone within a household limits EdTech usage. Requires understanding how smartphones are actually used in rural Bangladesh. |

---

## 4. Summary

### Headline

**The AI flagged 7 of 10 major referee concerns in ~60 seconds** (5 full matches, 2 partial matches, 1 opposite recommendation, 2 complete misses).

Against the 5 Tier 1 near-universal criticisms specifically: **3 of 5 fully flagged, 1 partially flagged, 1 completely missed.**

### What the AI is good at

- **Statistical and econometric issues**: MHT problems, power analysis, attrition, identification failures. The AI's strongest category -- it caught every major statistical concern and added some (winner's curse, lasso degrees of freedom) that referees did not emphasize.
- **Internal consistency of causal claims**: The AI correctly identified that the mediation chain (info -> tutoring -> learning) is not identified. This was the paper's core vulnerability.
- **Structural completeness**: The AI systematically checked measurement, methodology, and presentation. It produced a well-organized audit that covers the same territory referees collectively covered.

### What the AI misses

- **Field norms and benchmarks**: It did not know that 4-8 weeks is short for an education RCT. It did not know that the COVID edtech literature is now crowded. Domain knowledge about "what's normal" in a subfield is a gap.
- **Within-paper falsification logic**: Referees ran the paper's claims against its own results and found contradictions (data arm increased tutoring more but didn't improve learning). The AI identified the identification problem abstractly but did not perform these internal consistency checks against the results tables.
- **Publication strategy**: No advice on journal targeting, paper format (short note vs. full paper), or how to position the contribution relative to the existing literature.
- **Institutional and contextual knowledge**: How phones are shared in Bangladeshi households, whether data packages can be resold, what the EdTech tool actually looks like in practice.
- **Cutting-edge methodological references**: Referees cited Ghanem et al. (2023), Goldsmith-Pinkham et al. (2024), and other recent advances. The AI suggested standard tools (Lee bounds, Heckman/Pinto mediation) but not the newest methods.

### One-line takeaway for the demo

> An AI audit in 60 seconds catches most of the statistical and identification problems that 11 referees across 8 journal submissions surfaced over 4 years -- but it cannot replace the field knowledge, internal-logic stress-testing, and publication strategy that human experts provide.

---

*Compiled 2026-04-24 for UVM Faculty AI Bootcamp demo.*
