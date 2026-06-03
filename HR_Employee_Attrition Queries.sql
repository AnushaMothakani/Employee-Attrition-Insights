CREATE DATABASE hr_project;
USE hr_project;

SELECT COUNT(*) FROM hr_cleaned;

SHOW TABLES;

SELECT * FROM hr_cleaned LIMIT 5;

SELECT SUM(attrition_flag) FROM hr_cleaned;

SELECT department,
COUNT(*) AS total_employees,
SUM(attrition_flag) AS employees_left,
ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 2) AS attrition_pct
FROM hr_cleaned
GROUP BY department
ORDER BY attrition_pct DESC;

SELECT salary_band,
COUNT(*) AS total_employees,
SUM(attrition_flag) AS employees_left,
ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 2) AS attrition_pct
FROM hr_cleaned
GROUP BY salary_band
ORDER BY attrition_pct DESC;

SELECT is_overtime,
COUNT(*) AS total_employees,
SUM(attrition_flag) AS employees_left,
ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 2) AS attrition_pct
FROM hr_cleaned
GROUP BY is_overtime;

SELECT attrition_flag,
ROUND(AVG(monthly_income), 2) AS avg_salary,
ROUND(AVG(years_at_company), 2) AS avg_tenure,
ROUND(AVG(age), 2) AS avg_age,
ROUND(AVG(work_life_balance), 2) AS avg_wlb
FROM hr_cleaned
GROUP BY attrition_flag;

SELECT employee_number, 
department,
job_role, 
monthly_income,
years_at_company,
is_overtime,
work_life_balance,
job_satisfaction
FROM hr_cleaned
WHERE attrition_flag = 0
AND is_overtime = 1
AND monthly_income < 3000
AND work_life_balance <= 2
ORDER BY monthly_income ASC;
