# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 

data=pd.read_csv("heart.csv")
print(data.info)
print(data.describe())

# This dataset don't have any missing value so we can perform EDA
null=data.isnull().sum()
print(null)


# The bar chart tells us regarding the possibility of heart disease for Gender. 
# It is clear that Male are highly prone to heart diseases.
plt.figure(figsize = (15,7))
sns.barplot(data.Sex, data.HeartDisease, color="skyblue",errcolor=".2", edgecolor=".2")
plt.show()

# Plotting Histograms
fig, axes = plt.subplots(3, 2 , figsize=(14, 10))
sns.histplot(data['Sex'], ax=axes[0, 0])
sns.histplot(data['RestingBP'], ax=axes[1, 0])
sns.histplot(data['Cholesterol'], ax=axes[0, 1])
sns.histplot(data['Oldpeak'], ax=axes[2, 0])
sns.histplot(data['MaxHR'], ax=axes[1, 1], bins=70)
fig.delaxes(axes[2,1])
fig.tight_layout()
plt.show()

# plotting Count plot
cols = data.select_dtypes(include='category').columns.values
fig, axes = plt.subplots(3, 2, figsize=(15,8))
sns.countplot(data=data, x='Sex', hue='Sex', ax=axes[0,0])
sns.countplot(data=data, x='ChestPainType', hue='ChestPainType', ax=axes[0,1])
sns.countplot(data=data, x='FastingBS', hue='FastingBS', ax=axes[1,0])
sns.countplot(data=data, x='RestingECG', hue='RestingECG', ax=axes[1,1])
sns.countplot(data=data, x='ExerciseAngina', hue='ExerciseAngina', ax=axes[2,0])
sns.countplot(data=data, x='ST_Slope', hue='ST_Slope', ax=axes[2,1])
fig.tight_layout()
plt.show()


cat_cols = data.select_dtypes(include='category').columns.values
fig, axes = plt.subplots(3, 2, figsize=(14,7))
sns.countplot(data=data, x='Sex', hue='HeartDisease', ax=axes[0,0])
sns.countplot(data=data, x='ChestPainType', hue='HeartDisease', ax=axes[0,1])
sns.countplot(data=data, x='FastingBS', hue='HeartDisease', ax=axes[1,0])
sns.countplot(data=data, x='RestingECG', hue='HeartDisease', ax=axes[1,1])
sns.countplot(data=data, x='ExerciseAngina', hue='HeartDisease', ax=axes[2,0])
sns.countplot(data=data, x='ST_Slope', hue='HeartDisease', ax=axes[2,1])
fig.tight_layout()
plt.show()
# Plotting violin_plot
fig, axes = plt.subplots(3, 2, figsize=(12,10))
sns.violinplot(data=data, x='HeartDisease', y='Age', hue='HeartDisease', ax=axes[0,0])
sns.violinplot(data=data, x='HeartDisease', y='Cholesterol', hue='HeartDisease', ax=axes[0,1])
sns.violinplot(data=data, x='HeartDisease', y='RestingBP', hue='HeartDisease', ax=axes[1,0])
sns.violinplot(data=data, x='HeartDisease', y='MaxHR', hue='HeartDisease', ax=axes[1,1])
sns.violinplot(data=data, x='HeartDisease', y='Oldpeak', hue='HeartDisease', ax=axes[2,0])
fig.delaxes(axes[2,1])
fig.tight_layout()
plt.show()

# plotting boxplot
fig, axes = plt.subplots(1, 3, figsize=(12,5))
sns.boxplot(data=data, x='Sex', y='Age', hue='HeartDisease', ax=axes[0])
sns.boxplot(data=data, x='Sex', y='Cholesterol', hue='HeartDisease', ax=axes[1])
sns.boxplot(data=data, x='Sex', y='RestingBP', hue='HeartDisease', ax=axes[2])
fig.tight_layout()
plt.show()

# plotting correlation heatmap:

plt.figure(figsize=(15,15))
corr_matrix=data.corr()
sns.heatmap(corr_matrix,  square=True ,vmin=1,vmax=-1, cmap='Blues',annot=True,linewidth=1)
plt.title("Correlation heatmap")
plt.show()

# plotting pairplot
sns.pairplot(data, hue = 'HeartDisease')
plt.show()
