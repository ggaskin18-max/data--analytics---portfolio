
# Nova Retail Group | Sales & Profitability Analysis

### Beyond the Numbers: When Strong Sales Don't Tell the Full Story

**An End-to-End Business Analytics Case Study | Google Sheets • MySQL • Power BI • DAX**

**Dataset:** 9,994 retail transactions | 2014–2017

---

## The Story Behind the Data

**A business can generate millions in revenue and still have a profitability problem. But how do you identify what's going wrong?**

Imagine managing a retail company with thousands of transactions, customers across multiple regions, and products ranging from furniture to technology and office supplies.

Sales are coming in. Customers are purchasing. Revenue continues to grow.

From a sales perspective, the business appears to be doing well.

But there is another side to the story.

Despite generating approximately **2.30 million in revenue**, Nova Retail Group recorded a total profit of **286,397.02**, representing an overall profit margin of **12.47%**.

This raised a question that became the foundation of my investigation:

**If the business is generating substantial revenue, why is the profit margin comparatively modest?**

Is the issue linked to product performance? Are discounts affecting profitability? Are certain regions generating sales without delivering corresponding profits?

Or is the business overlooking individual products that are consistently operating at a loss?

I approached this project with one goal: **to understand the story behind the numbers and identify where management could focus its efforts to improve profitability.**

*Nova Retail Group is a fictional retail company created for this portfolio case study using the historical Sample Superstore dataset.*

---

## Understanding the Business Challenge

The challenge wasn't simply to calculate revenue and profit. Those figures alone would not explain what was happening within the business.

A company could generate high sales in one category while making very little profit from it. A region could outperform another in revenue but underperform in profitability. Discounts might encourage sales activity without necessarily improving financial returns.

For management, these differences matter.

Without understanding them, the business could continue investing in products, markets or promotional strategies that contribute relatively little to overall profit.

**My task was to investigate where revenue was being generated, where profitability was being weakened, and which areas deserved closer attention.**

Rather than beginning with assumptions, I structured the analysis around the data.

---

## The Analytical Journey

### Chapter 1 — Building Trust in the Data

**Tool: Google Sheets**

Before asking the data to explain the business problem, I needed to establish whether the information was reliable.

I began with 9,994 retail transaction records and conducted data quality checks to identify missing values, duplicate records and potential inconsistencies in key financial variables.

I examined Sales, Profit and Discount, validated the transaction count and established baseline financial KPIs.

The initial analysis produced the following results:

| Financial Indicator | Result |
|---|---:|
| Total Revenue | 2,297,200.86 |
| Total Profit | 286,397.02 |
| Profit Margin | 12.47% |
| Transaction Records | 9,994 |

These figures established the starting point for the investigation.

More importantly, they provided a benchmark for validating the calculations I would later reproduce in Power BI.

**What I learned:** Before investigating a business problem, it is essential to establish confidence in the data and its underlying calculations.

### Chapter 2 — Looking Beyond Total Revenue

**Tool: MySQL**

With the initial financial position established, the next question was: **Where exactly is the business generating and losing money?**

I imported the dataset into MySQL and developed eight business-focused queries to investigate performance across categories, products, discounts, regions, customer segments and time.

The first significant discovery came from comparing revenue and profit across product categories.

Technology generated approximately **836K in revenue**, contributing **145K in profit** and achieving a 17.40% margin.

Furniture, however, generated approximately **742K in revenue** but contributed only **18K in profit**, resulting in a margin of just **2.49%**.

This was an important turning point in the analysis.

Furniture was attracting substantial sales, yet those sales were translating into very little profit compared with Technology.

The question was no longer whether Furniture was selling.

**It was why those sales were contributing so little to profitability.**

I explored this further by analysing sub-category performance.

Tables emerged as the largest loss-making sub-category, followed by Bookcases and Supplies.

These findings suggested that the company's financial challenges were not evenly distributed across its product portfolio.

Certain areas were performing well, while others were reducing overall profitability.

### Chapter 3 — Investigating the Discounting Question

**Tool: MySQL**

The next stage of the investigation focused on discounting.

Discounts are commonly used to attract customers and encourage purchases, but their financial impact needs to be evaluated.

I wanted to understand whether heavily discounted transactions were associated with weaker profitability.

The analysis revealed a striking contrast.

Transactions without discounts generated a **29.51% profit margin**.

However, several product groups receiving discounts of 50% or more recorded substantial losses.

For example, heavily discounted Binders transactions generated losses of approximately **38.5K**, while Machines recorded losses of approximately **27.2K**.

This raised an important commercial consideration:

**What is the value of generating additional sales if those sales fail to contribute positively to profit?**

Although the analysis could not establish that discounts caused increased purchasing or financial losses, it highlighted a relationship that management should investigate.

This finding reinforced the need to evaluate promotional strategies using profitability measures rather than sales activity alone.

### Chapter 4 — Exploring Differences Across Regions and Customers

**Tool: MySQL**

Having investigated products and discounting, I wanted to understand whether profitability challenges extended to the company's geographical markets and customer segments.

Regional analysis revealed that West achieved a **14.94% profit margin**, while Central recorded just **7.92%**.

Interestingly, Central generated more revenue than South but produced less profit.

This suggested that a region's sales performance did not necessarily reflect its contribution to profitability.

The customer analysis revealed a similar pattern.

Consumer customers generated the highest revenue and total profit, but their profit margin was only **11.55%**.

Home Office customers, despite generating less total revenue, achieved the highest margin at **14.03%**.

Together, these findings strengthened one recurring theme:

**The largest contributor to sales is not always the most profitable relative to revenue.**

For management, this means growth opportunities should be evaluated through both revenue and margin performance.

---

## Chapter 5 — Turning Analysis into an Interactive Business Dashboard

**Tool: Power BI and DAX**

By this point, the SQL investigation had identified several areas deserving management attention.

However, presenting findings through tables and queries alone would make it difficult for business stakeholders to explore the information.

I therefore developed a two-page Power BI dashboard to communicate the findings visually and support interactive analysis.

Using DAX, I created measures for Total Revenue, Total Profit and Profit Margin.

These measures allow financial indicators to respond dynamically when users select different categories, regions or customer segments.

### Dashboard 1 — Sales & Profitability Overview

The first dashboard focuses on understanding the company's overall financial performance and identifying profitability concerns across product categories, discounts and regions.

It combines financial KPI cards with visual comparisons of revenue, profit, product performance and regional outcomes.

![Sales and Profitability Overview](PowerBI/dashboard_overview.png)

**What the dashboard helps users understand:**

The business generates substantial revenue, but financial performance varies significantly across product groups and geographical markets.

By interacting with the dashboard, stakeholders can explore which areas contribute strongly to profitability and which require further investigation.

### Dashboard 2 — Customer & Product Insights

The second dashboard examines the relationship between customer segment performance and individual product profitability.

It also identifies the ten products generating the largest recorded losses.

![Customer and Product Insights](PowerBI/customer_product_insights.png)

**What the dashboard helps users understand:**

Revenue contribution and profitability are not interchangeable.

The dashboard highlights differences between customer segments and identifies specific loss-making products, helping management determine where further commercial review may be valuable.

---

## From Findings to Business Decisions

**The purpose of this project was not simply to identify problems, but to consider how the findings could inform better decisions.**

Based on the analysis, I identified four priority areas for management.

### 1. Reassess High-Risk Discounting Practices

The association between substantial discounts and negative profitability suggests a need to review promotional strategies.

I would recommend introducing minimum-margin checks, particularly for products frequently sold at discounts of 50% or more.

The objective would be to protect profitability while still allowing the business to use promotions strategically.

### 2. Investigate Loss-Making Products Before Making Commercial Decisions

Tables and selected high-value products generated substantial financial losses.

Rather than recommending their immediate removal, I would investigate product costs, pricing, discounts and transaction patterns to determine why these products underperform.

This would allow management to make evidence-based decisions about pricing adjustments, promotions and product assortment.

### 3. Examine the Drivers of Regional Underperformance

Central's comparatively low profit margin suggests that regional performance deserves closer investigation.

I would recommend comparing product mix, discounting patterns and sales composition across regions to identify factors that may explain the difference.

### 4. Prioritize Profitable Growth

The results consistently demonstrate that revenue growth alone is not enough to evaluate financial success.

Management should monitor revenue, profit and profit margin together, supported by product- and region-level reporting.

**The objective is not simply to sell more, but to generate sales that contribute meaningfully to profitability.**

---

## Technical Skills Demonstrated

Throughout this project, I applied different analytical tools at different stages of the investigation.

| Tool | How I Applied It |
|---|---|
| Google Sheets | Data cleaning, validation and baseline KPI calculations |
| MySQL | Business-focused queries, aggregation, grouping, filtering and profitability investigation |
| Power BI | Interactive dashboard development and financial reporting |
| DAX | Dynamic revenue, profit and margin calculations |
| GitHub | Project documentation and version-controlled portfolio presentation |

The workflow demonstrates my ability to progress from raw transactional data to structured analysis and business-focused reporting.

---

## Limitations and Analytical Considerations

This case study uses historical Sample Superstore data covering 2014–2017.

Nova Retail Group is a fictional business created for analytical demonstration, so the findings do not represent the current performance of a real company.

The dataset also does not provide a complete breakdown of business operating costs. Recorded profit figures should therefore not be interpreted as a fully audited measure of net business profitability.

Furthermore, although substantial discounts were associated with financial losses, the analysis does not establish a causal relationship between discounting and customer demand or profitability.

These considerations are important when interpreting the results and deciding what further analysis would be necessary.

---

## Final Reflection — What Did the Data Really Tell Us?

This project began with a business that appeared successful based on revenue alone.

But as the investigation progressed, a more complex picture emerged.

Some high-revenue categories delivered relatively little profit. Certain products generated losses. Heavy discounting was associated with weak financial outcomes, and profitability differed across customer segments and regions.

The analysis demonstrated that **business performance cannot be fully understood through revenue alone**.

The real value came from asking deeper questions, investigating the patterns behind the financial figures and identifying where management could focus its attention.

Through Google Sheets, SQL and Power BI, I was able to transform transactional data into a structured business investigation supported by interactive visual reporting.

### The Key Takeaway

**Generating revenue is important. Understanding how that revenue translates into profit is what makes the analysis commercially valuable.**

This project demonstrates my approach to data analytics: validate the information, investigate the business problem, question the findings, communicate the evidence and recommend practical next steps.

---

*Data source: Sample Superstore dataset. Nova Retail Group is a fictional business created for portfolio demonstration purposes.*