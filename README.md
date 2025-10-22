## Algonive_mall_segmentation
# 🛍️ Mall Customer Segmentation using KMeans & Streamlit

Welcome to the **Mall Customer Segmentation** project! This is an end-to-end machine learning solution using **unsupervised learning** to cluster mall customers into meaningful segments — based on their age, income, and spending behavior.

To make it more interactive and beginner-friendly, a **Streamlit web app** is included so you can explore clusters in real-time!

---

## 🎯 Project Objectives

- 🎯 Segment customers into distinct behavioral groups
- 📊 Help businesses target marketing strategies more effectively
- 🌐 Provide an **interactive web app** for visual exploration
- 🧑‍💻 Make the project beginner-friendly, well-documented, and shareable

---

## 🧠 Workflow: What This Project Does

### 1. **Data Exploration**
- Load dataset from Kaggle
- Check for missing values, understand distributions
- Visualize basic trends using plots

### 2. **Feature Selection & Preprocessing**
- Focused on key features: `Annual Income` and `Spending Score`
- Standardized features using `StandardScaler` for balanced clustering

### 3. **KMeans Clustering**
- Applied **Elbow Method** to find optimal number of clusters
- Trained the **KMeans** algorithm and predicted clusters
- Assigned cluster labels to all customers

### 4. **Data Visualization**
- Visualized clusters using 2D scatter plots
- Used color coding and cluster centers for better interpretability

### 5. **Interactive Web App**
- Built a **Streamlit** app to:
  - Upload your own dataset
  - See clusters instantly
  - Explore spending patterns by segment

---

## 🧪 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Programming language |
| **Pandas & NumPy** | Data analysis and manipulation |
| **Matplotlib & Seaborn** | Data visualization |
| **Scikit-learn** | KMeans clustering and preprocessing |
| **Streamlit** | Web app for interactive visualization |

---

## 📂 Dataset Used

**Source**: [Kaggle - Mall Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial)

**Columns in dataset**:
- `CustomerID`
- `Gender`
- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`

---

## 🚀 How to Run This Project

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/Banubakode/mall-customer-segmentation.git
cd mall-customer-segmentation


