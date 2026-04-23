# Loan-Default-Prediction
Loan Default Risk Prediction using Machine Learning

## 📌 Overview
This project aims to predict whether a borrower will default on a loan using machine learning techniques. 
It uses financial and demographic features to classify loan status into default or non-default.

---

## 📊 Dataset
The dataset used in this project is not included due to size limitations.

🔗 Dataset Source: [https://www.kaggle.com/datasets/yasserh/loan-default-dataset]

To run this project:
1. Download the dataset from the above link
2. Place it inside the `data/` folder
3. Rename it as `loan_data_small.csv`

---

## ⚙️ Project Structure
Loan-Default-Prediction/
│
├── data/
│
├── notebooks/
│ ├── EDA.ipynb
│ ├── Modeling.ipynb
│
├── src/
│ ├── preprocess.py
│ ├── train.py
│ ├── evaluate.py
│
├── README.md

---

## 🔍 Exploratory Data Analysis (EDA)
- Checked missing values and data types
- Analyzed target variable distribution
- Visualized income and loan amount distributions
- Generated correlation heatmap

---

## 🤖 Model Used
- Logistic Regression (Baseline Model)
- Random Forest
- Gradient Boosting
- KNN
- Decision tree
- Naive Bayes

---

## 📈 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## 🚀 How to Run

1. Clone the repository:
  https://github.com/likhithabhupathi2006-alt/Loan-Default-Prediction.git

2. Install dependencies:
  
3. Run notebooks:
- Open `EDA.ipynb`
- Open `Modeling.ipynb`

---

## 👥 Team Members
- Bhupathi Likhitha
- Teena Thakan 
- Palak Srivastava

## Best Model
KNN is your best practical model

Why?
Best balance between:
Precision
Recall
F1-score (highest among realistic models)

## 📌 Key Insights
- Random Forest achieved perfect performance (Accuracy, F1, ROC-AUC = 1.0), which may indicate overfitting or potential data leakage.
- Gradient Boosting and Decision Tree also showed near-perfect performance, suggesting similar overfitting behavior.
- KNN provided a better balance between precision and recall compared to Logistic Regression and Naive Bayes.
- Logistic Regression achieved high precision but relatively low recall, meaning it misses many actual defaulters.
- Naive Bayes had the lowest F1 Score, indicating weaker overall performance.

## 📌Conclusion
Among all models, KNN provided the best balance between precision and recall, making it the most suitable for loan default prediction. Ensemble models like Random Forest and Gradient Boosting achieved near-perfect accuracy, but this indicates possible overfitting or data leakage, so their results were not considered reliable.
