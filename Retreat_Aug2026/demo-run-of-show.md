> **SUPERSEDED 2026-08-26 (v3 deck has no live step).** Kept in case the pipeline demo returns for the Nov webinar.

# Retreat demo — run of show (Thu 2026-08-27, ~3 min)

**Design:** pre-run everything this morning; run *one* deterministic step live. No agent on stage, no permission prompts, nothing that can stall.

## Before 1:00
- [ ] Terminal open in `~/Desktop/retreat-demo/` — font **≥ 24 pt**, light background (June feedback: nobody could read the terminal)
- [ ] Folder state = clean: `ls` shows only `downloads - economic delights/`, the 4 scripts, `rubric.yaml`, `_prerun/`. **No** `no-pii/`, `pii/`, `grades/`. If they exist: `rm -rf no-pii pii grades`
- [ ] Finder window of `downloads - economic delights/` ready (so the room sees the three fake-student folder names — the names ARE the point)
- [ ] Slides on the other screen; "Live: one step" divider is the cue

## Live (after the "Live: one step" divider)
1. Show the Finder window: *"This is what Brightspace gives me. The student names are in the folder titles — before I open a single file, listing this folder is already a disclosure."*
2. In terminal:
   ```
   python3 deidentify.py
   ```
   Expected output (~5 s):
   ```
   STU01: 1 file(s),  424 words, 0 identifier(s) scrubbed -> no-pii/STU01.txt
   STU02: 1 file(s),  456 words, 1 identifier(s) scrubbed -> no-pii/STU02.txt
   STU03: 1 file(s),  570 words, 0 identifier(s) scrubbed -> no-pii/STU03.txt
   De-identified 3 submissions -> no-pii/
   Crosswalk -> pii/crosswalk.json   (the only place the names live; the agent never opens it)
   ```
   Talking point on the "0 identifiers scrubbed": *"Two of these essays never mention the student's own name — the name was only in the folder. That's normal. The scrub is belt-and-suspenders; renaming the folder is the real work."*
3. `ls no-pii pii` — *"Left folder is what the agent gets. Right folder it never opens."*
4. Advance to "What the rest of the pipeline produced" and narrate the pre-run output. Don't run `grade.py` live (it calls `claude -p`, ~30–60 s per essay).

## If something breaks
- Pre-run outputs are in `_prerun/` (console transcript in `_prerun/console.txt`). `cp -R _prerun/no-pii _prerun/pii .` and carry on.
- Worst case: skip to the results slide. The slide stands on its own.

## Named cut
If Part 1 runs long: skip the live step entirely, go divider → results slide. Saves ~2 min.

## After
`rm -rf no-pii pii grades` to reset for the November webinar.
