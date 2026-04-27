# Bug Examples: AI Code Audit of a Replication Package

Source: bd-remote-ed (Bangladesh remote education RCT), ~8,000 lines of Stata across 8 scripts.
Found during a Claude-assisted code audit in March 2026.

---

## 1. The copy-paste typo (silent misspecification)

**What**: A missing-value flag variable was defined as `_c_child_work` instead of `_f_c_child_work` -- omitting the `_f_` prefix that marks it as a flag.

**Where**: Copy-pasted into 3 of 5 scripts that define `$flags` (`15_3_coeff_plots_2024Sep.do`, `Anderson q_lasso.do`, `Andersonq_eb_04June_2024.do`). The 4th script had it right, but the error propagated through copy-paste.

**Why it matters**: The control variable `_c_child_work` appeared twice in regressions -- once in `$controls`, once in `$flags` -- instead of including its missing indicator. Regressions were technically misspecified.

**How AI found it**: Cross-file pattern matching. AI compared the `$flags` definition across all 5 scripts and spotted the inconsistency on the last entry of a 17-variable list.

**The fix**: `_c_child_work` --> `_f_c_child_work` (and centralize into a single `_globals.do` include file so it can never diverge again).

---

## 2. The missing gate (wasted compute)

**What**: A 250-line data-loading block ran unconditionally, even when a `gendata=0` flag was set to skip it and use cached data.

**Where**: `06_lasso_2024_apr09.do`, lines 114-380. The parallel script (`12_lasso_2022_version1.do`) had the block correctly wrapped in `if ${gendata} == 1 { }`.

**Why it matters**: Every time someone re-ran the lasso analysis using cached results, it still reloaded and re-prepped the full dataset -- wasting minutes of compute and risking errors if the source data file was missing.

**How AI found it**: Structural comparison of the two forked lasso scripts. AI diffed their control flow and noticed one had the `if` gate and the other didn't.

**The fix**: Wrap lines 114-380 in `if ${gendata} == 1 { ... }`, matching the sister script.

---

## 3. The version-specific crash (putexcel syntax)

**What**: `putexcel A1 = "`var'"` worked in Stata 16 but crashes in Stata 17+, which requires parenthesized expressions.

**Where**: Both lasso scripts (`06_lasso_2024_apr09.do` and `12_lasso_2022_version1.do`), in the block that exports lasso-selected covariates to Excel.

**Why it matters**: Anyone running the replication package on Stata 17 or 18 would get a hard crash mid-pipeline, with no obvious explanation. The error message doesn't clearly point to the syntax change.

**How AI found it**: Code review against Stata version compatibility rules. AI flagged the unparenthesized `putexcel` expression as incompatible with the current Stata version.

**The fix**: `putexcel A1 = "`var'"` --> `putexcel A1 = ("`var'")`

---

## 4. The 17-item list with one wrong entry (copy-paste drift)

**What**: The `$flags` variable list was defined independently in 5+ scripts instead of being sourced from a single file. Over time, the copies drifted apart.

**Where**: `18_cleaned_tables_het_Mar26.do` (correct), `15_3_coeff_plots_2024Sep.do` (wrong), `Anderson q_lasso.do` (wrong), `Andersonq_eb_04June_2024.do` (wrong), plus 10+ archived script versions -- all with the same error.

**Why it matters**: This is the same bug as #1, but the structural lesson is different: the error survived in 10+ archived versions spanning 2+ years of active development. No human reviewer caught it because the variable lists are long, visually similar, and the wrong version "looks right."

**How AI found it**: AI scanned every `global flags` definition in the repo (including 89 archived scripts) and flagged the inconsistency. A human would need to compare 17 variables across 15+ files character by character.

**Structural fix**: Extract shared definitions to a single `_globals.do` include file. Scripts source the file instead of copy-pasting the definition. One source of truth, zero drift.

---

## Key takeaway

These are not exotic bugs. They are the ordinary, invisible errors that accumulate in any research codebase: a missing prefix in a long variable list, an `if` block that wraps 15 of 16 sections, a syntax rule that changed between software versions. AI finds them because it reads every line of every file without fatigue, and cross-references patterns that humans skip over.
