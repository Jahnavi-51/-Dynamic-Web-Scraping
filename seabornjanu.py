# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme()
#
# tips = sns.load_dataset("")
#
# sns.relplot(
#     data = tips,
#     x ="timestamp",y="prices",col ="prices of crypto"
# )
#
# plt.show()

import pandas as pd

# Sample tips dataset
data = {
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 14.83, 29.85, 15.92],
    "tip": [1.01, 1.66, 3.50, 3.31, 4.06, 5.00, 2.00, 3.15, 5.75, 2.60],
    "sex": ["Female", "Female", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Female"],
    "smoker": ["No", "No", "No", "Yes", "No", "No", "No", "Yes", "Yes", "No"],
    "day": ["Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri"],
    "time": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Dinner", "Dinner", "Lunch"],
    "size": [2, 3, 3, 2, 4, 4, 2, 2, 3, 2]
}

# Create a DataFrame
tips = pd.DataFrame(data)

import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tips = sns.load_dataset("tips")

# Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Scatter Plot of Total Bill vs. Tip")
plt.show()

# Bar Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill", estimator=sum)
plt.title("Total Bill by Day")
plt.show()

# Line Plot
plt.figure(figsize=(8, 5))
sns.lineplot(data=tips, x="size", y="total_bill", ci=None)
plt.title("Total Bill by Table Size")
plt.show()

# Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Box Plot of Total Bill by Day")
plt.show()

# Violin Plot
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill")
plt.title("Violin Plot of Total Bill by Day")
plt.show()

# Heatmap
plt.figure(figsize=(8, 5))
pivot_table = tips.pivot_table(values='tip', index='day', columns='sex', aggfunc='mean')
sns.heatmap(pivot_table, annot=True, cmap='coolwarm')
plt.title("Mean Tip by Day and Gender")
plt.show()

# Customized Bar Plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill by Day (Customized)")
plt.show()

