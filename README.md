# 🏡 Exploratory Data Analysis (EDA) on Housing Dataset

## 📌 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on a housing dataset (`housing.csv`).  
The main goal is to explore the dataset, clean missing values, analyze distributions, and identify relationships between features and the target variable (`Price`).

---

## 📂 Dataset
- **File:** `housing.csv`  
- **Features:** Includes numerical and categorical variables such as:
  - `LotArea` – Size of the property
  - `Bedrooms` – Number of bedrooms
  - `Bathrooms` – Number of bathrooms
  - `FurnishingStatus` – (Furnished, Semi-Furnished, Unfurnished)
  - `Price` – Target variable (House Price)

*(Column names may vary depending on your dataset.)*

---

## 🔎 Steps in EDA

### 1. Data Loading
- Loaded dataset using **Pandas** (`pd.read_csv()`).

### 2. Data Exploration
- Checked dataset structure, column names, and data types (`df.info()`).
- Displayed first rows (`df.head()`).
- Generated summary statistics (`df.describe()`).
- Counted missing values (`df.isnull().sum()`).

### 3. Data Cleaning
- Handled **missing values**:
  - Numeric columns → filled with **mean**.
  - Categorical columns → filled with **forward fill** or **mode**.
- Removed duplicate records (`df.drop_duplicates()`).
- Encoded categorical variables (one-hot encoding) if required.

### 4. Univariate Analysis
- Distribution plots for numerical features (histogram, boxplot).
- Frequency counts for categorical features (bar plots).

### 5. Bivariate Analysis
- Correlation heatmap for numerical features.
- Scatter plots (e.g., `Price` vs `LotArea`).
- Box plots to compare categorical features with `Price`.

### 6. Insights
- Identified strong correlations between some features and **Price**.
- Detected presence of outliers in numerical features.
- Observed differences in price distribution across furnishing categories.

---

## 📊 Visualizations
Some of the plots created:
- Histogram of **house prices**.
- Boxplot of **Price vs FurnishingStatus**.
- Correlation **heatmap** of numerical features.
- Scatter plot of **LotArea vs Price**.

---

## 🛠️ Technologies Used
- **Python 3**
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Advanced visualization

---

## 🚀 How to Run
1. Clone this repository or download the files.
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn

