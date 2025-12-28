# introduction-to-cs-group-assignment-
# Comparative Analysis – Question 3

This part of the group assignment focuses on **Comparative Analysis** using the dataset `SampleSuperstore.csv`.  
The objective is to examine how different groups (regions, segments, and categories) compare in terms of sales, profit, and discount patterns.

---

## 📖 Introduction

Comparative analysis helps identify differences between groups in a dataset.  
By comparing regions, customer segments, and product categories, we can highlight which areas perform better and where challenges exist.  
This provides valuable insights for decision-making in marketing, pricing, and resource allocation.

---

## ⚙️ Methodology

- The dataset was grouped by **Region**, **Segment**, and **Category**.  
- Sales, profit, and discount values were aggregated for each group.  
- Statistical tests (t-test) were used to check differences in means.  
- Visualizations were generated using Python (`question3.py`) to make the comparisons clear.  
- All plots are stored in the `visuals/` folder for easy reference.

---

## 📊 Findings

### 3.1 Difference in Means (East vs West)

**Code used:**
```python
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv("data/SampleSuperstore.csv")

east_sales = df[df['Region'] == 'East']['Sales']
west_sales = df[df['Region'] == 'West']['Sales']

t_stat, p_val = stats.ttest_ind(east_sales, west_sales)
print("T-statistic:", t_stat)
print("P-value:", p_val)

if p_val < 0.05:
    print("Significant difference in average sales between East and West.")
else:
    print("No significant difference in average sales between East and West.")

# Visualization
avg_sales = df.groupby("Region")["Sales"].mean()
avg_sales.plot(kind="bar", title="Average Sales by Region")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig("analysis/visuals/region_sales.png")
plt.close()
Results:

T-statistic: 0.80

P-value: 0.42

Interpretation:  
The t-statistic measures how far apart the two group averages are compared to the variation in the data. A small value (like 0.80) means the groups are quite similar.
The p-value tells us the probability that the observed difference is just random chance. A p-value of 0.42 means there’s a 42% chance the difference is random — much higher than the usual 5% cutoff.
👉 In simple terms: East and West regions have similar average sales, and any small differences are not statistically meaningful.

**Visual:** ![Regional Sales](analysis/visuals/region_sales.png) ---

### 3.2 Comparison Across Groups
#### Regional Comparison:

Sales look similar across regions, but profits differ.

The West region earns the highest average profit, while Central earns the least.
👉 This shows that sales alone don’t guarantee profitability — discounts and costs matter.
**Visuals:** ![Regional Sales](analysis/visuals/region_sales.png) ![Regional Profit](analysis/visuals/region_profit.png)
Segment Comparison:
**Visual:** ![Segment Profit](analysis/visuals/segment_profit.png)
Home Office customers generate the highest average profit.

Consumer customers generate the lowest.
👉 Selling to home offices is more profitable, possibly due to bulk purchases or better margins.


Category Comparison:

Categories with higher discounts show lower profit margins.
**Visual:** ![Category Discount](analysis/visuals/category_discount.png) ---
👉 Discounts can boost sales volume but reduce profitability. Companies need to balance between attracting customers and keeping margins healthy.
✅ Conclusion
The comparative analysis highlights important differences between groups in the dataset:

Regions differ in both sales and profit.

Segments show unique profitability patterns.

Discounts drive sales but reduce margins.

Final takeaway:  
The statistical values (t-statistic and p-value) confirm whether differences are real or just random. In our case, East vs West sales differences are not significant. However, visual comparisons across regions, segments, and categories reveal meaningful business insights: profitability varies even when sales look similar, and discounts can erode margins.
## ▶️ How to Run From the project root: ```powershell python analysis/question3.py