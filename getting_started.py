"""
Getting Started with Python and Pandas
======================================

Welcome! This is your first step into the world of Python and pandas.
This script will help you verify everything is working correctly.

Run this file to make sure your environment is set up properly!
"""

print("🐍 Welcome to Python and Pandas Learning! 🐼")
print("=" * 50)

# ============================================================================
# 1. CHECK PYTHON VERSION
# ============================================================================

import sys
print(f"\n✅ Python Version: {sys.version}")

if sys.version_info >= (3, 7):
    print("✅ Great! You have a compatible Python version.")
else:
    print("⚠️  Warning: You might need Python 3.7 or higher for best compatibility.")

# ============================================================================
# 2. CHECK REQUIRED LIBRARIES
# ============================================================================

print(f"\n🔍 Checking Required Libraries:")
print("-" * 30)

# Check pandas
try:
    import pandas as pd
    print(f"✅ pandas {pd.__version__} - READY!")
except ImportError:
    print("❌ pandas not found. Install with: pip install pandas")

# Check numpy
try:
    import numpy as np
    print(f"✅ numpy {np.__version__} - READY!")
except ImportError:
    print("❌ numpy not found. Install with: pip install numpy")

# ============================================================================
# 3. CREATE YOUR FIRST DATAFRAME
# ============================================================================

print(f"\n🎯 Creating Your First DataFrame:")
print("-" * 30)

try:
    # Create sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Tokyo']
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    print("🎉 Success! Here's your first DataFrame:")
    print(df)
    
    print(f"\nDataFrame info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
except Exception as e:
    print(f"❌ Error creating DataFrame: {e}")

# ============================================================================
# 4. BASIC OPERATIONS TEST
# ============================================================================

print(f"\n🧪 Testing Basic Operations:")
print("-" * 30)

try:
    # Test some basic operations
    print(f"Average age: {df['Age'].mean()}")
    print(f"People in the data: {len(df)}")
    print(f"Cities represented: {df['City'].tolist()}")
    
    # Add a new column
    df['Country'] = ['USA', 'UK', 'Japan']
    print(f"\nAfter adding Country column:")
    print(df)
    
    print("✅ All basic operations working correctly!")
    
except Exception as e:
    print(f"❌ Error in basic operations: {e}")

# ============================================================================
# 5. FILE OPERATIONS TEST
# ============================================================================

print(f"\n📁 Testing File Operations:")
print("-" * 30)

try:
    import os
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Save DataFrame to CSV
    df.to_csv('data/first_dataframe.csv', index=False)
    print("✅ Successfully saved DataFrame to CSV")
    
    # Read it back
    df_read = pd.read_csv('data/first_dataframe.csv')
    print("✅ Successfully read DataFrame from CSV")
    
    print("File operations working correctly!")
    
except Exception as e:
    print(f"❌ Error in file operations: {e}")

# ============================================================================
# 6. ENVIRONMENT SUMMARY
# ============================================================================

print(f"\n📊 Environment Summary:")
print("=" * 30)

print(f"✅ Python Version: {sys.version.split()[0]}")
try:
    print(f"✅ pandas Version: {pd.__version__}")
    print(f"✅ numpy Version: {np.__version__}")
except:
    print("❌ Some libraries not available")

print(f"✅ Working Directory: {os.getcwd()}")
print(f"✅ Data Directory: {'Created' if os.path.exists('data') else 'Not found'}")

# ============================================================================
# 7. WHAT'S NEXT?
# ============================================================================

print(f"\n🚀 What's Next?")
print("=" * 30)

next_steps = [
    "1. 📚 Start with '01_python_basics.py' to learn Python fundamentals",
    "2. 🐼 Move to '04_pandas_basics.py' for pandas introduction", 
    "3. 📝 Practice with '06_data_insertion.py' for data manipulation",
    "4. 📄 Learn file operations with '07_csv_operations.py'",
    "5. 🚀 Complete the project in 'projects/basic_data_analysis.py'"
]

for step in next_steps:
    print(step)

print(f"\n💡 Tips for Success:")
tips = [
    "• Run each file step by step",
    "• Experiment with the code - try changing values!",
    "• Complete the exercises at the end of each file",
    "• Don't rush - understanding is more important than speed",
    "• Ask questions and look up documentation when needed"
]

for tip in tips:
    print(tip)

# ============================================================================
# 8. QUICK PYTHON REFRESHER
# ============================================================================

print(f"\n⚡ Quick Python Refresher:")
print("-" * 30)

# Variables and basic operations
name = "Data Scientist"
experience_years = 2
is_learning = True

print(f"Role: {name}")
print(f"Experience: {experience_years} years")
print(f"Currently learning: {is_learning}")

# Lists and loops
skills = ["Python", "pandas", "Data Analysis"]
print(f"\nSkills to learn:")
for i, skill in enumerate(skills, 1):
    print(f"  {i}. {skill}")

# Simple function
def calculate_progress(completed_files, total_files):
    return (completed_files / total_files) * 100

progress = calculate_progress(1, 5)  # You just completed this file!
print(f"\nLearning progress: {progress}% (1 out of 5 files completed)")

# ============================================================================
# 9. TROUBLESHOOTING
# ============================================================================

print(f"\n🔧 Troubleshooting:")
print("-" * 30)

troubleshooting = """
If you see errors:

📦 Missing Libraries:
   • Run: pip install pandas numpy
   • Or: python3 -m pip install pandas numpy

🔒 Permission Errors:
   • Try: pip install --user pandas numpy
   • Or: python3 -m pip install --user pandas numpy

🐍 Python Not Found:
   • Make sure Python is installed
   • Try: python3 instead of python

📁 File Errors:
   • Make sure you're in the right directory
   • Check if data folder exists

❓ Still having issues?
   • Check the README.md file
   • Verify your Python installation
   • Ensure you have write permissions in this directory
"""

print(troubleshooting)

# ============================================================================
# COMPLETION
# ============================================================================

print(f"\n🎉 Congratulations!")
print("=" * 30)

print("You've successfully completed the setup verification!")
print("Your Python and pandas environment is ready for learning.")
print(f"\n🎯 You're now ready to start your data science journey!")
print("Happy learning! 🚀📊🐍🐼")

print(f"\n" + "=" * 50)
print("🌟 Ready to become a Python & Pandas expert! 🌟")
print("=" * 50)