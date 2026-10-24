## SQL Analysis – Investigating the Drivers of Profitability

### Overview

Following the data cleaning, validation and initial financial analysis conducted in Google Sheets, this stage uses MySQL to investigate the factors influencing Nova Retail Group's profitability.

The Google Sheets analysis validated **9,994 transaction records** and established three key performance indicators:

- **Total Revenue:** 2,297,200.86
- **Total Profit:** 286,397.02
- **Profit Margin:** 12.47%

While these findings provide an overview of the company's financial performance, they do not fully explain why profitability is relatively low compared with total sales.

### Role of SQL in the Analysis

SQL will be used to move beyond the initial KPIs and investigate the underlying drivers of business performance.

Through data aggregation, filtering, grouping and comparative analysis, SQL will help identify:

1. Which product categories and sub-categories generate the highest revenue and profit.
2. Which regions contribute most to profitability and which underperform.
3. How discounting affects profit margins.
4. Which customer segments generate the greatest value.
5. Which products consistently generate losses despite recording sales.

### Expected Outcome

The SQL analysis aims to uncover patterns and profitability challenges that are not immediately visible from the overall financial KPIs.

These findings will inform recommendations to improve pricing, discounting, product performance and regional profitability.

The results will also support further analysis in Python and the development of an interactive Power BI dashboard.