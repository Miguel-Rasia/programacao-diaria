# font: codesignal
# Import required libraries
import seaborn as sns
import numpy as np

# TODO: Load the Titanic DataSet
titanic = sns.load_dataset("titanic")

# TODO: Calculate mean, median, and mode for 'age', print them
print(titanic['age'].mean())
print(titanic['age'].median())
print(titanic['age'].mode()[0])

# TODO: Calculate the standard deviation for 'age', print it
print(np.std(titanic['age']))

# TODO: Calculate Quartiles for 'age', print them
print(titanic['age'].quantile(0.25))
print(titanic['age'].quantile(0.75))