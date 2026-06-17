"""
Generate audience_charts_teaching.png from the teaching webinar attendance/registration CSV.
PII guardrail: reads Name/Email columns but never prints or emits them.
Only aggregates are written to disk or printed to console.
Output: figures/audience_charts_teaching.png
Layout: 2x2 grid matching research webinar chart style.
"""

import collections
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

CSV_PATH = '/Users/ebeam/Downloads/TwA Webinar_ Agentic Tools for Teaching - Attendance report 6-15-26.csv'
OUT_PATH = 'figures/audience_charts_teaching.png'

SLATE    = '#1B4D5C'
GOLD     = '#D4A84B'
SAGE     = '#EDF2F0'
GRAY     = '#8899A6'
CORAL    = '#C0534D'
GREEN    = '#2E7D52'
LGOLD    = '#FDF6E3'
CHARCOAL = '#2C3E50'

# ── 1. Read non-PII columns ──────────────────────────────────────────────────
roles = []
countries = []
backgrounds = []
topics = []

with open(CSV_PATH, encoding='utf-16') as f:
    lines = f.readlines()

# Teams attendance report: header at line 12, data from line 13
# Cols: 0=Name,1=FirstJoin,...,6=Role,7=RegFirst,8=RegLast,9=RegEmail,
#        10=RegTime,11=RegStatus,12=Organization,13=Country/Region,
#        14=Role(survey),15=AI background,16=Topics
for line in lines[13:]:
    line = line.rstrip('\n')
    if not line.strip():
        continue
    parts = line.split('\t')
    if len(parts) < 12:
        continue
    status = parts[11].strip().lower() if len(parts) > 11 else ''
    if status not in ('approved', 'registered', ''):
        continue
    country = parts[13].strip().strip('"').strip() if len(parts) > 13 else ''
    role    = parts[14].strip() if len(parts) > 14 else ''
    bg      = parts[15].strip() if len(parts) > 15 else ''
    topic   = parts[16].strip() if len(parts) > 16 else ''
    if country:
        countries.append(country)
    if role:
        roles.append(role)
    if bg:
        backgrounds.append(bg)
    if topic:
        topics.append(topic)

print(f"Parsed {len(roles)} role, {len(countries)} country, {len(backgrounds)} bg, {len(topics)} topic entries")

# ── 2. Aggregate ─────────────────────────────────────────────────────────────

ROLE_MAP = {
    'faculty': 'Faculty',
    'professor': 'Faculty',
    'instructor': 'Faculty',
    'postdoc': 'Researcher (post-doc,\nresearch staff, etc)',
    'researcher': 'Researcher (post-doc,\nresearch staff, etc)',
    'research': 'Researcher (post-doc,\nresearch staff, etc)',
    'phd': 'PhD student',
    'graduate': 'PhD student',
    'grad student': 'PhD student',
    'pre-doc': 'Pre-doc/research assistant',
    'research assistant': 'Pre-doc/research assistant',
    'staff': 'Other',
    'administrator': 'Other',
    'other': 'Other',
    'student': "Master's student",
    'masters': "Master's student",
    'master': "Master's student",
    'undergraduate': "Master's student",
    'practitioner': 'Practitioner',
    'ngo': 'Practitioner',
    'policy': 'Practitioner',
}

def clean_role(r):
    rl = r.lower()
    for key, label in ROLE_MAP.items():
        if key in rl:
            return label
    return r[:35] if r else 'Other'

role_counts = collections.Counter(clean_role(r) for r in roles)

US_VARIANTS = {'usa', 'u.s.', 'u.s.a.', 'us', 'united states of america',
               'united states', 'america'}
def norm_country(c):
    c = c.strip().strip('"').strip("'").strip()
    if c.lower() in US_VARIANTS:
        return 'United States'
    return c

countries = [norm_country(c) for c in countries]
country_counts = collections.Counter(countries)
n_countries = len(country_counts)
top_n = 6
top_items = country_counts.most_common(top_n)
top_countries = dict(top_items)
other_count = sum(country_counts.values()) - sum(v for _, v in top_items)
if other_count > 0:
    top_countries['Other'] = other_count

# AI Background — 3 buckets matching research chart
BG_BUCKETS = [
    ('Beginner / new', [
        'no experience', 'no prior', 'never used', 'never tried', "haven't used",
        'have not used', "don't have", 'new to', 'just starting', 'just started',
        'none', 'nothing', 'zero', 'novice', 'complete beginner',
        'some experience', 'limited', 'minimal', 'little experience',
        'tried', 'experimenting', 'occasionally', 'beginner',
        'chatgpt a few', 'used it a few', 'little bit', 'played around',
        'dabbled', 'starting to', 'basic familiarity', 'basic',
    ]),
    ('Intermediate / regular user', [
        'moderate', 'intermediate', 'familiar', 'comfortable', 'regular',
        'regularly', 'frequently', 'often', 'use it for', 'use for',
        'use claude', 'use chatgpt', 'use ai', 'research workflow',
        'teaching workflow', 'part of my workflow', 'most days',
        'several times', 'routine', 'weekly', 'quite a bit',
    ]),
    ('Advanced / power user', [
        'extensive', 'advanced', 'daily', 'expert', 'heavy user',
        'proficient', 'deeply', 'every day', 'power user', 'claude code',
        'coding with', 'build with', 'develop', 'deploy', 'significant',
    ]),
]

def bucket_bg(text):
    tl = text.lower()
    for label, keywords in reversed(BG_BUCKETS):
        if any(k in tl for k in keywords):
            return label
    return 'Beginner / new'

bg_counts = collections.Counter(bucket_bg(b) for b in backgrounds)
for label, _ in BG_BUCKETS:
    if label not in bg_counts:
        bg_counts[label] = 0

# Topics — keyword buckets matching research chart style
TOPIC_BUCKETS = [
    ('Grading & feedback', ['grad', 'feedback', 'assess', 'rubric', 'essay', 'student work']),
    ('Course design & prep', ['course', 'curriculum', 'syllabus', 'lecture', 'design', 'prep', 'material']),
    ('Privacy & FERPA', ['privacy', 'ferpa', 'data', 'security', 'protect', 'student data']),
    ('Getting started & setup', ['start', 'setup', 'begin', 'intro', 'how to', 'getting started', 'first']),
    ('Coding & automation', ['code', 'coding', 'automat', 'script', 'programm', 'stata', 'python']),
    ('Best practices & tips', ['best practice', 'tip', 'effective', 'workflow', 'practical', 'example']),
]

def bucket_topics(text):
    tl = text.lower()
    matched = []
    for label, keywords in TOPIC_BUCKETS:
        if any(k in tl for k in keywords):
            matched.append(label)
    return matched if matched else ['Other']

topic_counts = collections.Counter()
for t in topics:
    for label in bucket_topics(t):
        topic_counts[label] += 1

print("Role counts:", dict(role_counts.most_common()))
print("Top countries:", top_countries)
print("Background:", dict(bg_counts))
print("Topics:", dict(topic_counts.most_common()))

# ── 3. Plot (2x2 layout matching research chart) ────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(12, 7))
fig.patch.set_facecolor('white')

def make_hbar(ax, labels, values, colors, title, fmt='n', total_for_pct=None):
    """fmt: 'n' = raw count, 'pct' = percentage only, 'both' = count + pct."""
    bars = ax.barh(labels, values, color=colors, height=0.55, zorder=2)
    ax.set_facecolor('white')
    ax.grid(axis='x', color=SAGE, linewidth=0.8, zorder=1)
    ax.set_title(title, fontsize=11, fontweight='bold', color=SLATE, pad=8,
                 loc='left')
    ax.tick_params(axis='y', labelsize=9, length=0)
    ax.tick_params(axis='x', labelsize=8)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for bar, val in zip(bars, values):
        if fmt == 'pct' and total_for_pct:
            pct = val / total_for_pct * 100
            label = f'{pct:.0f}%'
        elif fmt == 'both' and total_for_pct:
            pct = val / total_for_pct * 100
            label = f'{val} ({pct:.0f}%)'
        else:
            label = str(val)
        ax.text(bar.get_width() + max(values) * 0.02,
                bar.get_y() + bar.get_height() / 2,
                label, va='center', ha='left', fontsize=8.5,
                fontweight='bold', color=CHARCOAL)
    ax.set_xlim(0, max(values) * 1.25)

# --- Panel 1 (top-left): Role ---
rc_sorted = sorted(role_counts.items(), key=lambda x: x[1])
labels_r = [k for k, v in rc_sorted]
values_r = [v for k, v in rc_sorted]
n_role = sum(values_r)
colors_r = [SLATE] * len(labels_r)
make_hbar(axes[0, 0], labels_r, values_r, colors_r,
          f'WHO REGISTERED — ROLE (N={n_role})', fmt='pct', total_for_pct=n_role)

# --- Panel 2 (top-right): AI Experience ---
bg_order = ['Beginner / new', 'Intermediate / regular user', 'Advanced / power user']
bg_colors = [GOLD, GOLD, GOLD]
bg_vals = [bg_counts.get(k, 0) for k in bg_order]
n_bg = sum(bg_vals)
make_hbar(axes[0, 1], bg_order, bg_vals, bg_colors,
          f'AI EXPERIENCE (N={n_bg}, APPROX.)', fmt='pct', total_for_pct=n_bg)

# --- Panel 3 (bottom-left): Topics Requested ---
tc_sorted = sorted(topic_counts.items(), key=lambda x: x[1])
if not tc_sorted:
    tc_sorted = [('(no responses)', 0)]
labels_t = [k for k, v in tc_sorted]
values_t = [v for k, v in tc_sorted]
n_topics = len(topics)
colors_t = [CORAL] * len(labels_t)
make_hbar(axes[1, 0], labels_t, values_t, colors_t,
          f'TOPICS REQUESTED (N={n_topics})', fmt='n')

# --- Panel 4 (bottom-right): Geography ---
cc_sorted = sorted(top_countries.items(), key=lambda x: x[1])
labels_c = [k for k, v in cc_sorted]
values_c = [v for k, v in cc_sorted]
n_geo = sum(country_counts.values())
colors_c = [SLATE if k != 'Other' else GRAY for k in labels_c]
make_hbar(axes[1, 1], labels_c, values_c, colors_c,
          f'GEOGRAPHY (N={n_geo}, {n_countries} COUNTRIES)', fmt='pct', total_for_pct=n_geo)

plt.tight_layout(pad=2.0)
plt.savefig(OUT_PATH, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Saved → {OUT_PATH}")
