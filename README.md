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
- Visualizations were generated using Python (`question3.py`) to make the comparisons clear.  
- All plots are stored in the `visuals/` folder for easy reference.

---

## 📊 Findings

- **Regional Comparison**: Sales and profit vary significantly across regions. Some regions generate higher revenue but lower profit margins, showing the impact of discounts and costs.  
- **Segment Comparison**: Customer segments differ in profitability. Certain segments contribute more consistently to profit, while others show volatility.  
- **Category Comparison**: Discounts applied to product categories influence overall profitability. High discounts may boost sales but reduce profit margins.

---

## 🖼️ Visuals

The following plots illustrate the comparative analysis:

### Regional Sales
![Region Sales](visuals/region_sales.png)

### Regional Profit
![Region Profit](visuals/region_profit.png)

### Segment Profit
![Segment Profit](visuals/segment_profit.png)

### Category Discount
![Category Discount](visuals/category_discount.png)

---

## ✅ Conclusion

The comparative analysis highlights important differences between groups in the dataset:
- Regions differ in both sales and profit.  
- Segments show unique profitability patterns.  
- Discounts drive sales but reduce margins.  

These insights help organizations refine pricing and marketing strategies to maximize profitability.

---

## ▶️ How to Run

From the project root:
```powershell
python analysis/question3.py

