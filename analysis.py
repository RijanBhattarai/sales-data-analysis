"""
============================================================
  Sales Data Analysis & Visualisation
  Author  : Rijan
  Tool    : Python (pandas, matplotlib, seaborn)
  Dataset : Nepali e-commerce sales (Jan–Jun 2024)
============================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

# ── Setup ─────────────────────────────────────────────────────
OUTPUT_DIR = "output_charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({"figure.dpi": 150, "font.family": "DejaVu Sans"})

BLUE = "#1F497D"
COLORS = ["#1F497D", "#2E86AB", "#A23B72", "#F18F01", "#C73E1D", "#3B1F2B"]

# ── Load Data ─────────────────────────────────────────────────
df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

# ── Feature Engineering ───────────────────────────────────────
df["revenue"] = df["quantity"] * df["unit_price"]
df["month"] = df["date"].dt.to_period("M").astype(str)
df["month_name"] = df["date"].dt.strftime("%b %Y")

# ─────────────────────────────────────────────────────────────
# SUMMARY STATISTICS
# ─────────────────────────────────────────────────────────────
print("=" * 55)
print("       SALES DATA ANALYSIS — SUMMARY REPORT")
print("=" * 55)
print(f"  Total Orders        : {len(df)}")
print(f"  Total Revenue       : NPR {df['revenue'].sum():,.0f}")
print(f"  Average Order Value : NPR {df['revenue'].mean():,.0f}")
print(
    f"  Date Range          : {df['date'].min().date()} → {df['date'].max().date()}")
print(f"  Products Tracked    : {df['product'].nunique()}")
print(f"  Cities              : {df['customer_city'].nunique()}")
print("=" * 55)

# ─────────────────────────────────────────────────────────────
# CHART 1 — Monthly Revenue Trend (Line Chart)
# ─────────────────────────────────────────────────────────────
monthly = (
    df.groupby("month")["revenue"]
    .sum()
    .reset_index()
    .sort_values("month")
)
monthly["month_label"] = pd.to_datetime(monthly["month"]).dt.strftime("%b %Y")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly["month_label"], monthly["revenue"],
        marker="o", linewidth=2.5, color=BLUE, markersize=8, markerfacecolor="white",
        markeredgewidth=2.5)
ax.fill_between(monthly["month_label"], monthly["revenue"],
                alpha=0.1, color=BLUE)

for x, y in zip(monthly["month_label"], monthly["revenue"]):
    ax.annotate(f"NPR {y/1000:.0f}K", (x, y),
                textcoords="offset points", xytext=(0, 10),
                ha="center", fontsize=9, color=BLUE)

ax.set_title("Monthly Revenue Trend (Jan–Jun 2024)",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Revenue (NPR)", fontsize=11)
ax.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"NPR {x/1000:.0f}K"))
ax.tick_params(axis="x", rotation=15)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_monthly_revenue.png")
plt.close()
print("  ✔ Chart 1 saved: Monthly Revenue Trend")

# ─────────────────────────────────────────────────────────────
# CHART 2 — Revenue by Category (Bar Chart)
# ─────────────────────────────────────────────────────────────
cat_rev = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(cat_rev["category"], cat_rev["revenue"],
              color=COLORS[:len(cat_rev)], edgecolor="white", linewidth=0.8)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5000,
            f"NPR {bar.get_height()/1000:.0f}K",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold")

ax.set_title("Total Revenue by Product Category",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Category", fontsize=11)
ax.set_ylabel("Revenue (NPR)", fontsize=11)
ax.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"NPR {x/1000:.0f}K"))
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_revenue_by_category.png")
plt.close()
print("  ✔ Chart 2 saved: Revenue by Category")

# ─────────────────────────────────────────────────────────────
# CHART 3 — Top 5 Products by Revenue (Horizontal Bar)
# ─────────────────────────────────────────────────────────────
top_products = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=True)
    .tail(5)
    .reset_index()
)

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(top_products["product"], top_products["revenue"],
               color=BLUE, edgecolor="white")

for bar in bars:
    ax.text(bar.get_width() + 3000, bar.get_y() + bar.get_height() / 2,
            f"NPR {bar.get_width()/1000:.0f}K",
            va="center", fontsize=9.5, fontweight="bold", color=BLUE)

ax.set_title("Top 5 Products by Total Revenue",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Revenue (NPR)", fontsize=11)
ax.xaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"NPR {x/1000:.0f}K"))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_top_products.png")
plt.close()
print("  ✔ Chart 3 saved: Top 5 Products")

# ─────────────────────────────────────────────────────────────
# CHART 4 — Sales by City (Pie Chart)
# ─────────────────────────────────────────────────────────────
city_rev = (
    df.groupby("customer_city")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    city_rev.values,
    labels=city_rev.index,
    autopct="%1.1f%%",
    colors=COLORS[:len(city_rev)],
    startangle=140,
    pctdistance=0.82,
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)
for at in autotexts:
    at.set_fontsize(9)
    at.set_fontweight("bold")

ax.set_title("Revenue Distribution by City",
             fontsize=14, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_sales_by_city.png")
plt.close()
print("  ✔ Chart 4 saved: Sales by City")

# ─────────────────────────────────────────────────────────────
# CHART 5 — Payment Method Usage (Donut Chart)
# ─────────────────────────────────────────────────────────────
pay_counts = df["payment_method"].value_counts()

fig, ax = plt.subplots(figsize=(7, 6))
wedges, texts, autotexts = ax.pie(
    pay_counts.values,
    labels=pay_counts.index,
    autopct="%1.1f%%",
    colors=COLORS[:len(pay_counts)],
    startangle=90,
    pctdistance=0.78,
    wedgeprops={"edgecolor": "white", "linewidth": 2, "width": 0.6}
)
for at in autotexts:
    at.set_fontsize(9)
    at.set_fontweight("bold")

ax.set_title("Payment Method Distribution",
             fontsize=14, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/05_payment_methods.png")
plt.close()
print("  ✔ Chart 5 saved: Payment Method Distribution")

# ─────────────────────────────────────────────────────────────
# CHART 6 — Monthly Sales Heatmap by Category
# ─────────────────────────────────────────────────────────────
heatmap_data = (
    df.groupby(["month", "category"])["revenue"]
    .sum()
    .unstack(fill_value=0)
)
heatmap_data.index = pd.to_datetime(heatmap_data.index).strftime("%b %Y")

fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(
    heatmap_data / 1000,
    annot=True,
    fmt=".0f",
    cmap="Blues",
    linewidths=0.5,
    ax=ax,
    cbar_kws={"label": "Revenue (NPR '000)"}
)
ax.set_title("Monthly Revenue Heatmap by Category (NPR '000)",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Category", fontsize=11)
ax.set_ylabel("Month", fontsize=11)
ax.tick_params(axis="x", rotation=20)
ax.tick_params(axis="y", rotation=0)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/06_heatmap.png")
plt.close()
print("  ✔ Chart 6 saved: Monthly Heatmap by Category")

# ─────────────────────────────────────────────────────────────
# DETAILED SUMMARY TABLE
# ─────────────────────────────────────────────────────────────
print()
print("── Revenue by Category ──────────────────────────────")
cat_table = df.groupby("category").agg(
    Orders=("order_id", "count"),
    Units_Sold=("quantity", "sum"),
    Total_Revenue=("revenue", "sum")
).sort_values("Total_Revenue", ascending=False)
cat_table["Total_Revenue"] = cat_table["Total_Revenue"].apply(
    lambda x: f"NPR {x:,.0f}")
print(cat_table.to_string())

print()
print("── Monthly Revenue Summary ──────────────────────────")
mon_table = df.groupby("month_name").agg(
    Orders=("order_id", "count"),
    Revenue=("revenue", "sum")
).reset_index()
mon_table["Revenue"] = mon_table["Revenue"].apply(lambda x: f"NPR {x:,.0f}")
print(mon_table.to_string(index=False))

print()
print(f"  All charts saved in '{OUTPUT_DIR}/' folder.")
print("=" * 55)
