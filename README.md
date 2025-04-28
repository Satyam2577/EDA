Titanic EDA Dashboard

This project performs an Exploratory Data Analysis (EDA) on the Titanic dataset using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.
It visualizes survival patterns based on features like Passenger Class, Sex, Age, Fare, and Embarkation Port.


📂 Dataset

The dataset used is train.csv, which typically contains:
Passenger details (age, sex, class, fare, etc.)
Survival information (1 = Survived, 0 = Did not survive)

🛠 Libraries Used

  Pandas: Data manipulation and analysis
  NumPy: Numerical operations
  Matplotlib: Data visualization
  Seaborn: Enhanced data visualization

Install dependencies using:
  pip install pandas numpy matplotlib seaborn

📈 Exploratory Steps

Data Loading
Read the Titanic training dataset using pd.read_csv('train.csv').
Initial Data Exploration
Display information about the dataset using .info().
Check for missing values.
Describe statistical properties with .describe().
Value counts for key features (Survived, Pclass, Sex, Embarked).


Visualization 1: Main Dashboard
  Survival Count: Bar plot showing the count of survivors and non-survivors.
  Passenger Class vs Survival: Bar plot showing survival distribution across passenger classes.
  Sex vs Survival: Bar plot showing survival distribution across sexes.
  Age vs Survival: Boxplot showing the distribution of age across survival status.
  Fare vs Survival: Boxplot showing fare distribution for survival status.
  Correlation Heatmap: Heatmap displaying correlations between numerical features.

Visualization 2: Additional Analysis
  Age Distribution: Histogram with KDE for passenger ages.
  Fare Distribution: Histogram with KDE for fares.
  Embarked vs Survival: Bar plot showing survival distribution across embarkation ports.
  Age vs Fare Scatterplot: Scatterplot of Age vs Fare colored by survival status.

📊 Output

Two full dashboards with multiple subplots highlighting different insights into the Titanic dataset.
High-level patterns in survival by demographics, socio-economic status, and location.

🎯 Key Insights (Examples)

Women had higher survival rates compared to men.
First-class passengers had a better chance of survival.
Younger passengers and those who paid higher fares showed a slight survival advantage.

📌 How to Run

Ensure train.csv is available in the same directory as the script.
Run the Python script:
  python code.py
