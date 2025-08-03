"""
CSV Operations with Pandas Tutorial
===================================

This file covers how to work with CSV files using pandas - one of the most common data formats.
You'll learn to read, write, manipulate, and insert data from/to CSV files.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

print("Welcome to CSV Operations with Pandas! 📄")
print("=" * 40)

# ============================================================================
# 1. CREATING SAMPLE CSV FILES
# ============================================================================

print("\n1. Creating Sample CSV Files")
print("-" * 30)

# Create sample data for demonstrations
sample_employees = pd.DataFrame({
    'EmployeeID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Wilson', 'Eve Davis'],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'IT'],
    'Salary': [75000, 65000, 80000, 70000, 78000],
    'HireDate': ['2022-01-15', '2021-06-10', '2020-03-22', '2023-02-01', '2023-03-15'],
    'IsActive': [True, True, False, True, True]
})

# Create data directory
os.makedirs('data', exist_ok=True)

# Save to CSV
sample_employees.to_csv('data/employees.csv', index=False)
print("✅ Created sample CSV file: data/employees.csv")
print(sample_employees)

# Create another sample file with different characteristics
sales_data = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Quantity': [2, 10, 5, 3, 8],
    'Price': [999.99, 25.50, 75.00, 299.99, 89.99],
    'Customer': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie Davis']
})

sales_data.to_csv('data/sales.csv', index=False)
print(f"\n✅ Created sample CSV file: data/sales.csv")
print(sales_data)

# ============================================================================
# 2. BASIC CSV READING
# ============================================================================

print("\n2. Basic CSV Reading")
print("-" * 30)

# Basic reading
print("Reading employees.csv:")
df_employees = pd.read_csv('data/employees.csv')
print(df_employees)
print(f"Shape: {df_employees.shape}")
print(f"Columns: {df_employees.columns.tolist()}")

# Reading with specific parameters
print(f"\nReading sales.csv with date parsing:")
df_sales = pd.read_csv('data/sales.csv', parse_dates=['Date'])
print(df_sales)
print(f"Date column type: {df_sales['Date'].dtype}")

# ============================================================================
# 3. ADVANCED CSV READING OPTIONS
# ============================================================================

print("\n3. Advanced CSV Reading Options")
print("-" * 30)

# Reading only specific columns
print("Reading only specific columns:")
df_names_salary = pd.read_csv('data/employees.csv', usecols=['Name', 'Salary'])
print(df_names_salary)

# Reading with custom index
print(f"\nReading with EmployeeID as index:")
df_indexed = pd.read_csv('data/employees.csv', index_col='EmployeeID')
print(df_indexed)

# Reading only first few rows
print(f"\nReading only first 3 rows:")
df_limited = pd.read_csv('data/employees.csv', nrows=3)
print(df_limited)

# Skip rows
print(f"\nSkipping first row (header) and reading:")
df_skip = pd.read_csv('data/employees.csv', skiprows=1, 
                     names=['ID', 'Name', 'Dept', 'Salary', 'Date', 'Active'])
print(df_skip.head())

# ============================================================================
# 4. HANDLING DIFFERENT CSV FORMATS
# ============================================================================

print("\n4. Handling Different CSV Formats")
print("-" * 30)

# Create CSV with different separator
sample_semicolon = sample_employees.copy()
sample_semicolon.to_csv('data/employees_semicolon.csv', sep=';', index=False)

# Read CSV with different separator
print("Reading CSV with semicolon separator:")
df_semicolon = pd.read_csv('data/employees_semicolon.csv', sep=';')
print(df_semicolon.head())

# Create CSV with missing values
sample_with_na = sample_employees.copy()
sample_with_na.loc[1, 'Salary'] = np.nan
sample_with_na.loc[2, 'Department'] = np.nan
sample_with_na.to_csv('data/employees_with_na.csv', index=False)

# Read CSV and handle missing values
print(f"\nReading CSV with missing values:")
df_with_na = pd.read_csv('data/employees_with_na.csv')
print(df_with_na)
print(f"Missing values per column:\n{df_with_na.isnull().sum()}")

# Fill missing values while reading
df_filled = pd.read_csv('data/employees_with_na.csv', 
                       na_values=['', 'NULL', 'N/A'])
print(f"\nAfter reading with na_values specified:")
print(df_filled.fillna({'Salary': df_filled['Salary'].mean(), 
                       'Department': 'Unknown'}))

# ============================================================================
# 5. INSERTING DATA INTO EXISTING CSV
# ============================================================================

print("\n5. Inserting Data into Existing CSV")
print("-" * 30)

# Method 1: Read, modify, write back
print("Method 1: Read, modify, write back")
df_existing = pd.read_csv('data/employees.csv')
print("Original data:")
print(df_existing)

# Add new employee
new_employee = {
    'EmployeeID': 1006,
    'Name': 'Frank Miller',
    'Department': 'Sales',
    'Salary': 72000,
    'HireDate': '2023-04-10',
    'IsActive': True
}

df_existing = pd.concat([df_existing, pd.DataFrame([new_employee])], ignore_index=True)
df_existing.to_csv('data/employees.csv', index=False)
print(f"\nAfter adding new employee:")
print(df_existing.tail())

# Method 2: Append mode (be careful - this adds to the end without headers)
print(f"\nMethod 2: Using append mode for single row")
new_employee_2 = pd.DataFrame([[1007, 'Grace Lee', 'IT', 76000, '2023-05-01', True]], 
                             columns=df_existing.columns)

# Read existing data first to avoid header issues
existing_df = pd.read_csv('data/employees.csv')
updated_df = pd.concat([existing_df, new_employee_2], ignore_index=True)
updated_df.to_csv('data/employees.csv', index=False)

print("After appending Grace Lee:")
final_df = pd.read_csv('data/employees.csv')
print(final_df.tail())

# ============================================================================
# 6. BULK DATA INSERTION FROM CSV
# ============================================================================

print("\n6. Bulk Data Insertion from CSV")
print("-" * 30)

# Create a file with new employees to add
new_employees_data = pd.DataFrame({
    'EmployeeID': [1008, 1009, 1010],
    'Name': ['Henry Clark', 'Ivy Rodriguez', 'Jack Turner'],
    'Department': ['HR', 'Finance', 'Sales'],
    'Salary': [68000, 82000, 74000],
    'HireDate': ['2023-05-15', '2023-06-01', '2023-07-01'],
    'IsActive': [True, True, True]
})

new_employees_data.to_csv('data/new_employees.csv', index=False)
print("Created new employees file:")
print(new_employees_data)

# Read both files and combine
existing_employees = pd.read_csv('data/employees.csv')
new_employees = pd.read_csv('data/new_employees.csv')

print(f"\nExisting employees: {len(existing_employees)}")
print(f"New employees: {len(new_employees)}")

# Combine and save
all_employees = pd.concat([existing_employees, new_employees], ignore_index=True)
all_employees.to_csv('data/employees_updated.csv', index=False)

print(f"Combined employees: {len(all_employees)}")
print(all_employees.tail())

# ============================================================================
# 7. DATA VALIDATION DURING CSV OPERATIONS
# ============================================================================

print("\n7. Data Validation During CSV Operations")
print("-" * 30)

def validate_employee_data(df):
    """Validate employee data before insertion"""
    errors = []
    
    # Check for duplicate EmployeeIDs
    if df['EmployeeID'].duplicated().any():
        errors.append("Duplicate EmployeeIDs found")
    
    # Check for missing required fields
    required_fields = ['EmployeeID', 'Name', 'Department']
    for field in required_fields:
        if df[field].isnull().any():
            errors.append(f"Missing values in required field: {field}")
    
    # Check salary range
    if (df['Salary'] < 30000).any() or (df['Salary'] > 200000).any():
        errors.append("Salary values outside reasonable range (30k-200k)")
    
    return errors

# Test validation
print("Validating employee data:")
validation_errors = validate_employee_data(all_employees)
if validation_errors:
    print("❌ Validation errors found:")
    for error in validation_errors:
        print(f"  - {error}")
else:
    print("✅ Data validation passed!")

# Create invalid data to test
invalid_data = pd.DataFrame({
    'EmployeeID': [1001, 1011],  # 1001 is duplicate
    'Name': ['Duplicate Person', None],  # Missing name
    'Department': ['IT', 'Sales'],
    'Salary': [250000, 75000],  # 250k is too high
    'HireDate': ['2023-08-01', '2023-08-02'],
    'IsActive': [True, True]
})

print(f"\nTesting with invalid data:")
validation_errors = validate_employee_data(invalid_data)
if validation_errors:
    print("❌ Validation errors found:")
    for error in validation_errors:
        print(f"  - {error}")

# ============================================================================
# 8. ADVANCED CSV WRITING OPTIONS
# ============================================================================

print("\n8. Advanced CSV Writing Options")
print("-" * 30)

sample_df = all_employees.head()

# Writing with different options
print("Writing CSV with different options:")

# 1. Custom separator
sample_df.to_csv('data/employees_pipe.csv', sep='|', index=False)
print("✅ Saved with pipe separator")

# 2. Include index
sample_df.to_csv('data/employees_with_index.csv', index=True)
print("✅ Saved with index")

# 3. Only specific columns
sample_df[['Name', 'Department', 'Salary']].to_csv('data/employees_subset.csv', index=False)
print("✅ Saved subset of columns")

# 4. Custom date format
sample_df_dates = sample_df.copy()
sample_df_dates['HireDate'] = pd.to_datetime(sample_df_dates['HireDate'])
sample_df_dates.to_csv('data/employees_custom_date.csv', index=False, date_format='%d/%m/%Y')
print("✅ Saved with custom date format")

# 5. Handle missing values
sample_with_na = sample_df.copy()
sample_with_na.loc[0, 'Department'] = np.nan
sample_with_na.to_csv('data/employees_na.csv', index=False, na_rep='MISSING')
print("✅ Saved with custom NA representation")

# ============================================================================
# 9. WORKING WITH LARGE CSV FILES
# ============================================================================

print("\n9. Working with Large CSV Files")
print("-" * 30)

# Create a larger sample file
print("Creating large sample file for demonstration:")
large_data = []
for i in range(10000, 10100):  # 100 records for demo
    large_data.append({
        'ID': i,
        'Name': f'Employee_{i}',
        'Department': np.random.choice(['IT', 'HR', 'Finance', 'Sales', 'Marketing']),
        'Salary': np.random.randint(40000, 120000),
        'Performance': np.random.choice(['Low', 'Medium', 'High'])
    })

large_df = pd.DataFrame(large_data)
large_df.to_csv('data/large_employees.csv', index=False)
print(f"✅ Created large file with {len(large_df)} records")

# Reading in chunks
print(f"\nReading large file in chunks:")
chunk_size = 25
chunk_counter = 0

for chunk in pd.read_csv('data/large_employees.csv', chunksize=chunk_size):
    chunk_counter += 1
    print(f"Chunk {chunk_counter}: {len(chunk)} rows")
    if chunk_counter == 3:  # Show first 3 chunks
        print(chunk.head())
        break

# Processing chunks and inserting results
print(f"\nProcessing chunks and calculating statistics:")
salary_stats = []

for chunk in pd.read_csv('data/large_employees.csv', chunksize=chunk_size):
    dept_avg_salary = chunk.groupby('Department')['Salary'].mean()
    salary_stats.append(dept_avg_salary)

# Combine results
combined_stats = pd.concat(salary_stats, axis=1).mean(axis=1)
print("Average salary by department:")
print(combined_stats)

# ============================================================================
# 10. CSV DATA TRANSFORMATION AND INSERTION
# ============================================================================

print("\n10. CSV Data Transformation and Insertion")
print("-" * 30)

# Read raw data
raw_sales = pd.read_csv('data/sales.csv')
print("Original sales data:")
print(raw_sales)

# Transform data
transformed_sales = raw_sales.copy()
transformed_sales['Date'] = pd.to_datetime(transformed_sales['Date'])
transformed_sales['TotalValue'] = transformed_sales['Quantity'] * transformed_sales['Price']
transformed_sales['Month'] = transformed_sales['Date'].dt.month
transformed_sales['DayOfWeek'] = transformed_sales['Date'].dt.day_name()

# Add category based on product
def get_category(product):
    if product in ['Laptop', 'Monitor']:
        return 'Electronics'
    elif product in ['Mouse', 'Keyboard']:
        return 'Accessories'
    else:
        return 'Audio'

transformed_sales['Category'] = transformed_sales['Product'].apply(get_category)

print(f"\nTransformed sales data:")
print(transformed_sales)

# Save transformed data
transformed_sales.to_csv('data/sales_transformed.csv', index=False)
print("✅ Saved transformed data")

# Create summary and save
summary = transformed_sales.groupby('Category').agg({
    'Quantity': 'sum',
    'TotalValue': ['sum', 'mean'],
    'Product': 'count'
}).round(2)

summary.to_csv('data/sales_summary.csv')
print(f"\nSummary by category:")
print(summary)

# ============================================================================
# EXERCISES
# ============================================================================

print("\n" + "=" * 50)
print("EXERCISES - Try these on your own!")
print("=" * 50)

print("""
1. CSV Reading and Basic Operations:
   - Create a CSV file with student grades
   - Read it with different parameters (specific columns, date parsing)
   - Handle missing values during reading

2. Data Insertion and Updating:
   - Add new students to the existing CSV
   - Update existing student grades
   - Merge data from multiple CSV files

3. Data Validation:
   - Create a validation function for student data
   - Check for duplicate student IDs
   - Validate grade ranges (0-100)

4. Large File Processing:
   - Create a large CSV file (1000+ rows)
   - Process it in chunks
   - Calculate statistics and save results

5. Data Transformation:
   - Read sales data from CSV
   - Add calculated columns (profit, tax, etc.)
   - Group by categories and save summary

6. Real-world Project:
   - Build an inventory management system using CSV files
   - Include product addition, updates, and reporting
   - Handle multiple product categories
""")

# Sample solution framework
print(f"\nSample solution framework:")
print("""
# Exercise 1: Student grades CSV
students = pd.DataFrame({
    'StudentID': [1001, 1002, 1003, 1004],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Math': [85, 92, 78, 88],
    'Science': [90, 87, 82, 91],
    'English': [88, 85, 90, 86]
})

# Save to CSV
students.to_csv('data/students.csv', index=False)

# Add new student
new_student = pd.DataFrame([[1005, 'Eve', 89, 93, 87]], 
                          columns=students.columns)

# Read, combine, save
existing = pd.read_csv('data/students.csv')
updated = pd.concat([existing, new_student], ignore_index=True)
updated.to_csv('data/students.csv', index=False)
""")

print("\nCongratulations! You've mastered CSV Operations with Pandas! 🎉")
print("\nKey takeaways:")
print("- Use pd.read_csv() for reading with various options")
print("- Use DataFrame.to_csv() for writing")
print("- Always validate data before insertion")
print("- Process large files in chunks for efficiency")
print("- Transform data as needed before saving")
print("\nNext: Move on to 08_excel_operations.py for Excel file handling!")