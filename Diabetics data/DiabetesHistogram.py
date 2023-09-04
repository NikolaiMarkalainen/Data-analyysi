import pandas as pd

import matplotlib.pyplot as plt


diabetes = pd.read_csv('diabetes.csv')

variables_to_plot = ["Pregnancies", "Glucose", "BloodPressure", "Age", "Outcome", "BMI", "SkinThickness", "Insulin", "DiabetesPedigreeFunction"]
fig, axes = plt.subplots(3, 3, figsize=(15, 12))

axes = axes.ravel()

for i, var in enumerate(variables_to_plot):
    axes[i].hist(diabetes[var], bins=len(diabetes[var]), edgecolor='k')
    axes[i].set_title(var)
    axes[i].set_xlabel(var)
    axes[i].set_ylabel("Frequencies")

plt.tight_layout()

plt.show()


