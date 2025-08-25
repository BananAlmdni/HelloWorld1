"""
Python & Pandas Quick Reference Guide
====================================

This file contains a comprehensive quick reference for Python and pandas.
Use this as a cheat sheet when working on your projects!
"""

print("📚 Python & Pandas Quick Reference Guide")
print("=" * 50)

# ============================================================================
# PYTHON BASICS QUICK REFERENCE
# ============================================================================

print("\n🐍 PYTHON BASICS")
print("-" * 30)

# Variables and Data Types
print("Variables & Data Types:")
print("  name = 'Alice'              # String")
print("  age = 25                    # Integer") 
print("  height = 5.9               # Float")
print("  is_student = True          # Boolean")

# Lists
print("\nLists:")
print("  fruits = ['apple', 'banana']")
print("  fruits.append('orange')    # Add item")
print("  fruits[0]                  # Access first item")
print("  len(fruits)                # Get length")

# Dictionaries  
print("\nDictionaries:")
print("  person = {'name': 'Bob', 'age': 30}")
print("  person['name']             # Access value")
print("  person['email'] = 'bob@...' # Add new key")

# Functions
print("\nFunctions:")
print("  def greet(name):")
print("      return f'Hello, {name}!'")
print("  result = greet('Alice')")

# Control Structures
print("\nControl Structures:")
print("  if age >= 18:")
print("      print('Adult')")
print("  elif age >= 13:")  
print("      print('Teen')")
print("  else:")
print("      print('Child')")

print("\n  for item in list:")
print("      print(item)")

print("\n  while condition:")
print("      # do something")

# ============================================================================
# PANDAS QUICK REFERENCE  
# ============================================================================

print(f"\n🐼 PANDAS QUICK REFERENCE")
print("-" * 30)

# Import
print("Import:")
print("  import pandas as pd")
print("  import numpy as np")

# Creating DataFrames
print("\nCreating DataFrames:")
print("  # From dictionary")
print("  df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})")
print("  ")
print("  # From CSV")
print("  df = pd.read_csv('file.csv')")
print("  ")
print("  # From lists")
print("  df = pd.DataFrame(data, columns=['A', 'B'])")

# Viewing Data
print("\nViewing Data:")
print("  df.head()                  # First 5 rows")
print("  df.tail(3)                 # Last 3 rows")
print("  df.info()                  # Dataset info")
print("  df.describe()              # Statistics")
print("  df.shape                   # (rows, columns)")
print("  df.columns                 # Column names")
print("  df.dtypes                  # Data types")

# Selecting Data
print("\nSelecting Data:")
print("  df['column']               # Single column")
print("  df[['col1', 'col2']]       # Multiple columns")
print("  df.iloc[0]                 # First row by position")
print("  df.iloc[0:3]               # First 3 rows")
print("  df.loc[0]                  # Row by label")

# Filtering Data
print("\nFiltering Data:")
print("  df[df['age'] > 25]         # Simple filter")
print("  df[df['age'].between(20, 30)] # Range filter")
print("  df[df['name'].str.contains('A')] # String filter")
print("  df[df['city'].isin(['NYC', 'LA'])] # Multiple values")
print("  df[(df['age'] > 20) & (df['salary'] > 50000)] # Multiple conditions")

# Adding/Modifying Data  
print("\nAdding/Modifying Data:")
print("  df['new_col'] = values     # Add column")
print("  df['total'] = df['a'] + df['b'] # Calculated column")
print("  df.loc[0, 'name'] = 'New' # Modify single value")
print("  df.loc[len(df)] = new_row  # Add row")

# Data Insertion
print("\nData Insertion:")
print("  # Add single row")
print("  new_row = pd.DataFrame([{...}])")
print("  df = pd.concat([df, new_row], ignore_index=True)")
print("  ")
print("  # Add multiple rows")
print("  new_df = pd.DataFrame([{...}, {...}])")
print("  df = pd.concat([df, new_df], ignore_index=True)")

# Sorting and Grouping
print("\nSorting & Grouping:")
print("  df.sort_values('column')   # Sort by column")
print("  df.sort_values(['col1', 'col2']) # Sort by multiple")
print("  df.groupby('category').mean() # Group and aggregate")
print("  df.groupby('cat').agg({'col': ['sum', 'mean']})")

# Missing Data
print("\nMissing Data:")
print("  df.isnull().sum()          # Count missing values")
print("  df.dropna()                # Remove rows with NaN")
print("  df.fillna(value)           # Fill missing values")
print("  df.fillna(df.mean())       # Fill with mean")

# File Operations
print("\nFile Operations:")
print("  # CSV")
print("  df.to_csv('file.csv', index=False)")
print("  df = pd.read_csv('file.csv')")
print("  ")
print("  # Excel") 
print("  df.to_excel('file.xlsx', index=False)")
print("  df = pd.read_excel('file.xlsx')")

# Statistics
print("\nStatistics:")
print("  df['col'].mean()           # Average")
print("  df['col'].median()         # Median")
print("  df['col'].std()            # Standard deviation")
print("  df['col'].min()            # Minimum")
print("  df['col'].max()            # Maximum")
print("  df['col'].value_counts()   # Count unique values")
print("  df.corr()                  # Correlation matrix")

# ============================================================================
# COMMON PATTERNS
# ============================================================================

print(f"\n🔄 COMMON PATTERNS")
print("-" * 30)

# Data Loading and Initial Exploration
print("Data Loading & Exploration:")
print("  df = pd.read_csv('data.csv')")
print("  print(df.shape)")
print("  print(df.info())")
print("  print(df.describe())")
print("  print(df.isnull().sum())")

# Data Cleaning
print("\nData Cleaning:")
print("  # Remove duplicates")
print("  df = df.drop_duplicates()")
print("  ")
print("  # Handle missing values")
print("  df = df.dropna()  # or df.fillna(value)")
print("  ")
print("  # Fix data types")
print("  df['date'] = pd.to_datetime(df['date'])")
print("  df['price'] = df['price'].astype(float)")

# Data Analysis Workflow
print("\nAnalysis Workflow:")
print("  1. Load data: df = pd.read_csv('file.csv')")
print("  2. Explore: df.head(), df.info(), df.describe()")
print("  3. Clean: handle missing values, duplicates")
print("  4. Transform: add calculated columns")
print("  5. Analyze: groupby, aggregations, statistics")
print("  6. Export: df.to_csv('results.csv')")

# ============================================================================
# USEFUL FUNCTIONS
# ============================================================================

print(f"\n🛠️ USEFUL FUNCTIONS")
print("-" * 30)

# String Operations
print("String Operations:")
print("  df['col'].str.upper()      # Uppercase")
print("  df['col'].str.lower()      # Lowercase") 
print("  df['col'].str.contains('x') # Contains text")
print("  df['col'].str.replace('old', 'new') # Replace")
print("  df['col'].str.split(',')   # Split string")

# Date Operations
print("\nDate Operations:")
print("  pd.to_datetime(df['date']) # Convert to datetime")
print("  df['year'] = df['date'].dt.year")
print("  df['month'] = df['date'].dt.month")
print("  df['day_name'] = df['date'].dt.day_name()")

# Mathematical Operations
print("\nMathematical Operations:")
print("  df['col'].abs()            # Absolute value")
print("  df['col'].round(2)         # Round to 2 decimals")
print("  df['col'].cumsum()         # Cumulative sum")
print("  df['col'].pct_change()     # Percentage change")

# Conditional Operations
print("\nConditional Operations:")
print("  df['new'] = np.where(condition, value_if_true, value_if_false)")
print("  df['category'] = df['score'].apply(lambda x: 'High' if x > 80 else 'Low')")

# ============================================================================
# PERFORMANCE TIPS
# ============================================================================

print(f"\n⚡ PERFORMANCE TIPS")
print("-" * 30)

tips = [
    "✅ Use vectorized operations instead of loops",
    "✅ Use pd.concat() instead of append() in loops",
    "✅ Read large files in chunks: pd.read_csv('file.csv', chunksize=1000)",
    "✅ Use categorical data types for strings with few unique values",
    "✅ Specify data types when reading: dtype={'col': 'int32'}",
    "❌ Avoid: df.append() in loops (slow)",
    "❌ Avoid: Iterating row by row when vectorization is possible",
    "❌ Avoid: Creating DataFrames in loops"
]

for tip in tips:
    print(f"  {tip}")

# ============================================================================
# COMMON ERRORS AND SOLUTIONS
# ============================================================================

print(f"\n🔧 COMMON ERRORS & SOLUTIONS")
print("-" * 30)

errors = [
    ("KeyError: 'column'", "Column doesn't exist. Check df.columns"),
    ("IndexError", "Index out of range. Check df.shape"),
    ("ValueError: cannot convert", "Data type mismatch. Check df.dtypes"),
    ("FileNotFoundError", "File path incorrect. Check file location"),
    ("SettingWithCopyWarning", "Use .loc[] or .copy() when modifying DataFrames"),
    ("Memory Error", "File too large. Try reading in chunks"),
    ("Empty DataFrame", "Check file path and content")
]

for error, solution in errors:
    print(f"  ❌ {error}")
    print(f"     💡 {solution}")
    print()

# ============================================================================
# QUICK EXAMPLES
# ============================================================================

print(f"\n💡 QUICK EXAMPLES")
print("-" * 30)

print("Example 1: Load and explore data")
print("  df = pd.read_csv('sales.csv')")
print("  print(f'Shape: {df.shape}')")
print("  print(df.head())")
print("  print(df.describe())")

print("\nExample 2: Clean and transform")
print("  df = df.dropna()  # Remove missing values")
print("  df['total'] = df['quantity'] * df['price']")
print("  df['month'] = pd.to_datetime(df['date']).dt.month")

print("\nExample 3: Analyze and group")
print("  monthly_sales = df.groupby('month')['total'].sum()")
print("  top_products = df.groupby('product')['total'].sum().sort_values(ascending=False)")
print("  print(monthly_sales)")
print("  print(top_products.head())")

print("\nExample 4: Save results")
print("  monthly_sales.to_csv('monthly_report.csv')")
print("  top_products.to_csv('product_ranking.csv')")

# ============================================================================
# LEARNING RESOURCES
# ============================================================================

print(f"\n📖 LEARNING RESOURCES")
print("-" * 30)

resources = [
    "📚 Official pandas documentation: https://pandas.pydata.org/docs/",
    "📚 Python documentation: https://docs.python.org/3/",
    "💻 Practice platform: https://www.kaggle.com/learn/pandas",
    "📺 Video tutorials: Search 'pandas tutorial' on YouTube",
    "📝 Cheat sheets: Search 'pandas cheat sheet' online",
    "🤝 Community: Stack Overflow for specific questions"
]

for resource in resources:
    print(f"  {resource}")

print(f"\n🎯 Remember:")
print("- Practice regularly with real datasets")
print("- Start simple and gradually increase complexity") 
print("- Don't be afraid to experiment and make mistakes")
print("- Google is your friend for specific questions")
print("- Focus on understanding concepts, not memorizing syntax")

print(f"\n" + "=" * 50)
print("📚 Save this as your go-to reference! 📚")
print("=" * 50)