import pandas as pd
import matplotlib.pyplot as plt

diabetes = pd.read_csv('diabetes.csv')

age_diabetes_counts = diabetes.groupby(['Age', 'Outcome']).size().unstack().dropna()

plt.figure(figsize=(10,6))

plt.bar(age_diabetes_counts.index, age_diabetes_counts[1], label="Diabetic", color="red", alpha=1)
plt.bar(age_diabetes_counts.index, age_diabetes_counts[0], label="Non-Diabetic", color="blue", alpha=0.5)

    
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()

plt.title("Age and Diabetes")

plt.show()
