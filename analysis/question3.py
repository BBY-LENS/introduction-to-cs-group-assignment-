import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Quick check: show first 5 rows
print(df.head())

# Compare sales between East and West regions
east_sales = df[df['Region'] == 'East']['Sales']
west_sales = df[df['Region'] == 'West']['Sales']

t_stat, p_val = stats.ttest_ind(east_sales, west_sales)
print("T-statistic:", t_stat)
print("P-value:", p_val)

if p_val < 0.05:
    print("Significant difference in average sales between East and West.")
else:
    print("No significant difference in average sales between East and West.")

# Visualization: average sales by region
avg_sales = df.groupby("Region")["Sales"].mean()
avg_sales.plot(kind="bar", title="Average Sales by Region")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig("region_sales.png")   # saves directly into analysis folder
plt.close()

# Average profit by customer segment
segment_profit = df.groupby("Segment")["Profit"].mean()
segment_profit.plot(kind="bar", title="Average Profit by Segment")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.savefig("segment_profit.png")
plt.close()

# Average discount by product category
category_discount = df.groupby("Category")["Discount"].mean()
category_discount.plot(kind="bar", title="Average Discount by Category")
plt.ylabel("Average Discount")
plt.tight_layout()
plt.savefig("category_discount.png")
plt.close()

# ANOVA: Sales by region
regions = [df[df['Region'] == r]['Sales'] for r in df['Region'].unique()]
f_stat, p_val = f_oneway(*regions)
print("ANOVA F-statistic:", f_stat)
print("ANOVA P-value:", p_val)

if p_val < 0.05:
    print("Significant differences in average sales across regions")
else:
    print("No significant differences in average sales across regions")

# Average profit by region
region_profit = df.groupby("Region")["Profit"].mean()
region_profit.plot(kind="bar", title="Average Profit by Region")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.savefig("region_profit.png")
plt.close()
