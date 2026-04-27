"""
Make a map of lead-releasing facilities in Vermont from TRI data.
Facilities plotted as points sized by cumulative total releases,
color-coded by active/inactive status. Vermont county boundaries shown.
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
import warnings
warnings.filterwarnings("ignore")

# ── Paths ────────────────────────────────────────────────────────────────
DATA = "/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/data/vt_lead_tri.csv"
OUT  = "/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/vt_lead_map.png"
SHAPEFILE_URL = "https://www2.census.gov/geo/tiger/TIGER2023/COUNTY/tl_2023_us_county.zip"

# ── Load and prepare facility-level data ─────────────────────────────────
df = pd.read_csv(DATA)

# Aggregate to facility level
fac = (
    df.groupby(["tri_facility_id", "facility_name", "city", "county",
                "latitude", "longitude"])
    .agg(
        cumulative=("total_releases", "sum"),
        first_year=("year", "min"),
        last_year=("year", "max"),
        n_years=("year", "nunique"),
    )
    .reset_index()
)

# Classify: still active if last report is 2020 or later
fac["status"] = np.where(fac["last_year"] >= 2020, "Active (reported 2020–24)", "Inactive")

# For sizing: use sqrt scale so area is proportional to releases
fac["marker_size"] = np.sqrt(fac["cumulative"]) * 1.2

print(f"Loaded {len(fac)} unique facilities")
print(f"  Active: {(fac['status'].str.startswith('Active')).sum()}")
print(f"  Inactive: {(fac['status'] == 'Inactive').sum()}")
print(f"  Cumulative releases range: {fac['cumulative'].min():,.0f} – {fac['cumulative'].max():,.0f} lbs")

# ── Load Vermont county boundaries ───────────────────────────────────────
print("Downloading county boundaries...")
try:
    counties_all = gpd.read_file(SHAPEFILE_URL)
    vt_counties = counties_all[counties_all["STATEFP"] == "50"].copy()
    vt_counties = vt_counties.to_crs(epsg=4326)
    has_counties = True
    print(f"  Loaded {len(vt_counties)} VT counties")
except Exception as e:
    print(f"  Could not load county boundaries: {e}")
    print("  Falling back to points-only map")
    has_counties = False

# ── Build the map ────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 12), facecolor="#f7f7f7")
ax.set_facecolor("#f0f4f0")

# Plot county boundaries
if has_counties:
    vt_counties.plot(
        ax=ax,
        facecolor="#e8ede8",
        edgecolor="#999999",
        linewidth=0.8,
    )
    # Label counties
    for _, row in vt_counties.iterrows():
        centroid = row.geometry.centroid
        ax.text(
            centroid.x, centroid.y,
            row["NAME"],
            fontsize=6.5,
            color="#777777",
            ha="center", va="center",
            fontstyle="italic",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")],
        )

# Color palette
colors = {
    "Active (reported 2020–24)": "#c62828",   # dark red
    "Inactive": "#546e7a",                      # blue-gray
}

# Plot facilities
for status, group in fac.groupby("status"):
    ax.scatter(
        group["longitude"],
        group["latitude"],
        s=group["marker_size"],
        c=colors[status],
        alpha=0.7,
        edgecolors="white",
        linewidths=0.6,
        label=status,
        zorder=5,
    )

# Label the top 5 facilities with manual offsets to avoid overlap
top5 = fac.nlargest(5, "cumulative")
label_config = {
    "ETHAN ALLEN FIRING RANGE": {
        "short": "Ethan Allen Firing Range",
        "dx": 0.30, "dy": 0.15,
    },
    "GLOBALFOUNDRIES": {
        "short": "GlobalFoundries",
        "dx": 0.30, "dy": -0.08,
    },
    "GE AEROSPACE PLANT 1": {
        "short": "GE Aerospace Plant 1",
        "dx": 0.20, "dy": 0.03,
    },
    "GE AEROSPACE PLANT 2": {
        "short": "GE Aerospace Plant 2",
        "dx": 0.20, "dy": -0.05,
    },
    "JOHNSON CONTROLS": {
        "short": "Johnson Controls",
        "dx": 0.18, "dy": -0.02,
    },
}

for _, row in top5.iterrows():
    name = row["facility_name"]
    # Find matching config
    cfg = None
    for key, val in label_config.items():
        if key in name:
            cfg = val
            break
    if cfg is None:
        cfg = {"short": name[:25], "dx": 0.15, "dy": 0.02}

    cumul_str = f"{row['cumulative']:,.0f} lbs"
    ax.annotate(
        f"{cfg['short']}\n({cumul_str})",
        xy=(row["longitude"], row["latitude"]),
        xytext=(row["longitude"] + cfg["dx"], row["latitude"] + cfg["dy"]),
        fontsize=7,
        color="#333333",
        fontweight="bold",
        arrowprops=dict(arrowstyle="-", color="#999999", lw=0.7),
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cccccc", alpha=0.9),
        zorder=10,
    )

# ── Legend ───────────────────────────────────────────────────────────────
# Status legend
status_handles = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=colors["Active (reported 2020–24)"],
           markersize=10, label="Active (reported 2020–24)", markeredgecolor="white"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=colors["Inactive"],
           markersize=10, label="Inactive (last report before 2020)", markeredgecolor="white"),
]

# Size legend
size_examples = [100, 1000, 10000, 100000]
size_handles = []
for val in size_examples:
    ms = np.sqrt(np.sqrt(val) * 1.2)  # approximate visual marker size
    size_handles.append(
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#aaaaaa",
               markersize=ms, label=f"{val:,.0f} lbs",
               markeredgecolor="white", markeredgewidth=0.5)
    )

leg1 = ax.legend(
    handles=status_handles,
    loc="lower left",
    fontsize=8,
    title="Facility Status",
    title_fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="#cccccc",
    framealpha=0.95,
)
ax.add_artist(leg1)

leg2 = ax.legend(
    handles=size_handles,
    loc="upper right",
    fontsize=7.5,
    title="Cumulative Releases\n(point size)",
    title_fontsize=8,
    frameon=True,
    facecolor="white",
    edgecolor="#cccccc",
    framealpha=0.95,
    labelspacing=1.2,
)

# ── Titles and styling ──────────────────────────────────────────────────
ax.set_title(
    "Lead Releases from TRI-Reporting Facilities in Vermont\n1987–2024",
    fontsize=14,
    fontweight="bold",
    color="#222222",
    pad=15,
)

ax.text(
    0.5, -0.02,
    "Source: EPA Toxics Release Inventory (TRI). Point size proportional to cumulative total releases (lbs).\n"
    "36 unique facilities reporting lead or lead compound releases across 14 industry sectors.",
    transform=ax.transAxes,
    fontsize=7.5,
    color="#666666",
    ha="center",
    va="top",
)

# Clean up axes
ax.set_xlabel("")
ax.set_ylabel("")
ax.tick_params(labelsize=7, colors="#888888")
for spine in ax.spines.values():
    spine.set_edgecolor("#cccccc")

# Set bounds to Vermont with some padding
if has_counties:
    bounds = vt_counties.total_bounds  # minx, miny, maxx, maxy
    pad_x = (bounds[2] - bounds[0]) * 0.08
    pad_y = (bounds[3] - bounds[1]) * 0.05
    ax.set_xlim(bounds[0] - pad_x, bounds[2] + pad_x)
    ax.set_ylim(bounds[1] - pad_y, bounds[3] + pad_y)

plt.tight_layout()
plt.savefig(OUT, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()

print(f"\nMap saved to: {OUT}")
