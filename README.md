# 📊 Sales Data Analysis & Visualisation — Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-lightblue?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-teal)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A beginner-friendly Python project that analyses e-commerce sales data and produces **6 professional visualisation charts** using pandas, matplotlib, and seaborn.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Charts Generated](#charts-generated)
- [Key Insights](#key-insights)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Skills Demonstrated](#skills-demonstrated)

---

## Project Overview

This project loads a real-world-style sales CSV dataset from a Nepali e-commerce store (Jan–Jun 2024), performs data analysis using **pandas**, and generates 6 publication-quality charts using **matplotlib** and **seaborn**.

**Dataset Summary:**
| Metric | Value |
|--------|-------|
| Total Orders | 60 |
| Total Revenue | NPR 3,111,900 |
| Average Order Value | NPR 51,865 |
| Date Range | Jan 2024 – Jun 2024 |
| Products | 10 |
| Cities | 5 (Kathmandu, Pokhara, Biratnagar, Lalitpur, Chitwan) |

---

## Charts Generated

| # | Chart | Type | Purpose |
|---|-------|------|---------|
| 1 | Monthly Revenue Trend | Line Chart | Track revenue growth over time |
| 2 | Revenue by Category | Bar Chart | Compare category performance |
| 3 | Top 5 Products by Revenue | Horizontal Bar | Identify best sellers |
| 4 | Sales by City | Pie Chart | Geographic distribution |
| 5 | Payment Method Usage | Donut Chart | Preferred payment channels |
| 6 | Monthly Heatmap by Category | Heatmap | Spot seasonal patterns |

All charts are auto-saved in the `output_charts/` folder as `.png` files.

---

## Key Insights

- 📱 **Electronics dominates** — over 89% of total revenue comes from electronics
- 📈 **Revenue peaked in May 2024** — NPR 640,300 in a single month
- 💳 **Credit Card is the most popular** payment method
- 🏙️ **Kathmandu leads** in revenue among all cities
- 📚 **Books have the lowest revenue** but steady order volume

---

## Project Structure

```
sales-analysis/
│
├── data/
│   └── sales_data.csv          # Raw sales dataset (60 orders, Jan–Jun 2024)
│
├── output_charts/              # Auto-generated chart images
│   ├── 01_monthly_revenue.png
│   ├── 02_revenue_by_category.png
│   ├── 03_top_products.png
│   ├── 04_sales_by_city.png
│   ├── 05_payment_methods.png
│   └── 06_heatmap.png
│
├── analysis.py                 # Main analysis and visualisation script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/sales-data-analysis.git
cd sales-data-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis
python analysis.py
```

Charts will be saved automatically in the `output_charts/` folder and a summary report will print in the terminal.

---

## Skills Demonstrated

- **Data Loading & Cleaning** — `pandas` CSV loading, parsing dates, handling data types
- **Feature Engineering** — Deriving revenue, month, and period columns
- **Exploratory Data Analysis** — `groupby`, `agg`, `value_counts`, `sort_values`
- **Data Visualisation** — Line, bar, horizontal bar, pie, donut, and heatmap charts
- **Code Organisation** — Clean, well-commented, modular Python script
- **File Management** — Auto-creating output directories and saving figures

---

## Possible Extensions

- Add a Jupyter Notebook version with inline charts
- Build an interactive dashboard using `plotly` or `streamlit`
- Add forecasting using `scikit-learn` linear regression
- Connect to a live PostgreSQL database instead of CSV

---

*Part of a data analysis portfolio demonstrating Python data skills for professional and academic purposes.*
