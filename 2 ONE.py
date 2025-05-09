import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Replace with your actual data file
# Assuming the data has a column for candidate experience
data = pd.read_csv('C:/Users/Sharm/Downloads/sample_candidates.csv')

# Check the actual columns in the data
print("Columns in dataset:", data.columns)

# Inspect the first few rows to understand the structure
print(data.head())

# Use the correct column name for experience
experience_column = 'Experience'  # Change this if the column name differs

if experience_column not in data.columns:
    raise KeyError(f"Column '{experience_column}' not found in the dataset. Please check the column names.")

# Define experience bins and labels
bins = [0, 2, 5, 10, 20, 30]
labels = ['0-2 years', '3-5 years', '6-10 years', '11-20 years', '21-30 years']

# Categorize experience levels
data['Experience_Category'] = pd.cut(data[experience_column], bins=bins, labels=labels, right=True)

# Count number of candidates in each experience category
experience_counts = data['Experience_Category'].value_counts().sort_index()

# Plotting the histogram
plt.figure(figsize=(8, 6))
experience_counts.plot(kind='bar', color='skyblue')
plt.title('Candidate Experience Levels')
plt.xlabel('Experience Category')
plt.ylabel('Number of Candidates')
plt.xticks(rotation=45)
plt.show()