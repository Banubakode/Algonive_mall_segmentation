# Algonive_Mall_Segmentation  
🛍️ Mall Customer Segmentation using KMeans & Plotly Dash

Welcome to the **Mall Customer Segmentation** project! This end-to-end machine learning solution uses **KMeans clustering** to segment mall customers based on demographics and purchasing behavior, such as age, income, and spending score.

An **interactive Plotly Dash dashboard** is included for dynamic visualization of customer segments, helping businesses target marketing strategies and optimize customer engagement effectively.

---

## 🎯 Project Objectives

- Segment customers into meaningful groups using unsupervised learning  
- Provide actionable insights for personalized marketing campaigns  
- Develop an interactive dashboard for real-time exploration of customer segments  
- Deliver a beginner-friendly, well-documented, and reusable project

---

## 🧠 Workflow Overview

1. **Data Cleaning & Preprocessing**  
   - Load and clean the dataset  
   - Handle missing values and normalize features for better clustering  

2. **Exploratory Data Analysis (EDA)**  
   - Visualize key features such as Age, Annual Income, and Spending Score  
   - Understand underlying patterns and distributions  

3. **KMeans Clustering**  
   - Use the Elbow Method to determine the optimal number of clusters  
   - Apply KMeans algorithm and assign cluster labels to customers  

4. **Feature Engineering**  
   - Prepare and transform data to improve clustering results  

5. **Interactive Dashboard with Plotly Dash**  
   - Create scatter plots and pie charts to visualize clusters  
   - Summarize cluster profiles in tabular format  
   - Enable interactive exploration of customer segments

---

## 🧪 Tech Stack

| Tool             | Purpose                          |
|------------------|---------------------------------|
| Python           | Programming language             |
| Pandas           | Data manipulation and analysis  |
| Scikit-learn     | Clustering and preprocessing    |
| Plotly & Dash    | Interactive data visualization  |

---

## 📂 Dataset

- **Source**: [Kaggle - Mall Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial)  
- **Key Columns**:  
  - `CustomerID`  
  - `Gender`  
  - `Age`  
  - `Annual Income (k$)`  
  - `Spending Score (1-100)`

---

## 🚀 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourGithubUsername/Algonive_Mall_Segmentation.git
   cd Algonive_Mall_Segmentation

   
## Install dependencies

pip install dash plotly pandas scikit-learn


## Prepare the dataset
Ensure that the processed dataset file customer_segments.csv (with cluster labels) is placed in the project directory.

## Run the Dash app
python app.py


## Open the dashboard
Navigate to http://127.0.0.1:8050/
 in your browser to explore the interactive customer segmentation dashboard.

## 📊 Results & Insights

1. Customers segmented into N distinct clusters based on their demographics and spending behavior

2. Visualization of clusters enables easy identification of high-value and low-value customer groups

3. Helps businesses create targeted marketing strategies and improve customer engagement

## 🔮 Future Enhancements

- Add filtering options in the dashboard (e.g., filter by cluster, age range)
- Deploy the dashboard to cloud platforms (Heroku, AWS, etc.) for public access
- Integrate recommendation engines based on customer segments
- Apply dimensionality reduction (PCA, t-SNE) for enhanced visualization

## 📞 Contact
For any questions or collaboration opportunities, please reach out:
## Your Name — banubakodeankita@gmail.com

## Thank you for exploring the Algonive Mall Customer Segmentation project!
## Happy clustering! 🎉

