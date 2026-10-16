# Supermarket Sales Analysis 📊
### Turning retail transactions into actionable business insights

A portfolio-ready data analytics project using Python, Pandas, Matplotlib, and Seaborn to explore supermarket sales performance across product lines, branches, cities, payment methods, and time.

> **Project status:** Analysis code and portfolio documentation are included. The raw dataset is not bundled; add the dataset file locally before running the analysis.

## Project highlights

- Clean and validate transaction data
- Calculate key business KPIs
- Compare revenue by product line, branch, and city
- Explore daily and hourly sales patterns
- Analyze customer payment preferences
- Generate clear, presentation-ready charts
- Translate findings into business recommendations

## Business questions

1. Which product lines generate the most revenue?
2. Which branch and city perform best by total sales?
3. When are sales strongest during the day?
4. Which payment methods are most frequently used?
5. What practical actions could improve sales and inventory planning?

## Key findings from the analysis

The figures below are based on the results recorded during the analysis. Re-run the project against your dataset to reproduce and verify them.

| KPI | Result |
|---|---:|
| Total sales | 322,966.75 |
| Average transaction value | 322.97 |
| Highest single transaction | 1,042.65 |
| Highest-revenue product line | Food and beverages — 56,144.84 |
| Highest-revenue city | Naypyitaw — 110,568.71 |
| Highest-revenue branch | C — 110,568.71 |
| Highest-revenue hour | 19:00 — 39,699.51 |
| Most-used payment method | Ewallet — 345 transactions (34.5%) |

### Interpretation

- **Food and beverages** is the top product line by revenue in the recorded results.
- **Naypyitaw** and **Branch C** lead the city and branch comparisons respectively.
- **19:00** is the strongest hour by sales in the recorded hourly aggregation.
- Payment methods are fairly balanced: Ewallet (34.5%), Cash (34.4%), and Credit card (31.1%).
- Product-line performance varies by branch, suggesting that stock and promotional plans should be adapted to local demand.

## Repository structure

```text
supermarket-sales-portfolio/
├── supermarket_sales_analysis.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
├── LINKEDIN_POST.md
├── REPORT.md
└── outputs/
    └── figures/       # Charts generated when the script runs
```

## Dataset

This project commonly uses the **Supermarket Sales** dataset with columns such as:

`Invoice ID`, `Branch`, `City`, `Customer type`, `Gender`, `Product line`, `Unit price`, `Quantity`, `Tax 5%`, `Total`, `Date`, `Time`, `Payment`, `cogs`, `gross margin percentage`, `gross income`, and `Rating`.

Download the dataset from the source provided by your course or from a reputable public dataset page. Save the CSV as:

```text
supermarket_sales.csv
```

Place it in the project root next to `supermarket_sales_analysis.py`.

## Run locally

```bash
# 1. Create and activate a virtual environment (optional but recommended)
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Put supermarket_sales.csv in this folder

# 4. Run the analysis
python supermarket_sales_analysis.py
```

The script prints KPI summaries and saves charts in `outputs/figures/`.

## Tools used

- **Python** — analysis workflow
- **Pandas** — cleaning, grouping, and KPI calculations
- **Matplotlib / Seaborn** — visualization
- **Git & GitHub** — version control and project presentation

## Example business recommendations

1. Protect availability of high-revenue product lines, especially Food and beverages.
2. Compare product-line performance branch by branch before allocating inventory.
3. Review the drivers of lower-performing categories instead of assuming that promotions alone will solve the issue.
4. Align staffing and replenishment with observed busy hours, while checking transaction counts as well as revenue.
5. Monitor KPIs monthly to distinguish persistent patterns from short-term variation.

## Limitations

- Revenue does not automatically equal profit.
- These results describe the observed dataset and do not prove why customers behave a certain way.
- Recommendations should be tested against margin, inventory, staffing, and customer-level information where available.
- Confirm all headline numbers by running the code on the exact dataset used for the project.

## Author

**Your Name**  
Aspiring Data Analyst | Python • SQL • Data Visualization

Replace this line with your LinkedIn profile and contact details before publishing.
