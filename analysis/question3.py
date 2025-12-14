import pandas as pd
import scipy.stats as stats

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
