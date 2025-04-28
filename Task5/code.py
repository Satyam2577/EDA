# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting visual styles
sns.set(style="whitegrid", palette="pastel")
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Load the data
train_df = pd.read_csv('train.csv')
print("Data Info:")
print(train_df.info())

print("\nMissing Values:")
print(train_df.isnull().sum())

print("\nBasic Description:")
print(train_df.describe())

print("\nValue Counts:")
print("Survived:\n", train_df['Survived'].value_counts())
print("Pclass:\n", train_df['Pclass'].value_counts())
print("Sex:\n", train_df['Sex'].value_counts())
print("Embarked:\n", train_df['Embarked'].value_counts())

fig, axes = plt.subplots(2, 3, figsize=(20, 12))

# 1. Survival Count
sns.countplot(ax=axes[0,0], data=train_df, x='Survived', hue='Survived', palette='Set2', legend=False)
axes[0,0].set_title('Survival Count')

# 2. Passenger Class vs Survival
sns.countplot(ax=axes[0,1], data=train_df, x='Pclass', hue='Survived', palette='Set1')
axes[0,1].set_title('Passenger Class vs Survival')

# 3. Sex vs Survival
sns.countplot(ax=axes[0,2], data=train_df, x='Sex', hue='Survived', palette='coolwarm')
axes[0,2].set_title('Sex vs Survival')

# 4. Boxplot: Age vs Survival
sns.boxplot(ax=axes[1,0], data=train_df, x='Survived', y='Age', palette='viridis')
axes[1,0].set_title('Age Distribution by Survival')

# 5. Boxplot: Fare vs Survival
sns.boxplot(ax=axes[1,1], data=train_df, x='Survived', y='Fare', palette='rocket')
axes[1,1].set_title('Fare Distribution by Survival')

# 6. Heatmap: Correlation Matrix
corr = train_df.select_dtypes(include=['number']).corr()
sns.heatmap(corr, ax=axes[1,2], annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, square=True)
axes[1,2].set_title('Feature Correlation')

# Layout adjustment
plt.tight_layout(pad=3.0, rect=[0, 0, 1, 0.95])  # Reserve space for suptitle
fig.suptitle('Titanic EDA Dashboard', fontsize=24)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(18, 10))

# 1. Age Distribution
sns.histplot(ax=axes[0,0], data=train_df, x='Age', bins=30, kde=True, color='skyblue')
axes[0,0].set_title('Age Distribution')

# 2. Fare Distribution
sns.histplot(ax=axes[0,1], data=train_df, x='Fare', bins=30, kde=True, color='lightgreen')
axes[0,1].set_title('Fare Distribution')

# 3. Embarked vs Survival
sns.countplot(ax=axes[1,0], data=train_df, x='Embarked', hue='Survived', palette='muted')
axes[1,0].set_title('Embarked vs Survival')

# 4. Scatterplot: Age vs Fare colored by Survival
sns.scatterplot(ax=axes[1,1], data=train_df, x='Age', y='Fare', hue='Survived', palette='deep')
axes[1,1].set_title('Age vs Fare (Colored by Survival)')

# Layout adjustment
plt.tight_layout(pad=3.0, rect=[0, 0, 1, 0.95])
fig.suptitle('Titanic EDA Dashboard', fontsize=24)
plt.show()

