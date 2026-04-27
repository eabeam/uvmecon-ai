# Adversarial Econometrics Audit

**Paper:** "Lowering Barriers to Remote Education: Experimental Impacts on Parental Responses and Learning"
**Authors:** Beam, Mukherjee, Navarro-Sola
**Audit date:** 2026-04-24
**Auditor:** Claude (Opus 4.6, simulating `/econ-audit`)

---

## Executive Summary

This paper reports results from an RCT with 7,576 households in Bangladesh during COVID-19 school closures, testing three interventions: EdTech information, internet data packages, and phone-based teacher support. The main finding is that EdTech information increased tutoring spending and improved math scores by 0.15 SD, despite not increasing use of the promoted EdTech tool. The paper frames this as evidence that parental re-optimization drives learning gains.

The audit identifies **5 critical**, **8 important**, and **6 minor** issues. The most serious concerns relate to the causal chain linking information to tutoring to learning (which is suggestive, not identified), differential attrition in the learning assessment sample, underpowered heterogeneity analyses that drive the paper's inequality narrative, and a complex randomization design that makes interpretation difficult.

---

## Findings

### A. Identification & Causal Claims

#### A1. The information-to-tutoring-to-learning causal chain is not identified
- **Severity: CRITICAL**
- **Location:** Abstract, Section 5 (Learning), Section 7 (Discussion), Conclusion
- **Claim:** "providing EdTech information improved math scores by 0.15 SD, likely due to increased spending on tutoring" (abstract); "the tutoring itself contributed to the learning gains" (Section 5)
- **Concern:** The paper's central narrative is that EdTech information caused increased tutoring, which caused learning gains. But the paper only identifies the reduced-form ITT effect of information on learning. The mediation claim (information -> tutoring -> learning) is not identified. Tutoring is endogenous -- parents who increased tutoring in response to information may differ on unobservables from those who did not. There is no instrumental variables strategy, no formal mediation analysis with proper exclusion restrictions, and no way to rule out other channels. The paper acknowledges this ("we cannot conclusively identify *why*"), but the abstract, introduction, and conclusion repeatedly state the mediation claim as the primary finding. This mismatch between the identified result (ITT of information on learning) and the headline claim (tutoring drove it) is the paper's most serious issue.
- **Suggested fix:** Clearly distinguish the identified ITT effect from the suggestive mediation evidence. Consider formal mediation analysis (e.g., Heckman/Pinto or Imai/Keele/Tingley), acknowledging the identifying assumptions. Downgrade the mediation language throughout, especially in the abstract and conclusion, from "likely due to" to "consistent with" or "suggestive of."

#### A2. Ruling out direct information effects on learning
- **Severity: IMPORTANT**
- **Location:** Section 5, Discussion
- **Claim:** Learning gains from EdTech information are attributed to tutoring increases, not to the EdTech tool itself, because EdTech tool usage did not increase.
- **Concern:** The paper rules out the EdTech tool as a channel by showing no increase in self-reported usage. But information could affect learning through channels other than tutoring or EdTech tool usage: it could change student motivation, parental attention/monitoring, the quality (not just quantity) of parent-child interactions, or other unobserved behaviors. The paper checks student engagement and finds no effects, but these are coarse self-reported measures collected after the intervention ended. The exclusion of all non-tutoring channels is assumed, not demonstrated.
- **Suggested fix:** Acknowledge more clearly that multiple unobserved channels could mediate the information effect. The tutoring channel is consistent with the data but not uniquely identified.

#### A3. Teacher support: confounded comparison group
- **Severity: IMPORTANT**
- **Location:** Section 2.4 (Randomization), Empirical Specification
- **Claim:** Teacher support effects are estimated via beta_3.
- **Concern:** Teacher support was only randomized among those already receiving the general information treatment (Sangsad TV reminders). The coefficient beta_3 therefore captures the effect of teacher support *conditional on receiving general information*, not the standalone effect of teacher support versus pure control. The paper acknowledges this by including GenInfo as a separate term, but the interpretation throughout treats the teacher support results as if they reflect a clean comparison to control. A reader could easily misinterpret the teacher support effect as "no impact of teacher support vs. nothing" rather than "no incremental impact of teacher support beyond general information."
- **Suggested fix:** Be more explicit throughout that the teacher support comparison group received general information, not nothing. Discuss whether the general information could have affected the teacher support estimates.

#### A4. Data package never provided without information
- **Severity: IMPORTANT**
- **Location:** Section 2.4, Empirical Specification
- **Claim:** beta_2 captures the effect of the data package.
- **Concern:** The data package was always bundled with an information treatment (either EdTech info or general info). There is no "data package only" arm. This means we cannot separate the effect of the data package from its interaction with information. The paper's main specification includes interaction terms, but the "main" data package coefficient actually captures the interaction effect (data + information vs. information alone), not the standalone effect of data provision. This is noted in the methodology but not consistently reflected in interpretation.
- **Suggested fix:** Remind readers more prominently that the data package effect is always conditional on information receipt. Be cautious about generalizing to settings where data is provided without information.

---

### B. Statistical Issues

#### B1. Multiple hypothesis testing across treatment arms and outcomes
- **Severity: CRITICAL**
- **Location:** Throughout Sections 4-6
- **Concern:** The paper tests three main treatment arms across multiple outcome domains (tech resources, non-tech resources, parental time investment, parental economic investment, learning) with multiple individual outcomes within each domain. The paper reports sharpened q-values within domains for the three main treatment coefficients, which is appropriate. However, the paper does not adjust for testing across domains or across the three treatment arms. With 3 treatments x 5+ domains, the family-wise error rate across the entire set of hypothesis tests is substantial. The headline 0.15 SD learning effect has p < 0.05 unadjusted and q-values of 0.079 and 0.137 -- the latter already above conventional thresholds after within-domain adjustment only.
- **Suggested fix:** Report a single omnibus test adjusting across all primary outcomes and treatment arms, or at minimum, be transparent about the total number of hypothesis tests conducted and the expected number of false positives.

#### B2. Statistical power for learning outcomes
- **Severity: CRITICAL**
- **Location:** Section 3 (Empirical specification), Section 5
- **Concern:** The paper reports being powered to detect 0.18 SD for EdTech info vs. control on learning. The headline effect is 0.15 SD. This means the study is underpowered for its main learning result -- the MDE exceeds the observed effect size. The fact that the result is significant at 5% reflects sampling variability, but the point estimate is below the MDE, which raises the possibility that the significant result is an overestimate (winner's curse / Type M error). Furthermore, the IRT-based learning measure q-value (0.137) does not survive conventional MHT thresholds.
- **Suggested fix:** Acknowledge explicitly that the learning result is at the margin of statistical power. Discuss the possibility of upward bias due to winner's curse. Present the confidence intervals prominently to give readers a sense of the plausible range.

#### B3. Heterogeneity analyses are underpowered and drive the inequality narrative
- **Severity: CRITICAL**
- **Location:** Section 6 (Heterogeneity)
- **Concern:** The paper's inequality narrative -- that EdTech information benefits wealthy households and may widen gaps -- is based on subgroup analyses by median SES split. However: (1) The tests for differential effects between subgroups are generally not significant at conventional levels for most outcomes (the paper reports p-values from interaction tests, which are often large). (2) Splitting an already-underpowered learning sample in half means each subgroup has roughly half the power. (3) Finding a significant effect in one subgroup and a null in another does not establish differential effects -- the proper test is the interaction, which is often insignificant. The paper reports some interaction p-values but the narrative treats the subgroup pattern as established rather than suggestive.
- **Suggested fix:** Reframe the heterogeneity results as exploratory/suggestive. Emphasize the interaction tests (which are the correct test for differential effects) rather than contrasting within-subgroup significance. Acknowledge the severe power limitations for subgroup analyses.

#### B4. Lasso-selected covariates and researcher degrees of freedom
- **Severity: IMPORTANT**
- **Location:** Section 3 (Empirical Specification)
- **Concern:** The main specification uses lasso regression to select covariates. While this is a valid approach (citing Urminsky et al. 2016), it introduces researcher degrees of freedom: the lasso penalty parameter, the candidate covariate set, and whether the lasso is run separately for each outcome or jointly. The paper reports that alternative specifications (stratification-cell FE only) are in the appendix, which is good practice. However, the main results are presented with the lasso-selected covariates, and it is unclear whether the covariate set varies across outcomes. If different covariates are selected for different outcomes, this complicates interpretation.
- **Suggested fix:** State clearly whether the same covariate set is used across all outcomes or whether it varies. If it varies, discuss implications. Consider presenting the stratification-cell-FE-only results as the main specification, with lasso results as robustness.

#### B5. Pre-analysis plan submitted after data collection began
- **Severity: IMPORTANT**
- **Location:** Footnote in Section 1, PAP documentation
- **Concern:** The paper notes the PAP was "submitted after launching the first follow-up survey round, but the research team did not look at any results from that round before it was posted." While this statement is credible, a late-registered PAP provides weaker protection against specification searching. Several aspects of the current analysis appear to differ from the PAP (the empirical specification has been re-parameterized for readability, the conceptual framework has been removed, the Sangsad TV treatment is downgraded). Some outcomes described in the paper as "exploratory" (e.g., intensive-margin usage changes) seem central to the interpretation.
- **Suggested fix:** Include an explicit PAP concordance table showing: (1) each pre-specified hypothesis and whether it was confirmed; (2) any deviations from the PAP and their justification; (3) which results are pre-specified vs. exploratory.

---

### C. Measurement & Data

#### C1. Differential attrition in the learning assessment
- **Severity: CRITICAL**
- **Location:** Section 2.6 (Attrition), Section 5.1 (Robustness)
- **Concern:** The paper rejects the null of equal response rates across treatment arms at the 5% level for Round 2 and at the 1% level for learning assessments. This is a serious problem for the main learning result. The paper presents three robustness checks (investment results replicate in the LA sample, IPW, Behaghel trimming), all of which are reassuring but not definitive. IPW relies on selection-on-observables. The Behaghel trimming relies on the monotonicity assumption that treatment doesn't affect relative reluctance. Given that the headline result is at the boundary of significance and power, even modest compositional differences could generate or eliminate the effect.
- **Suggested fix:** Present Lee (2009) bounds to show whether the result survives under worst-case attrition. Report more detail on which treatment arms have higher/lower attrition and in which direction the bias would go under plausible scenarios.

#### C2. Self-reported outcomes and measurement error
- **Severity: IMPORTANT**
- **Location:** Sections 4-5
- **Concern:** All intermediate outcomes (learning resource usage, tutoring spending, parental time investment) are self-reported by parents. These are subject to social desirability bias, recall error, and potentially differential reporting by treatment status. Parents who received EdTech information may report differently about their educational investments even absent real changes. The paper discusses social desirability for EdTech usage but not for tutoring expenditure reporting. A parent who just received messages about educational technology might over-report tutoring spending to seem like a "good parent." The fact that effects fade after the intervention is consistent with either the salience story (reminders caused real but temporary behavior change) or a reporting story (reminders caused temporary reporting changes).
- **Suggested fix:** Acknowledge that the tutoring expenditure results could be affected by the same reporting biases discussed for EdTech usage. Discuss whether the intervention could have changed the salience of tutoring in parents' minds, leading to differential reporting.

#### C3. Phone-based learning assessment limitations
- **Severity: IMPORTANT**
- **Location:** Section 2.5, Section 5
- **Concern:** The math assessment consists of only 8 questions per student (out of a bank of 19), administered by phone with oral questions and multiple-choice answers. This introduces several concerns: (1) With 4 base questions per grade, the unadjusted score has very coarse resolution -- each question contributes 0.25 of the score, making it difficult to detect small effects reliably. (2) The IRT model is estimated on 8 items per student, which is below the recommended minimum of 10 items cited in the paper itself (Stone 1992). (3) Phone-based oral math assessment is an unusual modality and may measure phone-task familiarity as much as math ability. Students in treatment arms who received more phone contact may perform better simply due to familiarity with the phone assessment format.
- **Suggested fix:** Acknowledge the phone-familiarity confound explicitly, especially for the teacher support arm (which involved extensive phone interaction). Discuss the measurement properties of the 4-question base score more thoroughly.

#### C4. Non-representative sample limits external validity
- **Severity: MINOR**
- **Location:** Section 2.2 (Sample Selection)
- **Concern:** The sample requires smartphone ownership, which excludes a large share of Bangladeshi households. The paper acknowledges this and shows comparisons to MICS data. However, the three sampling frames (RDD, stipend recipients, platform users) create a heterogeneous sample that is neither nationally representative nor representative of any well-defined population. The stipend recipients are selected on income; the platform users are selected on tech engagement. Pooling these creates a sample with unusual characteristics that may not generalize.
- **Suggested fix:** Be more cautious about external validity claims. Consider whether effects differ across the three sampling frames as a robustness check (this would also be informative about generalizability).

---

### D. Methodology

#### D1. Complex randomization design complicates interpretation
- **Severity: IMPORTANT**
- **Location:** Section 2.4
- **Concern:** The randomization design involves cross-randomization of EdTech info (50/50), general info (50/50), data package (cross-randomized only with information recipients, with unequal probability across info types), and teacher support (randomized only within general info recipients, with expanded share due to take-up concerns). This creates a complex treatment assignment structure with unequal cell sizes and multiple interaction terms. The regression specification has 9 treatment-related coefficients. The paper's main tables report only 3, with the rest in the appendix. This approach is defensible but makes it difficult for the reader to assess whether the interaction terms are well-estimated and whether the main effects are robust to alternative specifications of the interaction structure.
- **Suggested fix:** Include a clear table showing the full factorial structure with cell sizes. Present sensitivity analyses using alternative specifications (e.g., fully saturated model, pairwise comparisons).

#### D2. Absence of a structural model weakens the mechanism story
- **Severity: MINOR**
- **Location:** Discussion section, commented-out framework in source
- **Concern:** The LaTeX source contains a fully developed conceptual framework (Section 2, "Conceptual Framework") that has been commented out. This framework formalized the household optimization problem with perceived vs. actual returns to EdTech, complementarity between inputs, and heterogeneity by parental skill. Without this framework, the mechanism discussion relies on informal reasoning. Including a formal model -- even in the appendix -- would discipline the claims about substitution vs. complementarity of inputs, perceived vs. actual returns, and the conditions under which information causes tutoring increases. Its absence makes the mechanism discussion somewhat ad hoc.
- **Suggested fix:** Consider including the conceptual framework in an appendix, or referencing it explicitly. At minimum, use the framework's structure to organize the discussion of mechanisms.

#### D3. Cost-effectiveness comparison is misleading
- **Severity: MINOR**
- **Location:** Discussion, "Cost Effectiveness" paragraph
- **Concern:** The paper reports a cost-effectiveness of "5.44 SD increase per $100 spent" for the EdTech information arm. This comparison is misleading for two reasons: (1) The paper's own analysis suggests the learning gains were driven by increased tutoring spending, which cost families an additional ~$2/week. The intervention cost ($2.77) excludes the private costs borne by families, making the cost-effectiveness calculation incomplete. (2) Comparing this to Angrist et al. (2022) at "0.89 SD per $100" is misleading if the latter's intervention did not induce additional family spending. Apples-to-apples comparison requires including all costs -- both program and family -- or at minimum flagging this difference prominently.
- **Suggested fix:** Include household tutoring costs in the cost-effectiveness calculation, or clearly flag that the $2.77 figure excludes induced private expenditures. Adjust the cross-study comparison accordingly.

---

### E. Presentation & Framing

#### E1. Paper length and commented-out material
- **Severity: MINOR**
- **Location:** Throughout
- **Concern:** The LaTeX source contains enormous amounts of commented-out text -- alternative abstracts, prior versions of paragraphs, detailed gender heterogeneity analyses, extended results discussions. While comments don't appear in the compiled paper, the resulting document is still very long and repetitive. The introduction repeats the results in detail (multiple paragraphs), the results sections repeat findings across subsections, and the discussion re-summarizes everything. For a paper targeting a top field journal (JDE, EJ, JEBO), tightening the exposition would strengthen the contribution.
- **Suggested fix:** Reduce the introduction results preview to one paragraph. Move more discussion of individual coefficients to the appendix. Cut roughly 20-30% of the main text.

#### E2. Framing emphasizes the most fragile result
- **Severity: MINOR**
- **Location:** Abstract, Introduction, Conclusion
- **Concern:** The paper's headline framing centers on the 0.15 SD learning gain from EdTech information mediated through tutoring. But this is arguably the paper's most fragile finding: it is at the margin of power, the mediation is not identified, the MHT-adjusted q-value for IRT scores (0.137) does not survive conventional thresholds, and it depends on a subgroup (wealthy households) to fit the narrative. The more robust and well-powered findings -- that interventions shift parental investments, that teacher support substitutes for in-person teachers, that information decreases tech-resource usage -- receive less emphasis. An alternative framing that centers on the parental investment responses (which are better-powered and more novel) with learning as a secondary outcome would be on stronger empirical ground.
- **Suggested fix:** Consider reframing the paper around the parental investment results as the primary contribution, with learning outcomes presented as secondary/exploratory evidence of downstream effects.

#### E3. "May have widened inequalities" claim not supported by the data
- **Severity: MINOR**
- **Location:** Section 6 (Heterogeneity), Conclusion
- **Concern:** The paper claims that EdTech information "may have unintentionally widened educational inequalities." This requires showing that wealthy students gained AND poor students were harmed. The evidence shows the former (0.21 SD for wealthy, significant) but not the latter (near-zero for poor, not significant). No change for poor students is not widening inequality -- it is differential benefit. "Widening inequality" requires either absolute harm to poorer students or a pre-existing gap growing larger. The paper does not formally test whether the SES achievement gap widened. This is an important distinction for policy implications.
- **Suggested fix:** Use "differential benefit" rather than "widened inequality" unless a formal test of the change in the SES gap is presented. Alternatively, compute the gap at baseline and endline and test whether it changed.

---

## Summary Table

| ID | Category | Issue | Severity |
|----|----------|-------|----------|
| A1 | Identification | Mediation claim (info->tutoring->learning) not identified | Critical |
| A2 | Identification | Non-tutoring channels not ruled out | Important |
| A3 | Identification | Teacher support comparison group not pure control | Important |
| A4 | Identification | Data package always bundled with information | Important |
| B1 | Statistical | No MHT adjustment across domains/treatments | Critical |
| B2 | Statistical | Main learning result below MDE | Critical |
| B3 | Statistical | Underpowered heterogeneity drives inequality narrative | Critical |
| B4 | Statistical | Lasso covariate selection and researcher degrees of freedom | Important |
| B5 | Statistical | PAP submitted after data collection began | Important |
| C1 | Measurement | Differential attrition in learning assessment (p<0.001) | Critical |
| C2 | Measurement | Self-reported outcomes subject to differential reporting | Important |
| C3 | Measurement | Phone-based 8-item math assessment limitations | Important |
| C4 | Measurement | Non-representative sample (smartphone owners) | Minor |
| D1 | Methodology | Complex randomization design hard to interpret | Important |
| D2 | Methodology | Removed conceptual framework weakens mechanism story | Minor |
| D3 | Methodology | Cost-effectiveness excludes induced private costs | Minor |
| E1 | Presentation | Paper too long, needs tightening | Minor |
| E2 | Presentation | Headline framing rests on the most fragile result | Minor |
| E3 | Presentation | "Widened inequality" claim overstated | Minor |

---

## Overall Assessment

The paper tackles an interesting and policy-relevant question about how parents respond to educational interventions and how those responses affect learning. The experimental design is creative, the descriptive analysis is informative, and the investment results are well-powered and plausible. The paper's main vulnerability is that its headline claim -- that EdTech information caused learning gains through increased tutoring -- rests on a chain of inference that is suggestive but not identified, measured with noisy instruments, at the edge of statistical power, and sensitive to attrition. A skeptical referee would find the investment results (Sections 4-5 through the parental response results) convincing but would push back hard on the learning-through-tutoring mediation story and the inequality framing. Reframing the paper around the well-powered parental investment findings, with the learning results presented as suggestive downstream evidence, would put the paper on much stronger ground.

---

*Generated by Claude (Opus 4.6) as an adversarial econometrics audit for the UVM Faculty AI Bootcamp demo. This simulates the `/econ-audit` skill.*
