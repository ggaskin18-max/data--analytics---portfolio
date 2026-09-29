## Python analysis and validation

I used Python and pandas to check the cleaned employee dataset and validate the findings from my SQL analysis. The dataset contained 1,470 employee records: 237 employees had left and 1,233 had stayed, giving an overall attrition rate of 16.12%.

I then compared both departure counts and attrition rates across departments and job roles. Research & Development had the most departures (133), while Sales had the highest departmental attrition rate (20.63%). Laboratory Technicians had the most departures by job role (62), while Sales Representatives had the highest job-role attrition rate (39.76%, or 33 of 83 employees). Comparing rates as well as counts helped account for differences in group size.

The high attrition rate among Sales Representatives and the large number of Laboratory Technician departures give HR two clear priorities for follow-up. HR could review exit interviews, workload, pay and career progression in these roles to identify possible reasons for employees leaving before choosing targeted retention measures.

**Python evidence:** I used pandas to validate the 1,470-record dataset and calculate attrition counts and rates by department and job role. The output supports the findings discussed above.

![alt text](<Screenshot python.png>)

**Evidence 2 — Attrition by job role:** I used a pandas cross-tabulation to calculate the percentage of employees who left within each role. Sales Representatives had the highest attrition rate at 39.76% (33 of 83 employees).



