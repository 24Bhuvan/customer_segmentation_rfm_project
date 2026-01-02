# 📊 Customer Segmentation Using RFM Analysis

## 🔍 Project Overview

This project performs **end-to-end customer segmentation using RFM (Recency, Frequency, Monetary) analysis** to help businesses understand customer behavior and improve marketing decisions.

The pipeline processes raw transaction data, generates RFM metrics, segments customers, and produces business-ready insights and visualizations.

---

## 🎯 Business Objectives

- Identify high-value customers  
- Segment users based on purchase behavior  
- Analyze revenue contribution by segment  
- Support marketing and retention strategies  
- Deliver clean, business-ready reports  

---

## 🧠 Project Deliverables

- ✔ Cleaned transaction dataset  
- ✔ RFM metrics per customer  
- ✔ Customer segmentation (A / B / C)  
- ✔ Revenue analysis  
- ✔ Visualization charts  
- ✔ Business insights report  

---

## 📁 Project Structure

customer_segmentation_rfm_project/
│
├── data/
│ ├── raw/
│ │ └── transactions.csv
│ └── processed/
│ ├── cleaned_transactions.csv
│ └── rfm_table.csv
│
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ └── 02_rfm_analysis.ipynb
│
├── outputs/
│ ├── charts/
│ │ ├── recency_distribution.png
│ │ ├── frequency_distribution.png
│ │ ├── monetary_distribution.png
│ │ └── segment_counts.png
│ └── reports/
│ ├── rfm_insights.txt
│ └── marketing_campaign_report.pdf
│
├── src/
│ ├── init.py
│ ├── data_loading.py
│ ├── preprocessing.py
│ ├── rfm_calculation.py
│ ├── scoring.py
│ ├── segmentation.py
│ └── visualization.py
│
├── README.md
└── requirements.txt


---

## 🔄 Project Workflow

### 1️⃣ Data Loading
- Reads raw transaction data
- Converts date and numeric columns

**File:** `src/data_loading.py`

---

### 2️⃣ Data Cleaning
- Removes missing values
- Filters invalid transactions
- Removes duplicates

**File:** `src/preprocessing.py`

---

### 3️⃣ RFM Calculation
- **Recency:** Days since last purchase  
- **Frequency:** Number of orders  
- **Monetary:** Total spend  

**File:** `src/rfm_calculation.py`

---

### 4️⃣ RFM Scoring
- Percentile-based scoring (1–4)
- Higher score = higher customer value

**File:** `src/scoring.py`

---

### 5️⃣ Customer Segmentation

| Segment | Description |
|-------|-------------|
| A | High-value customers |
| B | Medium-value customers |
| C | Low-value / inactive customers |

**File:** `src/segmentation.py`

---

### 6️⃣ Visualization
Generated charts:
- Recency distribution  
- Frequency distribution  
- Monetary distribution  
- Segment count chart  

**File:** `src/visualization.py`

---

### 7️⃣ Business Insights Report
Generates a business-friendly report including:
- Segment distribution
- Revenue contribution
- Key insights

**Output:**
outputs/reports/rfm_insights.txt

---

## ▶️ How to Run the Project

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
Step 2: Run notebooks
notebooks/01_data_exploration.ipynb
notebooks/02_rfm_analysis.ipynb
OR run scripts
python src/data_loading.py
python src/preprocessing.py
python src/rfm_calculation.py
python src/scoring.py
python src/segmentation.py
python src/visualization.py
