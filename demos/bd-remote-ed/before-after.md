# BD Remote Education: Before and After AI-Assisted Cleanup

## The Project

Bangladesh remote education RCT — evaluates TV instruction, adaptive edtech, data subsidies, and teacher support during COVID-era school closures. Collaborative project with an RA, accumulated code over 3+ years (2021-2024).

---

## BEFORE: The Original Project

**Location:** `Dropbox/a2i project/09_Analysis&Results/02_Do files/`

### By the numbers

- **51 do-files** scattered across 4 subdirectories
- **No master file that works** — `01_master_5th June 2021.do` was out of date by 3+ years
- **No config system** — hardcoded paths throughout every script
- **No documentation** — no README, no changelog, no audit trail
- **Not in version control** — everything lived in Dropbox with no git history

### The folder structure

```
02_Do files/
   01_master_5th June 2021.do        <-- master last touched June 2021
   02_datagen.do
   03_vargen_07sep.do                <-- which vargen is current?
   03_vargen.do                      <-- this one? or that one?
   04_outcome domains.do
   05_endline balance_eb.do          <-- "_eb" = Emily's version
   05_endline balance.do             <-- whose version is this?
   06_covariate_lasso.do
   07_outcome domains_heterog_gender_age.do
   07_outcome domains_heterog_genderXage.do
   09_attrition_8 July_e.do          <-- "_e" = Emily's edits
   09_attrition_8 July.do
   19_lee_bounds.do                  <-- added 2.5 years later
   balance tests.do
   scores.do
   ...
   Archive/
      02_datagen_2.do
      02_datagen_20June2021.do
      02_datagen_24june2021.do
      02_datagen_eb.do
      04_outcome domains copy.do
      04_outcome domains_07_01_pm.do
      04_outcome domains_eb_lns.do
      04_outcome domains_eb.do
      04_outcome domains_July12.do
      ... (18 files total)
   WB Submission Files/              <-- duplicated copies for World Bank
      (14 more files, mostly copies of the top-level ones)
   ado/
   Maps/
```

### The problems

1. **Which script is canonical?** Multiple versions of every key file (e.g., 7 variants of `04_outcome domains`)
2. **Date-in-filename versioning:** `_07sep`, `_02July1130am`, `_14 July`, `_July12`
3. **Author-in-filename versioning:** `_eb`, `_e`, `_eb_lns`
4. **No single entry point** — you had to know which scripts to run and in what order
5. **Duplicated submission folder** — 14 files copied into `WB Submission Files/` with no link to originals
6. **Hardcoded paths** — every script contained `/Users/ebeam/Dropbox/a2i project/...`

---

## AFTER: The Clean Repo

**Location:** `Github/bd-remote-ed/`

### By the numbers

- **8 canonical scripts** in the pipeline (+ 2 MHT helper scripts, 1 shared globals file)
- **86 old variants** safely moved to `Archive/` — nothing deleted
- **1 master do-file** (`00_master_repo.do`) with 7 phase switches
- **1 config template** (`config_local_template.do`) — zero hardcoded paths
- **1 justfile** — cross-platform task runner (`just run`, `just check`, `just setup`)
- **Full documentation** — README, audit memo, changelog, refactoring notes
- **Git version control** — 10 meaningful commits tracking every change

### The repo structure

```
bd-remote-ed/
   code/
      00_master_repo.do              <-- single entry point
      07_Dofiles_academic/
         _globals.do                 <-- shared macros
         02_datagen.do
         03_vargen.do                <-- THE vargen (one version)
         05_balance_04Jun24.do
         06_lasso_2024_apr09.do
         12_lasso_2022_version1.do
         15_3_coeff_plots_2024Sep.do
         18_cleaned_tables_het_Mar26.do
         create_de-identified_datasets.do
         MHT/
            Andersonq_eb_04June_2024.do
            Anderson q_lasso.do
            fdr_sharpened_qvalues.do
            fdr_sharpened_qvalues_edited.do
         Archive/                    <-- 86 old variants, preserved
         ado/                        <-- custom Stata programs
   config/
      config_local_template.do       <-- copy, edit paths, run
   docs/
      a2i_code_audit_2026-03-14.md
      CHANGELOG.md
      refactoring_audit_2026-03-21.md
      ...
   output/                           <-- gitignored, generated
      data/
      tables/
      figures/
   logs/
   justfile
   README.md
   .gitignore
```

### The master do-file (key excerpt)

```stata
* Switches — set to 0 to skip a stage
loc newvars     1  // Phase 1: build analysis datasets
loc lasso       1  // Phase 1b: lasso covariate selection
loc lasso_v1    1  // Phase 1c: lasso v1
loc tables      1  // Phase 2a: main regression tables
loc coefplots   1  // Phase 2b: coefficient plots
loc mht_eb      1  // Phase 2c: MHT q-values, EB spec
loc mht_lasso   1  // Phase 2c: MHT q-values, lasso spec
```

### The config system

```stata
* Copy this file to config_local.do and edit for your machine.
global repo_root "/Users/ebeam/Dropbox/GitHub/bd-remote-ed"
global remote_ed "/Users/ebeam/Dropbox/a2i project"
global raw_masterdata "${raw_root}/masterdata LONG.dta"
global dofiles "${repo_root}/code/07_Dofiles_academic"
global data_out "${output_root}/data"
global tables "${output_root}/tables"
```

### Running the pipeline

```bash
just setup    # create config_local.do from template
just run      # run the full 7-stage pipeline
just check    # verify all expected outputs exist
```

---

## The Transformation

| Dimension | Before | After |
|---|---|---|
| Do-files to consider | 51 across 4 folders | 8 canonical + clear Archive |
| Master file | Outdated (June 2021) | Current, 7 phase switches |
| Config system | None (hardcoded paths) | `config_local_template.do` |
| Path portability | Only runs on Emily's machine | Any collaborator, any machine |
| Version control | None (Dropbox) | Git, 10 commits |
| Documentation | None | README, audit memo, changelog |
| Task runner | None | justfile (cross-platform) |
| "Which version?" questions | Constant | Zero |
| Bugs found and fixed | Unknown | 4 (lasso grid failure, testparm crash, strata bug, VarClean duplication) |

## Time Investment

- **Session 1** (March 14): Code audit, initial import, master + config setup
- **Session 2** (March 21): Full pipeline build, refactoring, bug fixes, documentation
- **Total: ~2 Claude Code sessions (a few hours) vs. estimated days by hand**

## What AI Was Good At Here

- **Auditing 51 files** to determine which 8 were actually canonical
- **Tracing dependencies** across scripts to build the correct run order
- **Finding silent bugs** (e.g., lasso grid failures that produced empty results without error)
- **Mechanical refactoring** (extracting shared globals, wiring config, fixing path references)
- **Generating documentation** from the code itself (audit memo, README, changelog)
- **Not deleting anything** — all 86 old variants preserved in Archive, fully reversible
