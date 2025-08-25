"""
Pandas Data Insertion Tutorial
==============================

This file focuses specifically on different methods to insert data into pandas DataFrames.
You'll learn various techniques for adding rows, columns, and modifying existing data.
"""

import pandas as pd
import numpy as np
from datetime import datetime, date

print("Welcome to Pandas Data Insertion! 📝")
print("=" * 40)

# ============================================================================
# 1. CREATING BASE DATAFRAMES FOR EXAMPLES
# ============================================================================

print("\n1. Creating Base DataFrames")
print("-" * 30)

# Create sample employee DataFrame
employees = pd.DataFrame({
    'EmployeeID': [1001, 1002, 1003],
    'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown'],
    'Department': ['IT', 'HR', 'Finance'],
    'Salary': [75000, 65000, 80000],
    'HireDate': ['2022-01-15', '2021-06-10', '2020-03-22']
})

print("Base Employee DataFrame:")
print(employees)

# ============================================================================
# 2. INSERTING SINGLE ROWS
# ============================================================================

print("\n2. Inserting Single Rows")
print("-" * 30)

# Method 1: Using loc with length of DataFrame
print("Method 1: Using df.loc[len(df)]")
employees_copy1 = employees.copy()
employees_copy1.loc[len(employees_copy1)] = [1004, 'Diana Wilson', 'Marketing', 70000, '2023-02-01']
print(employees_copy1)

# Method 2: Using concat with new DataFrame
print(f"\nMethod 2: Using pd.concat()")
employees_copy2 = employees.copy()
new_employee = pd.DataFrame({
    'EmployeeID': [1005],
    'Name': ['Eve Davis'],
    'Department': ['IT'],
    'Salary': [78000],
    'HireDate': ['2023-03-15']
})
employees_copy2 = pd.concat([employees_copy2, new_employee], ignore_index=True)
print(employees_copy2)

# Method 3: Using append (deprecated but still shown for reference)
print(f"\nMethod 3: Using dictionary with concat (recommended over append)")
employees_copy3 = employees.copy()
new_employee_dict = {
    'EmployeeID': 1006,
    'Name': 'Frank Miller',
    'Department': 'Sales',
    'Salary': 72000,
    'HireDate': '2023-04-10'
}
# Convert dict to DataFrame and concat
new_df = pd.DataFrame([new_employee_dict])
employees_copy3 = pd.concat([employees_copy3, new_df], ignore_index=True)
print(employees_copy3)

# ============================================================================
# 3. INSERTING MULTIPLE ROWS
# ============================================================================

print("\n3. Inserting Multiple Rows")
print("-" * 30)

# Method 1: Using concat with multiple row DataFrame
print("Inserting multiple rows at once:")
employees_multi = employees.copy()

new_employees = pd.DataFrame({
    'EmployeeID': [1007, 1008, 1009],
    'Name': ['Grace Lee', 'Henry Clark', 'Ivy Rodriguez'],
    'Department': ['IT', 'HR', 'Finance'],
    'Salary': [76000, 68000, 82000],
    'HireDate': ['2023-05-01', '2023-05-15', '2023-06-01']
})

employees_multi = pd.concat([employees_multi, new_employees], ignore_index=True)
print(employees_multi)

# Method 2: Using list of dictionaries
print(f"\nUsing list of dictionaries:")
employees_list = employees.copy()

new_employees_list = [
    {'EmployeeID': 1010, 'Name': 'Jack Turner', 'Department': 'Sales', 'Salary': 74000, 'HireDate': '2023-07-01'},
    {'EmployeeID': 1011, 'Name': 'Kate Wright', 'Department': 'Marketing', 'Salary': 71000, 'HireDate': '2023-07-15'}
]

new_df_from_list = pd.DataFrame(new_employees_list)
employees_list = pd.concat([employees_list, new_df_from_list], ignore_index=True)
print(employees_list.tail())

# ============================================================================
# 4. INSERTING COLUMNS
# ============================================================================

print("\n4. Inserting Columns")
print("-" * 30)

# Start with base DataFrame
employees_cols = employees.copy()

# Method 1: Simple assignment
print("Method 1: Simple column assignment")
employees_cols['Email'] = ['alice.j@company.com', 'bob.s@company.com', 'charlie.b@company.com']
print(employees_cols)

# Method 2: Calculated columns
print(f"\nMethod 2: Calculated columns")
employees_cols['AnnualBonus'] = employees_cols['Salary'] * 0.1
employees_cols['TotalCompensation'] = employees_cols['Salary'] + employees_cols['AnnualBonus']
print(employees_cols[['Name', 'Salary', 'AnnualBonus', 'TotalCompensation']])

# Method 3: Conditional columns
print(f"\nMethod 3: Conditional columns")
employees_cols['SeniorityLevel'] = employees_cols['Salary'].apply(
    lambda x: 'Senior' if x >= 75000 else 'Mid' if x >= 65000 else 'Junior'
)
print(employees_cols[['Name', 'Salary', 'SeniorityLevel']])

# Method 4: Using np.where for complex conditions
employees_cols['Performance'] = np.where(
    employees_cols['Salary'] > 70000, 'High',
    np.where(employees_cols['Salary'] > 65000, 'Medium', 'Low')
)
print(employees_cols[['Name', 'Salary', 'Performance']])

# ============================================================================
# 5. INSERTING AT SPECIFIC POSITIONS
# ============================================================================

print("\n5. Inserting at Specific Positions")
print("-" * 30)

# Insert row at specific index
print("Inserting row at specific position:")
employees_pos = employees.copy()

# First, we need to make space
employees_pos = employees_pos.reset_index(drop=True)
print("Original DataFrame:")
print(employees_pos)

# Insert at position 1 (between first and second row)
new_row = pd.DataFrame({
    'EmployeeID': [1050],
    'Name': ['Linda Thompson'],
    'Department': ['Operations'],
    'Salary': [73000],
    'HireDate': ['2023-01-10']
})

# Split DataFrame and insert
first_part = employees_pos.iloc[:1]
second_part = employees_pos.iloc[1:]
employees_pos = pd.concat([first_part, new_row, second_part], ignore_index=True)
print(f"\nAfter inserting at position 1:")
print(employees_pos)

# Insert column at specific position using insert()
print(f"\nInserting column at specific position:")
employees_pos.insert(2, 'MiddleName', ['M.', 'J.', 'K.', 'R.'])
print(employees_pos)

# ============================================================================
# 6. INSERTING WITH DIFFERENT DATA TYPES
# ============================================================================

print("\n6. Inserting with Different Data Types")
print("-" * 30)

# Create DataFrame with various data types
mixed_data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85.5, 90.0, 78.5],
    'Passed': [True, True, False],
    'JoinDate': [date(2023, 1, 15), date(2023, 2, 10), date(2023, 3, 5)]
})

print("DataFrame with mixed data types:")
print(mixed_data)
print(f"Data types:\n{mixed_data.dtypes}")

# Insert new row with correct data types
new_mixed_row = {
    'ID': 4,
    'Name': 'Diana',
    'Score': 92.5,
    'Passed': True,
    'JoinDate': date(2023, 4, 1)
}

mixed_data = pd.concat([mixed_data, pd.DataFrame([new_mixed_row])], ignore_index=True)
print(f"\nAfter inserting new row:")
print(mixed_data)

# ============================================================================
# 7. BULK DATA INSERTION FROM DIFFERENT SOURCES
# ============================================================================

print("\n7. Bulk Data Insertion from Different Sources")
print("-" * 30)

# Example 1: From lists
print("Inserting from lists:")
base_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(f"Base DataFrame:\n{base_df}")

# Data as lists
new_data_lists = [
    [5, 6],
    [7, 8],
    [9, 10]
]

new_rows_df = pd.DataFrame(new_data_lists, columns=['A', 'B'])
base_df = pd.concat([base_df, new_rows_df], ignore_index=True)
print(f"After inserting from lists:\n{base_df}")

# Example 2: From numpy array
print(f"\nInserting from numpy array:")
base_df2 = pd.DataFrame({'X': [1, 2], 'Y': [3, 4], 'Z': [5, 6]})
print(f"Base DataFrame:\n{base_df2}")

np_data = np.array([
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])

np_df = pd.DataFrame(np_data, columns=['X', 'Y', 'Z'])
base_df2 = pd.concat([base_df2, np_df], ignore_index=True)
print(f"After inserting from numpy array:\n{base_df2}")

# ============================================================================
# 8. INSERTING WITH INDEX MANAGEMENT
# ============================================================================

print("\n8. Inserting with Index Management")
print("-" * 30)

# Create DataFrame with custom index
indexed_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
}, index=['A001', 'A002', 'A003'])

print("DataFrame with custom index:")
print(indexed_df)

# Insert with specific index
new_row_indexed = pd.DataFrame({
    'Name': ['Diana'],
    'Score': [92]
}, index=['A004'])

indexed_df = pd.concat([indexed_df, new_row_indexed])
print(f"\nAfter inserting with custom index:")
print(indexed_df)

# Insert multiple rows with custom indices
new_rows_indexed = pd.DataFrame({
    'Name': ['Eve', 'Frank'],
    'Score': [88, 91]
}, index=['A005', 'A006'])

indexed_df = pd.concat([indexed_df, new_rows_indexed])
print(f"\nAfter inserting multiple rows with custom indices:")
print(indexed_df)

# ============================================================================
# 9. HANDLING DUPLICATE DATA DURING INSERTION
# ============================================================================

print("\n9. Handling Duplicate Data During Insertion")
print("-" * 30)

# Create DataFrame with potential duplicates
original_data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com']
})

print("Original data:")
print(original_data)

# Data to insert (contains duplicate)
new_data = pd.DataFrame({
    'ID': [2, 4, 5],  # ID 2 already exists
    'Name': ['Bob', 'Diana', 'Eve'],  # Bob is duplicate
    'Email': ['bob@email.com', 'diana@email.com', 'eve@email.com']
})

print(f"\nData to insert:")
print(new_data)

# Method 1: Insert all and then remove duplicates
combined_with_dups = pd.concat([original_data, new_data], ignore_index=True)
print(f"\nAfter concatenation (with duplicates):")
print(combined_with_dups)

# Remove duplicates based on ID
combined_no_dups = combined_with_dups.drop_duplicates(subset=['ID'], keep='first')
print(f"\nAfter removing duplicates (keeping first occurrence):")
print(combined_no_dups)

# Method 2: Filter out duplicates before insertion
new_ids = set(original_data['ID'])
filtered_new_data = new_data[~new_data['ID'].isin(new_ids)]
print(f"\nFiltered new data (no existing IDs):")
print(filtered_new_data)

combined_filtered = pd.concat([original_data, filtered_new_data], ignore_index=True)
print(f"\nFinal result after filtering:")
print(combined_filtered)

# ============================================================================
# 10. PERFORMANCE CONSIDERATIONS
# ============================================================================

print("\n10. Performance Considerations")
print("-" * 30)

print("Performance Tips for Data Insertion:")
print("""
1. ✅ DO: Use pd.concat() for adding multiple rows
2. ❌ AVOID: Using append() in loops (deprecated and slow)
3. ✅ DO: Collect data in lists/dicts, then create DataFrame once
4. ❌ AVOID: Adding one row at a time in loops
5. ✅ DO: Use vectorized operations for calculated columns
6. ✅ DO: Pre-allocate DataFrame size when possible
""")

# Example of efficient bulk insertion
print(f"\nEfficient bulk insertion example:")
import time

# Simulate collecting data
collected_data = []
for i in range(1000, 1005):
    collected_data.append({
        'ID': i,
        'Name': f'Employee_{i}',
        'Salary': 50000 + (i % 100) * 1000
    })

# Convert to DataFrame once
bulk_df = pd.DataFrame(collected_data)
print(f"Bulk inserted {len(bulk_df)} rows efficiently")
print(bulk_df.head())

# ============================================================================
# EXERCISES
# ============================================================================

print("\n" + "=" * 50)
print("EXERCISES - Try these on your own!")
print("=" * 50)

print("""
1. Create a DataFrame with student data and:
   - Add 3 new students using different insertion methods
   - Add a calculated column for GPA categories
   - Insert a new column at position 2

2. Create a sales DataFrame and:
   - Insert bulk data from lists
   - Handle duplicate customer IDs
   - Add time-based columns

3. Build an inventory management system:
   - Start with 5 products
   - Add new products with different data types
   - Calculate total value columns
   - Insert products at specific positions

4. Performance comparison:
   - Time the difference between inserting rows one by one vs. bulk
   - Create 1000 rows of sample data efficiently

5. Data validation during insertion:
   - Create a function that validates data before insertion
   - Handle missing values during insertion
   - Ensure data type consistency
""")

# Template for exercises
print(f"\nExercise template:")
print("""
# Exercise 1: Student data
students = pd.DataFrame({
    'StudentID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Grade': [85, 90, 78]
})

# Your code here...
""")

print("\nCongratulations! You've mastered Data Insertion in Pandas! 🎉")
print("Next steps:")
print("- Practice with real datasets")
print("- Learn about data validation")
print("- Explore database integration")
print("- Move on to advanced pandas operations")