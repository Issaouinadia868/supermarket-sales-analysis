# Supermarket Sales Analysis — Project Report

## 1. Objective
The objective is to understand sales performance across product lines, cities, branches, dates, hours, and payment methods, then turn the findings into practical business recommendations.

## 2. Tools and methods
- Python and Pandas for data preparation and aggregation
- Matplotlib and Seaborn for visual exploration
- Group-by summaries, KPI calculations, time-based analysis, and a branch/product-line heatmap

## 3. Headline results
The initial analysis recorded the following results:

- Total sales: **322,966.75**
- Average transaction value: **322.97**
- Highest transaction: **1,042.65**
- Top product line: **Food and beverages**, 56,144.84
- Top city: **Naypyitaw**, 110,568.71
- Top branch: **C**, 110,568.71
- Top sales hour: **19:00**, 39,699.51
- Payment method counts: Ewallet 345, Cash 344, Credit card 311

These numbers should be rechecked by running the included script on the exact CSV file. Results may vary if the source dataset differs.

## 4. Findings
### Product lines
Food and beverages generated the highest total sales in the recorded summary. This is a useful starting point for inventory planning, but sales alone do not reveal profit margin or stock availability.

### Branch and city
Branch C and Naypyitaw led their respective totals in the recorded results. The project also compares each product line across branches to expose differences in local demand.

### Time
The hourly aggregation peaked at 19:00. Staffing and replenishment decisions should consider both sales value and transaction volume, not revenue alone.

### Payment
Ewallet and Cash were used at similar rates, with Credit card somewhat lower. Since the difference is small, multiple payment options should remain available.

## 5. Recommendations
1. Review stock availability for high-revenue product lines.
2. Tailor promotions and assortment by branch instead of applying identical actions everywhere.
3. Investigate lower-performing combinations using price, availability, and margin data.
4. Plan staffing around observed busy periods, then validate against transaction counts.
5. Track revenue, transaction count, average transaction value, and gross income together.

## 6. Limitations
This is descriptive analysis, not a causal study. Total sales are not the same as profit, and the dataset may not represent current demand. Further work could include gross-margin analysis, customer segmentation, and a dashboard.

## 7. Conclusion
The analysis demonstrates how transaction data can support retail decisions. Comparing product lines, branches, cities, and time periods reveals where revenue is concentrated and where additional investigation may be useful.
