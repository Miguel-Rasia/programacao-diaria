#font: codesignal
import numpy as np
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Calculate the mean, median, and mode for the age and fare columns
mean_age_fare = titanic_df['fare'].mean()
median_age_fare = titanic_df['fare'].median()
mode_age_fare = titanic_df['fare'].mode().iloc[0]

print(f"Mean of fare: \n{mean_age_fare}\n")
print(f"Median of fare: \n{median_age_fare}\n")
print(f"Mode of fare: \n{mode_age_fare}\n")