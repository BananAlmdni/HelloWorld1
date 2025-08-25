"""
Pandas Basics Tutorial
======================

This file covers fundamental pandas concepts for data manipulation and analysis.
Pandas is the most important library for data science in Python.

Before running this file, you need to install pandas:
In your terminal, run: pip install pandas numpy

If you get errors, you might need to install with:
python3 -m pip install pandas numpy --break-system-packages
"""

# Import necessary libraries
try:
    import pandas as pd
    import numpy as np
    print("✅ Successfully imported pandas and numpy!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install pandas and numpy:")
    print("pip install pandas numpy")
    exit()

print("Welcome to Pandas Basics! 🐼")
print("=" * 40)

# ============================================================================
# 1. CREATING DATAFRAMES
# ============================================================================

print("\n1. Creating DataFrames")
print("-" * 30)

# Method 1: From a dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
    'Salary': [70000, 80000, 90000, 75000, 85000]
}

df = pd.DataFrame(data_dict)
print("DataFrame from dictionary:")
print(df)
print(f"DataFrame shape: {df.shape}")  # (rows, columns)

# Method 2: From lists
names = ['Frank', 'Grace', 'Henry']
ages = [29, 31, 27]
cities = ['Berlin', 'Madrid', 'Rome']

df2 = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'City': cities
})

print(f"\nSecond DataFrame:")
print(df2)

# Method 3: From numpy array
np_data = np.array([
    ['John', 26, 'Boston'],
    ['Jane', 24, 'Chicago'],
    ['Jack', 28, 'Seattle']
])

df3 = pd.DataFrame(np_data, columns=['Name', 'Age', 'City'])
print(f"\nDataFrame from numpy array:")
print(df3)

# ============================================================================
# 2. EXPLORING DATAFRAME STRUCTURE
# ============================================================================

print("\n2. Exploring DataFrame Structure")
print("-" * 30)

# Basic information about the DataFrame
print("DataFrame info:")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Data types:\n{df.dtypes}")

# First few rows
print(f"\nFirst 3 rows:")
print(df.head(3))

# Last few rows
print(f"\nLast 2 rows:")
print(df.tail(2))

# Statistical summary
print(f"\nStatistical summary:")
print(df.describe())

# Information about the DataFrame
print(f"\nDataFrame info:")
df.info()

# ============================================================================
# 3. SELECTING DATA
# ============================================================================

print("\n3. Selecting Data")
print("-" * 30)

# Selecting a single column
print("Names column:")
print(df['Name'])

# Selecting multiple columns
print(f"\nNames and Ages:")
print(df[['Name', 'Age']])

# Selecting rows by index
print(f"\nFirst row:")
print(df.iloc[0])

print(f"\nFirst 3 rows:")
print(df.iloc[0:3])

# Selecting specific rows and columns
print(f"\nFirst 2 rows, Name and Salary columns:")
print(df.iloc[0:2][['Name', 'Salary']])

# Using loc for label-based selection
print(f"\nRow with index 1:")
print(df.loc[1])

# ============================================================================
# 4. FILTERING DATA
# ============================================================================

print("\n4. Filtering Data")
print("-" * 30)

# Simple filtering
high_earners = df[df['Salary'] > 75000]
print("People earning more than $75,000:")
print(high_earners)

# Multiple conditions
young_high_earners = df[(df['Age'] < 30) & (df['Salary'] > 70000)]
print(f"\nYoung people (< 30) earning more than $70,000:")
print(young_high_earners)

# Using isin() for multiple values
cities_of_interest = df[df['City'].isin(['New York', 'London', 'Tokyo'])]
print(f"\nPeople in New York, London, or Tokyo:")
print(cities_of_interest)

# String filtering
names_with_a = df[df['Name'].str.contains('a', case=False)]
print(f"\nNames containing 'a' (case insensitive):")
print(names_with_a)

# ============================================================================
# 5. ADDING AND MODIFYING DATA
# ============================================================================

print("\n5. Adding and Modifying Data")
print("-" * 30)

# Create a copy to avoid modifying original data
df_modified = df.copy()

# Adding a new column
df_modified['Department'] = ['IT', 'HR', 'Finance', 'Marketing', 'IT']
print("Added Department column:")
print(df_modified)

# Calculating new columns
df_modified['Annual_Bonus'] = df_modified['Salary'] * 0.1
df_modified['Total_Compensation'] = df_modified['Salary'] + df_modified['Annual_Bonus']

print(f"\nWith calculated columns:")
print(df_modified[['Name', 'Salary', 'Annual_Bonus', 'Total_Compensation']])

# Modifying existing data
df_modified.loc[0, 'Age'] = 26  # Change Alice's age
print(f"\nAfter modifying Alice's age:")
print(df_modified[['Name', 'Age']].head())

# ============================================================================
# 6. SORTING DATA
# ============================================================================

print("\n6. Sorting Data")
print("-" * 30)

# Sort by single column
sorted_by_age = df.sort_values('Age')
print("Sorted by Age (ascending):")
print(sorted_by_age[['Name', 'Age']])

# Sort by multiple columns
sorted_multi = df.sort_values(['City', 'Age'], ascending=[True, False])
print(f"\nSorted by City (asc) then Age (desc):")
print(sorted_multi[['Name', 'City', 'Age']])

# Sort by index
sorted_by_index = df.sort_index(ascending=False)
print(f"\nSorted by index (descending):")
print(sorted_by_index)

# ============================================================================
# 7. GROUPING DATA
# ============================================================================

print("\n7. Grouping Data")
print("-" * 30)

# Create more data for grouping example
group_data = {
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance', 'Marketing'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'],
    'Salary': [70000, 80000, 60000, 65000, 90000, 85000, 55000],
    'Experience': [3, 5, 2, 4, 8, 6, 1]
}

df_group = pd.DataFrame(group_data)
print("Sample data for grouping:")
print(df_group)

# Group by department
dept_stats = df_group.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min', 'count'],
    'Experience': 'mean'
})

print(f"\nSalary statistics by Department:")
print(dept_stats)

# Simple groupby operations
print(f"\nAverage salary by department:")
print(df_group.groupby('Department')['Salary'].mean())

print(f"\nEmployee count by department:")
print(df_group.groupby('Department').size())

# ============================================================================
# 8. HANDLING MISSING DATA
# ============================================================================

print("\n8. Handling Missing Data")
print("-" * 30)

# Create data with missing values
data_with_na = {
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, None, 30, 28],
    'Salary': [50000, 60000, None, 70000],
    'City': ['NYC', 'LA', 'Chicago', None]
}

df_na = pd.DataFrame(data_with_na)
print("Data with missing values:")
print(df_na)

# Check for missing values
print(f"\nMissing values per column:")
print(df_na.isnull().sum())

# Drop rows with any missing values
df_dropna = df_na.dropna()
print(f"\nAfter dropping rows with missing values:")
print(df_dropna)

# Fill missing values
df_filled = df_na.fillna({
    'Age': df_na['Age'].mean(),
    'Salary': df_na['Salary'].median(),
    'City': 'Unknown'
})
print(f"\nAfter filling missing values:")
print(df_filled)

# ============================================================================
# 9. BASIC STATISTICS
# ============================================================================

print("\n9. Basic Statistics")
print("-" * 30)

print("Basic statistics for salary column:")
print(f"Mean: ${df['Salary'].mean():,.2f}")
print(f"Median: ${df['Salary'].median():,.2f}")
print(f"Standard deviation: ${df['Salary'].std():,.2f}")
print(f"Min: ${df['Salary'].min():,.2f}")
print(f"Max: ${df['Salary'].max():,.2f}")

# Value counts
print(f"\nAge distribution:")
print(df['Age'].value_counts().sort_index())

# Correlation
numeric_df = df.select_dtypes(include=[np.number])
print(f"\nCorrelation matrix:")
print(numeric_df.corr())

# ============================================================================
# 10. BASIC DATA INSERTION EXAMPLES
# ============================================================================

print("\n10. Basic Data Insertion")
print("-" * 30)

# Create a base DataFrame
base_df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
})

print("Original DataFrame:")
print(base_df)

# Method 1: Add new row using loc
base_df.loc[len(base_df)] = [4, 'Diana', 92]
print(f"\nAfter adding Diana:")
print(base_df)

# Method 2: Add new row using concat
new_row = pd.DataFrame([[5, 'Eve', 88]], columns=['ID', 'Name', 'Score'])
base_df = pd.concat([base_df, new_row], ignore_index=True)
print(f"\nAfter adding Eve:")
print(base_df)

# Method 3: Add multiple rows
new_rows = pd.DataFrame([
    [6, 'Frank', 83],
    [7, 'Grace', 91]
], columns=['ID', 'Name', 'Score'])

base_df = pd.concat([base_df, new_rows], ignore_index=True)
print(f"\nAfter adding Frank and Grace:")
print(base_df)

# Add new column
base_df['Grade'] = base_df['Score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C')
print(f"\nAfter adding Grade column:")
print(base_df)

# ============================================================================
# EXERCISES
# ============================================================================

print("\n" + "=" * 50)
print("EXERCISES - Try these on your own!")
print("=" * 50)

print("""
1. Create a DataFrame with student data (name, age, grade, subject) for 8 students.

2. Filter the DataFrame to show only students with grade >= 85.

3. Add a new column 'Status' that shows 'Pass' if grade >= 70, 'Fail' otherwise.

4. Group students by subject and calculate average grades.

5. Sort the DataFrame by grade in descending order.

6. Create a new DataFrame with 2 new students and merge it with the original.

7. Calculate the following statistics for grades:
   - Mean, Median, Standard deviation
   - Minimum and Maximum grades

8. Find students whose names start with a specific letter.
""")

# Example solution framework (uncomment and complete):
"""
# Exercise 1: Create student DataFrame
students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Age': [20, 21, 19, 22, 20, 21, 19, 20],
    'Grade': [85, 78, 92, 88, 76, 94, 82, 89],
    'Subject': ['Math', 'Science', 'Math', 'English', 'Science', 'Math', 'English', 'Science']
})

# Exercise 2: Filter high performers
high_performers = students[students['Grade'] >= 85]

# Continue with other exercises...
"""

print("\nCongratulations! You've completed Pandas Basics! 🎉")
print("Next steps:")
print("- Try the exercises above")
print("- Move on to 05_data_manipulation.py for advanced operations")
print("- Experiment with your own data")

# ============================================================================
# QUICK REFERENCE
# ============================================================================

print("\n" + "=" * 50)
print("QUICK REFERENCE")
print("=" * 50)

reference = """
Creating DataFrames:
- pd.DataFrame(dictionary)
- pd.DataFrame(list_of_lists, columns=column_names)

Viewing Data:
- df.head(n) - first n rows
- df.tail(n) - last n rows
- df.info() - DataFrame info
- df.describe() - statistical summary

Selecting Data:
- df['column'] - single column
- df[['col1', 'col2']] - multiple columns
- df.iloc[row_index] - row by position
- df.loc[label] - row by label

Filtering:
- df[df['column'] > value]
- df[df['column'].isin(list_of_values)]
- df[condition1 & condition2]

Adding Data:
- df['new_column'] = values
- df.loc[len(df)] = new_row
- pd.concat([df1, df2])

Sorting and Grouping:
- df.sort_values('column')
- df.groupby('column').agg(function)

Missing Data:
- df.isnull().sum()
- df.dropna()
- df.fillna(value)
"""

print(reference)