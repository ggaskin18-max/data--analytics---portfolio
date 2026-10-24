
# Nova Retail Group — SQL Analysis Summary

## Overview

Following data cleaning and initial KPI analysis in Google Sheets, MySQL was used to investigate profitability across 9,994 retail transactions.

The analysis examined product performance, discounting, regional profitability, customer segments, loss-making products and annual financial trends.

## Key Business Findings

**1. Furniture is the weakest-performing category.**

Despite generating 741,999.80 in revenue, Furniture achieved a profit margin of just 2.49%, compared with 17.40% for Technology.

**2. Loss-making sub-categories reduce overall profitability.**

Tables recorded losses of 17,725.48, while Bookcases and Supplies also generated negative profits.

**3. Heavy discounting is associated with substantial losses.**

Transactions without discounts achieved a 29.51% profit margin. In contrast, transactions receiving discounts of 50–80% generated losses.

Binders recorded losses of 38,510.50 across 613 heavily discounted transactions.

**4. Central is the least profitable region.**

Central generated 501,239.89 in revenue but achieved a profit margin of only 7.92%, compared with 14.94% in the West.

**5. Higher customer spending does not always mean higher profitability.**

Consumer generated the highest revenue but had the lowest segment profit margin at 11.55%. Home Office achieved the highest margin at 14.03%.

**6. Individual products contribute significantly to losses.**

Several high-value products, particularly within Machines and Tables, recorded substantial losses alongside high average discounts.

**7. Revenue growth has not consistently improved profit margins.**

Annual profit increased between 2014 and 2017, but the profit margin declined from 13.43% in 2016 to 12.74% in 2017.

## Business Recommendations

1. **Review discounting policies:** Investigate heavily discounted products and introduce minimum-margin checks.
2. **Improve Furniture profitability:** Examine the pricing, costs and discounting of Tables and Bookcases.
3. **Address regional underperformance:** Investigate Central's product mix and pricing practices.
4. **Optimise customer segment strategies:** Identify opportunities to improve Consumer profitability while learning from the higher-margin Home Office segment.
5. **Monitor product-level losses:** Establish regular reporting to identify products generating persistent losses.
6. **Prioritise profitable growth:** Evaluate sales performance alongside profit margins rather than revenue alone.

## Conclusion

The SQL analysis demonstrates that Nova Retail Group's main challenge is not simply generating sales but converting revenue into sustainable profit.

The findings highlight several areas requiring management attention, particularly heavy discounting, loss-making products and regional profitability differences.

These insights will guide the next stage of the project, where Python will be used for further exploratory analysis and visualisation, followed by Power BI for interactive business reporting.