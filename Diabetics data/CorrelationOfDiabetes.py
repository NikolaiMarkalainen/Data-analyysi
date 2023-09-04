import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


diabetes = pd.read_csv('diabetes.csv')

correlation_matrix = diabetes.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", linewidths=0.5)
plt.title("Diabetes Correlation Heatmap")
plt.show()


