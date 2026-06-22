# Run-of-Show — "AI as an Adversarial Reader"
**Webinar 1: AI for Research · Mon Jun 15 · Emily's segment (~18 min)**
Deck: `research_webinar_econ-audit.pdf` (11 slides) · You go first, Erkmen follows.

> Cue-card, not a script. For each slide: **⏱ time** · **🎯 the one thing to land** · talking beats · 🎬 any demo action. Total budget ~18 min — the AI-vs-referees table (S8) is the centerpiece; protect time for it.

---

### ⏱ 0:00 — S1 Title + S2 "What I'll Show You" · ~1.5 min
🎯 *One real paper, two uses of AI: audit the code, audit the paper.*
- Frame: this is **your** remote-ed paper you've been trying to publish — real, not a toy.
- The theme in one line: **AI as a fast, tireless adversarial reader of work you've already done. You stay the expert.**
- Tee up the split: Part 1 = the code, Part 2 = the paper.

---

## PART 1 — Auditing a Replication Package

### ⏱ 1:30 — S3 "Before: 3 Years of Accumulated Code" · ~2 min
🎯 *Everyone in the audience has a project that looks like this.*
- 51 do-files, 4 subdirectories, master file from June 2021, dates + initials in filenames, hardcoded paths.
- Land the relatability line: **"You probably have a project that looks exactly like this."**

### ⏱ 3:30 — S4 "After: One Clean, Reproducible Pipeline" · ~2 min
🎯 *51 → 8 do-files, full config + git + docs — and nothing deleted.*
- Walk the before/after table fast; don't read every row.
- Reassurance beat: **86 old variants preserved in Archive/ — fully reversible.**
- Cost line: **~2 Claude Code sessions vs. days by hand.**

### ⏱ 5:30 — S5 "The Bug It Found: A Typo Hiding in Plain Sight" · ~2.5 min  ⭐
🎯 *A one-character typo silently wrong for 2+ years — found by cross-referencing all 51 files.*
- `$flags` = 17 missing-value controls in **every regression**, defined in 5 scripts.
- The bug: 3 of 5 scripts dropped the `_f_` prefix → `_c_child_work` appeared **twice**, the real indicator left out.
- The punch: **no error, no crash — just quietly wrong across 10+ versions.** This is the slide that earns the whole talk.

---

## PART 2 — Auditing the Paper

### ⏱ 8:00 — S6 "What Is /econ-audit?" · ~2 min
🎯 *A reusable skill that reads your paper as a skeptical referee — in ~60 seconds.*
- Reads full paper (LaTeX, tables, appendix); checks identification, stats, measurement, methodology, presentation.
- Mention it's installable (`npx skills add eabeam/econ-skills --skill econ-audit`) — they can try it tonight.

### ⏱ 10:00 — S7 "Running It on the Paper: 5 Critical, 8 Important, 6 Minor" · ~2 min
🎯 *Concrete output: it found real, serious things.*
- 🎬 **DEMO DECISION — pick one before Monday:**
  - ☐ **Saved run** (what the slide says) — safest; just narrate the pinned output.
  - ☐ **Live** — only if you've tested it cold and have the saved output as fallback.
- Hit the 3 critical findings: mediation not identified (A1); no MHT + headline below MDE (B1–B3); differential attrition, Lee bounds (C1).
- The "pin the version" line is a nice honesty beat: *AI output varies between runs, so I reason about a fixed version.*

### ⏱ 12:00 — S8 "AI Audit vs. Real Referees: 7 of 10" · ~2.5 min  ⭐ CENTERPIECE
🎯 *AI matched most of what 11 real referee reports said — in 60 seconds vs. 4 years.*
- Don't read the table row by row. Land the **score: 5 full matches, 2 partial, 1 opposite, 2 misses.**
- Pick 2–3 vivid rows live (attrition + Lee bounds; noisy 8-item test; MHT/winner's curse).
- The contrast line: **11 referee reports, 8 journals, 4 years — vs. 60 seconds.**

### ⏱ 14:30 — S9 "What the AI Missed — And Why It Matters" · ~2 min
🎯 *The misses define the boundary: field knowledge, within-paper logic, publication strategy.*
- Short duration (needs field norms); the internal contradiction (data arm raised tutoring more, only info improved learning); COVID fatigue.
- The sharpest beat: **AI recommended *including* the model; every referee wanted it *cut*.** Sometimes it's exactly wrong.

### ⏱ 16:30 — S10 "Takeaway: A Very Good Pre-Submission Check" · ~1 min
🎯 *Replaces the first 80% of a careful discussant — in a minute, not a month.*
- Catches the systematic stuff (ID, power, MHT, attrition); doesn't replace field intuition or colleagues.
- **Code audit found bugs in 2 years of work — that alone justified it. Paper audit: run it before you submit. It's free.**

### ⏱ 17:30 — S11 "Try It — And Over to Erkmen" · ~1 min
🎯 *Two things to try tonight, then hand off.*
- Try: install `/econ-audit` on your next submission; point Claude at a messy project folder.
- Same principle both times: **AI does the mechanical reading; you keep the judgment.**
- 🎬 **Handoff line:** *"Next, Erkmen on using AI at the front end — to brainstorm and pressure-test research ideas before you've written anything."*

---

### Delivery reminders
- **Protect S5 and S8** — they're the two that earn the talk. If you're running long, trim S3/S4 narration, not these.
- One demo decision to make (S7): saved vs. live. Default to **saved** unless you've tested live cold.
- If Q&A is in 20/5 blocks, your natural pause points are after Part 1 (post-S5) and at the end.
