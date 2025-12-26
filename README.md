# Superstore Analysis 

This section of the group project focuses on **Correlation & Relationships, Outlier Analysis, and Categorical Data Analysis** using the Superstore dataset.  
It includes a notebook, supporting visuals, a written report, and presentation slides.

---

## 📖 Introduction
The goal of this analysis is to explore relationships between sales and profit, detect outliers in sales data, and examine categorical differences across product categories, customer segments, and regions.

---

## 📊 Components of My Work
- **Notebook:** `notebooks/Helen_analysis.ipynb`  
  - Correlation between Sales and Profit  
  - Outlier detection and interpretation  
  - Category, Segment, and Region analysis with cross-tabs and heatmaps  

- **Visuals:** `visuals/`  
  - Correlation heatmap  
  - Outlier boxplot  
  - Category proportions bar chart  
  - Segment distribution bar chart  
  - Category vs Segment heatmap  
  - Category vs Region heatmap  

- **Report:** `report/Helen_report.docx`  
  - Detailed written explanation of methodology and findings  

- **Slides:** `slides/Helen_slides.pdf`  
  - Presentation-ready summary of the notebook analysis  

---

## ⚙️ Methodology
1. **Correlation Analysis**  
   - Examined relationship between Sales and Profit (r ≈ 0.48, moderate positive correlation).  
   - Visualized with a heatmap.  

2. **Outlier Detection**  
   - Used boxplots and IQR method to identify extreme values in Sales.  
   - Found 1,167 outliers, discussed trade-offs of handling them.  

3. **Categorical Analysis**  
   - Category proportions: Office Supplies dominate (60%), followed by Furniture (21%) and Technology (18%).  
   - Segment distribution: Consumer segment is largest (52%), followed by Corporate (30%) and Home Office (18%).  
   - Regional distribution: West and East regions lead in transactions.  
   - Cross-tab heatmaps reveal distinct purchasing patterns by segment and region.  

---

## 📈 Key Findings
- **Sales vs Profit:** Moderate positive correlation — higher sales generally lead to higher profit, but discounts distort margins.  
- **Outliers:** Extreme sales values can bias averages; handling them improves model reliability.  
- **Categories:** Office Supplies drive most transactions, while Furniture and Technology vary by segment and region.  
- **Segments & Regions:** Consumer customers dominate, with regional differences suggesting tailored strategies.  

---

## ▶️ How to Run
From the project root:
```bash
jupyter notebook notebooks/Helen_analysis.ipynb

 Tools & Libraries
- Python 3.8+
- Pandas, NumPy, Seaborn, Matplotlib

📄 Outputs
- Cleaned dataset: data/superstore_analysis.csv
- Visualizations: PNG files in visuals/
- Report: DOCX file in report/
- Slides: PDF file in slides/

✅ Conclusion
This analysis provides actionable insights into sales drivers, customer segments, and regional demand.
By combining statistical methods, visualizations, and clear documentation, the work demonstrates a professional workflow for business analytics



