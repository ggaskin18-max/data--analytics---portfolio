
# Vertex Healthcare Group | Employee Attrition Analysis

### Beyond the Headcount: Investigating Workforce Attrition Through SQL and Python

**Tools:** MySQL | Python | pandas | Matplotlib | Excel | GitHub  
**Dataset:** 1,470 Employee Records  
**Project Focus:** Workforce Analytics, Employee Attrition and Data-Driven Retention Strategies

---

## The Business Story: Employees Are Leaving, But Where Is the Problem?

**What happens when an organisation knows employees are leaving but doesn't know where retention efforts should begin?**

Imagine a healthcare organisation experiencing concerns about employee turnover.

Every departure has potential consequences. Teams may need to redistribute work, managers may struggle to maintain staffing levels, and the organisation must invest time and resources into replacing experienced employees.

At Vertex Healthcare Group, management wants to understand whether attrition is affecting the workforce evenly or whether particular departments and job roles deserve greater attention.

This presents an important analytical challenge.

**Is it enough to identify where the most employees are leaving, or should management also consider how many employees work in each group?**

To investigate this, I analysed 1,470 employee records using MySQL and Python.

The project began with a broad question about employee attrition but developed into a deeper investigation of the difference between **departure counts and attrition rates**.

That distinction became central to understanding the workforce and identifying where management should focus further investigation.

*Vertex Healthcare Group is a fictional organisation used for this portfolio case study.*

---

## 1. Understanding the Business Problem

The challenge facing Vertex Healthcare Group is not simply employee turnover itself. It is the lack of clear evidence about where departures are concentrated and which employee groups may be experiencing comparatively high attrition.

Without this information, management risks implementing broad retention programmes without understanding where they are most needed.

I therefore structured the investigation around five questions:

- What is the overall proportion of employees who have left?
- Which departments account for the most departures?
- Do the departments with the most departures also have the highest attrition rates?
- Which job roles experience the greatest number and proportion of departures?
- What workforce areas should management prioritise for further investigation?

The objective was to generate insights that could support more focused workforce planning and retention strategies.

---

## 2. The Analytical Approach

Rather than relying on one analytical tool, I used a structured workflow to investigate, validate and communicate the findings.

### Stage 1 — Data Preparation and SQL Investigation

I began by preparing and reviewing the employee dataset before conducting SQL analysis in MySQL.

Using aggregation, grouping and filtering, I investigated attrition across departments, job roles and employee demographic groups.

This allowed me to identify where employee departures were most concentrated.

However, an important limitation emerged.

**The number of employees leaving a department does not necessarily indicate how likely employees in that department are to leave.**

Larger departments may naturally record more departures because they employ more people.

This observation informed the next stage of my analysis.

### Stage 2 — Python Validation and Deeper Analysis

To validate the SQL findings and investigate attrition more meaningfully, I used Python and pandas to reproduce key calculations.

I verified the dataset contained:

| Employee Status | Count |
|---|---:|
| Employees who left | 237 |
| Employees who stayed | 1,233 |
| Total employees | 1,470 |
| Overall attrition proportion | 16.12% |

I then calculated both departure counts and group-specific attrition rates.

The purpose was to distinguish between:

**Attrition count:** The number of employees who left.

**Attrition rate:** The percentage of employees within a particular group who left.

This distinction helped prevent misleading comparisons between departments and job roles of different sizes.

### Stage 3 — Data Visualisation with Matplotlib

I used Matplotlib to transform the Python results into visual comparisons.

The charts allowed me to examine how attrition patterns changed when I moved from absolute employee counts to percentages.

Rather than simply repeating the SQL analysis, Python provided an opportunity to validate the calculations and communicate the differences more clearly.

---

## 3. The Investigation: What Did the Data Reveal?

### Discovery 1 — The Overall Attrition Figure Was Only the Starting Point

The initial analysis identified 237 employee departures, representing **16.12% of the 1,470 employees**.

This provided an overview of the workforce, but it did not explain where departures were concentrated.

A company-wide figure can conceal significant differences between employee groups.

The next step was therefore to investigate the departments behind the overall result.

![Python Attrition Overview](image-1.png)

### Discovery 2 — Research & Development Recorded the Most Departures

My department-level analysis identified:

| Department | Employees Who Left |
|---|---:|
| Research & Development | 133 |
| Sales | 92 |
| Human Resources | 12 |

Research & Development accounted for the largest number of employees leaving.

At this stage, it could have been tempting to conclude that Research & Development was experiencing the greatest attrition challenge.

However, that conclusion would overlook an important factor: **department size**.

If Research & Development employs substantially more people than Human Resources, comparing departures alone may not provide a fair assessment.

I therefore extended the investigation to examine attrition rates.

![Department Departure Counts](python%20screenshot%205-1.png)

### Discovery 3 — The Departmental Attrition Rates Told a Different Story

Once the number of departures was compared with the total workforce in each department, the results changed.

| Department | Attrition Rate |
|---|---:|
| Sales | 20.63% |
| Human Resources | 19.05% |
| Research & Development | 13.84% |

Although Research & Development had the greatest number of departures, **Sales had the highest departmental attrition rate**.

This was one of the most important discoveries in the project.

The analysis showed that identifying the largest number of departures is not necessarily the same as identifying the group with the highest proportion of employees leaving.

**Business implication:** Management should consider both the operational impact of high departure counts and the relative attrition rates of different departments.

Research & Development may require attention because of the number of employees leaving, while Sales deserves investigation because of its comparatively higher attrition rate.

![Department Attrition Rate Comparison](image-3.png)

---

## 4. Drilling Down: Which Job Roles Require Attention?

Having identified differences between departments, I investigated whether particular job roles were contributing disproportionately to employee departures.

### Discovery 4 — Laboratory Technicians Recorded the Most Departures

The job-role analysis identified the following:

| Job Role | Employees Who Left |
|---|---:|
| Laboratory Technician | 62 |
| Sales Executive | 57 |
| Research Scientist | 47 |

Laboratory Technicians recorded the highest number of departures.

This finding suggested that further investigation of the role could be valuable, particularly given the potential operational consequences of losing employees in specialist positions.

However, the earlier departmental analysis had already demonstrated why departure counts should not be considered in isolation.

I therefore calculated attrition rates for individual job roles.

![Job Role Departure Counts](python%20screenshot%207-4.png)

### Discovery 5 — Sales Representatives Had the Highest Job-Role Attrition Rate

When I compared departures relative to the number of employees in each role, Sales Representatives emerged as the group with the highest reported attrition rate.

Based on the validated calculation of 33 departures among 83 Sales Representatives, the attrition rate was **39.76%**.

Laboratory Technicians had a lower attrition rate of approximately **22.22%**, despite recording more departures overall.

This created an important distinction:

**Laboratory Technicians accounted for the most departures, but Sales Representatives had the highest proportion of employees leaving.**

For management, these findings point to two different retention priorities.

Laboratory Technician departures may have a significant impact because of their volume, while the comparatively high attrition rate among Sales Representatives suggests the need for closer investigation of that role.

![Job Role Attrition Rates](image-7.png)

---

## 5. Translating the Findings into Business Decisions

The analysis identified patterns in employee departures, but it did not establish why employees left.

Factors such as workload, pay, career progression, leadership and employee satisfaction may be relevant. However, they would require additional evidence before being presented as causes.

With this in mind, I developed four recommendations.

### Recommendation 1 — Prioritise Sales for Retention Investigation

Sales recorded the highest departmental attrition rate at 20.63%.

Management should review employee feedback, exit interviews, workload and career development opportunities to identify potential contributing factors.

This would help determine whether the department requires targeted retention interventions.

### Recommendation 2 — Investigate Both High-Volume and High-Rate Job Roles

Laboratory Technicians recorded the highest number of departures, while Sales Representatives recorded the highest job-role attrition rate.

Both findings matter, but for different reasons.

I recommend prioritising these roles for further investigation, comparing their working conditions, employee experience and retention patterns.

### Recommendation 3 — Improve Workforce Monitoring

Management should monitor both departure counts and attrition rates rather than relying on a single organisation-wide figure.

Reporting should allow HR teams to compare departments and job roles while accounting for differences in workforce size.

This would support earlier identification of emerging retention concerns.

### Recommendation 4 — Evaluate Retention Initiatives Using Evidence

Potential retention measures could include career development opportunities, mentoring, employee engagement initiatives and reviews of rewards or working conditions.

However, interventions should be selected based on additional evidence and evaluated over time to determine whether they are associated with improvements.

---

## 6. Why Python Added Value to the SQL Analysis

One of the most valuable aspects of this project was the opportunity to validate and extend the initial SQL findings.

SQL helped identify where employee departures were concentrated.

Python and pandas allowed me to verify the calculations and compare attrition rates across groups of different sizes.

Matplotlib then made these differences easier to communicate.

The analysis demonstrated why working with counts alone can produce an incomplete picture of workforce attrition.

**Technical value:** The project combines SQL-based analysis, Python validation, calculated rates and data visualisation to investigate a business problem from multiple perspectives.

### Python Analysis Evidence

The following screenshot provides supporting evidence of the Python calculations and validation process.

![Python Validation Output](Screenshot%20python.png)

---

## 7. Project Limitations

The results should be interpreted within the limitations of the available dataset.

**Descriptive rather than causal analysis:** The findings identify where attrition occurred but do not establish why employees left.

**Workforce size differences:** Departure counts must be interpreted alongside group-specific attrition rates to avoid misleading comparisons.

**Time period:** The available analysis does not establish a verified annual turnover trend. The overall 16.12% figure describes the proportion of employees recorded as having left in the dataset.

**Fictional business context:** Vertex Healthcare Group is a fictional case study, and the data should not be represented as records from a real healthcare organisation.

These limitations help distinguish what the analysis demonstrates from questions requiring further investigation.

---

## 8. Technical Skills Demonstrated

| Skill | Application |
|---|---|
| SQL | Aggregation, grouping, filtering and workforce comparisons |
| Python | Data validation and exploratory analysis |
| pandas | Data manipulation, grouping and attrition calculations |
| Matplotlib | Visualisation of attrition counts and rates |
| Excel | Initial data preparation |
| Analytical Reasoning | Distinguishing absolute counts from relative rates |
| Business Communication | Translating findings into retention recommendations |

---

## 9. Final Reflection: What Did the Investigation Teach Me?

This project began with a question about employee turnover.

The initial findings showed that Research & Development had the largest number of departures.

However, the deeper analysis revealed that Sales had the highest departmental attrition rate.

A similar pattern emerged at job-role level: Laboratory Technicians recorded the most departures, while Sales Representatives had the highest reported rate.

These findings changed how the problem could be understood.

**The group losing the most employees is not necessarily the group with the greatest proportion of employees leaving.**

By combining SQL with Python validation and visualisation, I was able to investigate workforce attrition more carefully and identify different priorities for management attention.

The project demonstrates how data analysis can move beyond reporting figures to providing context, challenging initial assumptions and supporting better-informed business decisions.

### Final Takeaway

**Good workforce analysis is not just about knowing how many employees leave. It is about understanding where departures occur, how they compare across the workforce, and what further questions management needs to investigate.**

---

*Vertex Healthcare Group is a fictional organisation used for portfolio demonstration purposes.*