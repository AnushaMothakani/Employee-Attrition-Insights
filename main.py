import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hr_cleaned.csv")
print(df.shape)
print(df["attrition_flag"].value_counts())

print(df.columns.to_list())
print(df.dtypes)
print(df.isnull().sum())

df["annual_salary"] = df["monthly_income"] * 12
df["replacement_cost"] = df["annual_salary"] * 0.5

print("Annual_Salary:")
print(df["annual_salary"])
print("Replacement_Cost:")
print(df["replacement_cost"])

left = df[df["attrition_flag"] == 1]

total_cost = left["replacement_cost"].sum()
print(f"Total_attrition_cost:${total_cost:,}")

dept_cost = left.groupby("department")["replacement_cost"].sum().sort_values(ascending=False)
print("Department Wise Attrition Cost:")
print(dept_cost)
dept_cost.reset_index().to_csv("attrition_cost_by_dept", index=False)

# charts
dept = df.groupby("department")["attrition_flag"].mean() * 100
dept = dept.sort_values(ascending=False)

plt.figure(figsize=(8,5))
dept.plot(kind="bar", color="tomato", edgecolor="black")
plt.title("Attrition Rate by Department (%)")
plt.ylabel("Attrition Rate(%)")
plt.xlabel("Department")
plt.tight_layout()
plt.savefig("attrition_by_dept.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="attrition_flag", y="monthly_income", data=df, palette="Set2")
plt.xticks([0, 1], ["Stayed", "Left"])
plt.title("Monthly Income: Stayed vs Left")
plt.ylabel("Monthly Income ($)")
plt.tight_layout()
plt.savefig("salary_vs_attrition.png")
plt.show()

cols = ["attrition_flag", "monthly_income", "age",
        "years_at_company", "is_overtime",
        "work_life_balance", "job_satisfaction", "distance_from_home"]

plt.figure(figsize=(10, 7))
sns.heatmap(df[cols].corr(), annot=True, fmt=".2f", cmap="RdYlGn", center=0)
plt.title("Correlation Heatmap — What Drives Attrition")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

summary = df.groupby("department").agg(
    total_employees=("attrition_flag", "count"),
    employees_left=("attrition_flag", "sum"),
    attrition_rate=("attrition_flag", "mean")
).reset_index()

summary["attrition_rate"] = (summary["attrition_rate"] * 100).round(2)
summary.to_csv("attrition_summary.csv", index=False)
print(summary)
