"""
Basic Data Analysis Project
===========================

This project demonstrates practical application of Python and pandas concepts
you've learned. We'll analyze a sales dataset and create insights.

Project Goals:
1. Load and explore sales data
2. Clean and validate the data
3. Add calculated columns
4. Perform analysis and create summaries
5. Export results
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, date, timedelta

print("🚀 Basic Data Analysis Project")
print("=" * 40)

# ============================================================================
# 1. PROJECT SETUP AND DATA CREATION
# ============================================================================

print("\n1. Setting Up Project and Creating Sample Data")
print("-" * 30)

# Create project directory structure
os.makedirs('../data/project', exist_ok=True)
os.makedirs('output', exist_ok=True)

# Generate realistic sales data
np.random.seed(42)  # For reproducible results

# Products and their base prices
products = {
    'Laptop': 999.99,
    'Mouse': 25.50,
    'Keyboard': 75.00,
    'Monitor': 299.99,
    'Headphones': 89.99,
    'Webcam': 149.99,
    'Speaker': 199.99,
    'Tablet': 499.99
}

# Generate 500 sales records
sales_data = []
start_date = datetime(2023, 1, 1)

for i in range(500):
    # Random date in 2023
    random_days = np.random.randint(0, 365)
    sale_date = start_date + timedelta(days=random_days)
    
    # Random product
    product = np.random.choice(list(products.keys()))
    base_price = products[product]
    
    # Add some price variation (±20%)
    price = base_price * (1 + np.random.uniform(-0.2, 0.2))
    quantity = np.random.randint(1, 6)
    
    # Customer info
    customer_id = f"CUST{1000 + np.random.randint(0, 200)}"
    
    # Sales rep
    sales_rep = np.random.choice(['Alice Johnson', 'Bob Smith', 'Charlie Brown', 
                                 'Diana Wilson', 'Eve Davis'])
    
    # Region
    region = np.random.choice(['North', 'South', 'East', 'West', 'Central'])
    
    sales_data.append({
        'SaleID': f"S{10000 + i}",
        'Date': sale_date.strftime('%Y-%m-%d'),
        'Product': product,
        'Quantity': quantity,
        'UnitPrice': round(price, 2),
        'CustomerID': customer_id,
        'SalesRep': sales_rep,
        'Region': region
    })

# Create DataFrame
df_sales = pd.DataFrame(sales_data)
df_sales.to_csv('../data/project/sales_data.csv', index=False)

print(f"✅ Generated {len(df_sales)} sales records")
print("Sample data:")
print(df_sales.head())

# ============================================================================
# 2. DATA LOADING AND EXPLORATION
# ============================================================================

print("\n2. Data Loading and Initial Exploration")
print("-" * 30)

# Load the data
df = pd.read_csv('../data/project/sales_data.csv')

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

print("Dataset Information:")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"\nData types:")
print(df.dtypes)

print(f"\nFirst 5 rows:")
print(df.head())

print(f"\nLast 5 rows:")
print(df.tail())

print(f"\nBasic statistics:")
print(df.describe())

# Check for missing values
print(f"\nMissing values:")
print(df.isnull().sum())

# ============================================================================
# 3. DATA CLEANING AND VALIDATION
# ============================================================================

print("\n3. Data Cleaning and Validation")
print("-" * 30)

# Check for duplicates
duplicates = df.duplicated()
print(f"Duplicate rows: {duplicates.sum()}")

# Validate data ranges
print(f"\nData validation:")
print(f"Quantity range: {df['Quantity'].min()} - {df['Quantity'].max()}")
print(f"Price range: ${df['UnitPrice'].min():.2f} - ${df['UnitPrice'].max():.2f}")

# Check for invalid values
invalid_quantity = df[df['Quantity'] <= 0]
invalid_price = df[df['UnitPrice'] <= 0]

print(f"Invalid quantities: {len(invalid_quantity)}")
print(f"Invalid prices: {len(invalid_price)}")

# Check unique values in categorical columns
print(f"\nUnique products: {df['Product'].nunique()}")
print(f"Products: {df['Product'].unique()}")

print(f"\nUnique regions: {df['Region'].nunique()}")
print(f"Regions: {df['Region'].unique()}")

print(f"\nUnique sales reps: {df['SalesRep'].nunique()}")
print(f"Sales reps: {df['SalesRep'].unique()}")

# ============================================================================
# 4. DATA ENRICHMENT - ADDING CALCULATED COLUMNS
# ============================================================================

print("\n4. Adding Calculated Columns")
print("-" * 30)

# Calculate total value for each sale
df['TotalValue'] = df['Quantity'] * df['UnitPrice']

# Extract date components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter
df['DayOfWeek'] = df['Date'].dt.day_name()
df['WeekOfYear'] = df['Date'].dt.isocalendar().week

# Add product categories
def categorize_product(product):
    if product in ['Laptop', 'Tablet']:
        return 'Computing'
    elif product in ['Mouse', 'Keyboard']:
        return 'Input Devices'
    elif product in ['Monitor']:
        return 'Display'
    elif product in ['Headphones', 'Speaker']:
        return 'Audio'
    else:
        return 'Accessories'

df['Category'] = df['Product'].apply(categorize_product)

# Add size classification based on total value
def classify_sale_size(total_value):
    if total_value >= 1000:
        return 'Large'
    elif total_value >= 500:
        return 'Medium'
    else:
        return 'Small'

df['SaleSize'] = df['TotalValue'].apply(classify_sale_size)

print("Added calculated columns:")
print(df[['SaleID', 'Product', 'Quantity', 'UnitPrice', 'TotalValue', 
          'Category', 'Quarter', 'SaleSize']].head())

# ============================================================================
# 5. ANALYSIS AND INSIGHTS
# ============================================================================

print("\n5. Data Analysis and Insights")
print("-" * 30)

# Total sales overview
total_revenue = df['TotalValue'].sum()
total_items_sold = df['Quantity'].sum()
average_order_value = df['TotalValue'].mean()

print(f"📊 SALES OVERVIEW:")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Items Sold: {total_items_sold:,}")
print(f"Average Order Value: ${average_order_value:.2f}")
print(f"Number of Transactions: {len(df):,}")

# Analysis by Product
print(f"\n📈 PRODUCT ANALYSIS:")
product_analysis = df.groupby('Product').agg({
    'Quantity': 'sum',
    'TotalValue': ['sum', 'mean'],
    'SaleID': 'count'
}).round(2)

product_analysis.columns = ['Total_Quantity', 'Total_Revenue', 'Avg_Order_Value', 'Num_Orders']
product_analysis = product_analysis.sort_values('Total_Revenue', ascending=False)
print(product_analysis)

# Analysis by Category
print(f"\n📊 CATEGORY ANALYSIS:")
category_analysis = df.groupby('Category').agg({
    'TotalValue': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
}).round(2)

category_analysis.columns = ['Total_Revenue', 'Avg_Order_Value', 'Num_Orders', 'Total_Quantity']
category_analysis = category_analysis.sort_values('Total_Revenue', ascending=False)
print(category_analysis)

# Analysis by Sales Rep
print(f"\n👥 SALES REP PERFORMANCE:")
rep_analysis = df.groupby('SalesRep').agg({
    'TotalValue': ['sum', 'mean', 'count']
}).round(2)

rep_analysis.columns = ['Total_Sales', 'Avg_Order_Value', 'Num_Orders']
rep_analysis = rep_analysis.sort_values('Total_Sales', ascending=False)
print(rep_analysis)

# Analysis by Region
print(f"\n🌍 REGIONAL ANALYSIS:")
region_analysis = df.groupby('Region').agg({
    'TotalValue': ['sum', 'mean'],
    'SaleID': 'count'
}).round(2)

region_analysis.columns = ['Total_Revenue', 'Avg_Order_Value', 'Num_Orders']
region_analysis = region_analysis.sort_values('Total_Revenue', ascending=False)
print(region_analysis)

# Time-based analysis
print(f"\n📅 MONTHLY SALES TREND:")
monthly_sales = df.groupby(['Year', 'Month']).agg({
    'TotalValue': 'sum',
    'SaleID': 'count'
}).round(2)

monthly_sales.columns = ['Revenue', 'Orders']
print(monthly_sales.tail(10))  # Show last 10 months

# Day of week analysis
print(f"\n📆 SALES BY DAY OF WEEK:")
dow_analysis = df.groupby('DayOfWeek').agg({
    'TotalValue': ['sum', 'mean'],
    'SaleID': 'count'
}).round(2)

dow_analysis.columns = ['Total_Revenue', 'Avg_Order_Value', 'Num_Orders']
# Reorder by day of week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_analysis = dow_analysis.reindex(day_order)
print(dow_analysis)

# ============================================================================
# 6. ADVANCED ANALYSIS
# ============================================================================

print("\n6. Advanced Analysis")
print("-" * 30)

# Customer analysis
print(f"🛒 CUSTOMER ANALYSIS:")
customer_analysis = df.groupby('CustomerID').agg({
    'TotalValue': ['sum', 'mean', 'count'],
    'Date': ['min', 'max']
}).round(2)

customer_analysis.columns = ['Total_Spent', 'Avg_Order', 'Num_Orders', 'First_Purchase', 'Last_Purchase']

# Calculate customer lifetime (days between first and last purchase)
customer_analysis['Days_Active'] = (
    pd.to_datetime(customer_analysis['Last_Purchase']) - 
    pd.to_datetime(customer_analysis['First_Purchase'])
).dt.days

# Classify customers
def classify_customer(row):
    if row['Total_Spent'] >= 2000 and row['Num_Orders'] >= 5:
        return 'VIP'
    elif row['Total_Spent'] >= 1000 or row['Num_Orders'] >= 3:
        return 'Regular'
    else:
        return 'Occasional'

customer_analysis['Customer_Type'] = customer_analysis.apply(classify_customer, axis=1)

print("Top 10 customers by total spent:")
print(customer_analysis.sort_values('Total_Spent', ascending=False).head(10))

print(f"\nCustomer distribution:")
print(customer_analysis['Customer_Type'].value_counts())

# Product correlation analysis
print(f"\n🔗 PRODUCT CORRELATION:")
# Create pivot table for product correlation
product_customer = df.pivot_table(
    index='CustomerID', 
    columns='Product', 
    values='Quantity', 
    aggfunc='sum', 
    fill_value=0
)

# Calculate correlation
product_corr = product_customer.corr()
print("Products often bought together (correlation > 0.3):")
for i in range(len(product_corr.columns)):
    for j in range(i+1, len(product_corr.columns)):
        corr_value = product_corr.iloc[i, j]
        if corr_value > 0.3:
            print(f"{product_corr.columns[i]} & {product_corr.columns[j]}: {corr_value:.3f}")

# ============================================================================
# 7. CREATING SUMMARY REPORTS
# ============================================================================

print("\n7. Creating Summary Reports")
print("-" * 30)

# Executive Summary
executive_summary = {
    'Metric': [
        'Total Revenue',
        'Total Orders',
        'Average Order Value',
        'Total Customers',
        'Best Selling Product',
        'Top Sales Rep',
        'Best Region',
        'Peak Sales Month'
    ],
    'Value': [
        f"${total_revenue:,.2f}",
        f"{len(df):,}",
        f"${average_order_value:.2f}",
        f"{df['CustomerID'].nunique():,}",
        product_analysis.index[0],
        rep_analysis.index[0],
        region_analysis.index[0],
        monthly_sales.idxmax()[0]  # Month with highest revenue
    ]
}

summary_df = pd.DataFrame(executive_summary)
print("📋 EXECUTIVE SUMMARY:")
print(summary_df.to_string(index=False))

# Create detailed reports
print(f"\n📁 Creating detailed reports...")

# Save main dataset with calculated columns
df.to_csv('output/sales_data_enhanced.csv', index=False)
print("✅ Saved enhanced sales data")

# Save analysis results
product_analysis.to_csv('output/product_analysis.csv')
print("✅ Saved product analysis")

category_analysis.to_csv('output/category_analysis.csv')
print("✅ Saved category analysis")

rep_analysis.to_csv('output/sales_rep_performance.csv')
print("✅ Saved sales rep performance")

region_analysis.to_csv('output/regional_analysis.csv')
print("✅ Saved regional analysis")

customer_analysis.to_csv('output/customer_analysis.csv')
print("✅ Saved customer analysis")

monthly_sales.to_csv('output/monthly_trends.csv')
print("✅ Saved monthly trends")

summary_df.to_csv('output/executive_summary.csv', index=False)
print("✅ Saved executive summary")

# ============================================================================
# 8. DATA QUALITY REPORT
# ============================================================================

print("\n8. Data Quality Report")
print("-" * 30)

quality_report = {
    'Check': [
        'Total Records',
        'Duplicate Records',
        'Missing Values',
        'Invalid Quantities',
        'Invalid Prices',
        'Date Range',
        'Unique Customers',
        'Unique Products'
    ],
    'Result': [
        len(df),
        df.duplicated().sum(),
        df.isnull().sum().sum(),
        len(df[df['Quantity'] <= 0]),
        len(df[df['UnitPrice'] <= 0]),
        f"{df['Date'].min()} to {df['Date'].max()}",
        df['CustomerID'].nunique(),
        df['Product'].nunique()
    ],
    'Status': [
        '✅ Good',
        '✅ Good' if df.duplicated().sum() == 0 else '⚠️ Check',
        '✅ Good' if df.isnull().sum().sum() == 0 else '⚠️ Check',
        '✅ Good' if len(df[df['Quantity'] <= 0]) == 0 else '❌ Issues',
        '✅ Good' if len(df[df['UnitPrice'] <= 0]) == 0 else '❌ Issues',
        '✅ Good',
        '✅ Good',
        '✅ Good'
    ]
}

quality_df = pd.DataFrame(quality_report)
print("📊 DATA QUALITY REPORT:")
print(quality_df.to_string(index=False))

quality_df.to_csv('output/data_quality_report.csv', index=False)
print("✅ Saved data quality report")

# ============================================================================
# 9. INSIGHTS AND RECOMMENDATIONS
# ============================================================================

print("\n9. Key Insights and Recommendations")
print("-" * 30)

insights = [
    f"💰 Total revenue of ${total_revenue:,.2f} from {len(df):,} orders",
    f"🏆 Top product: {product_analysis.index[0]} (${product_analysis.iloc[0]['Total_Revenue']:,.2f})",
    f"⭐ Best sales rep: {rep_analysis.index[0]} (${rep_analysis.iloc[0]['Total_Sales']:,.2f})",
    f"🌟 Best region: {region_analysis.index[0]} (${region_analysis.iloc[0]['Total_Revenue']:,.2f})",
    f"👥 {customer_analysis[customer_analysis['Customer_Type'] == 'VIP'].shape[0]} VIP customers identified",
    f"📈 Average order value: ${average_order_value:.2f}",
    f"🛒 {df['CustomerID'].nunique()} unique customers with repeat rate of {(customer_analysis['Num_Orders'] > 1).mean()*100:.1f}%"
]

recommendations = [
    "🎯 Focus marketing efforts on Computing and Audio categories (highest revenue)",
    "📞 Investigate why some sales reps are outperforming others",
    "🎁 Create loyalty program for VIP customers to increase retention",
    "📊 Analyze seasonal trends to optimize inventory",
    "🤝 Cross-sell complementary products (e.g., Mouse + Keyboard)",
    "📈 Focus on converting Occasional customers to Regular customers",
    "🌍 Investigate regional differences to replicate success"
]

print("🔍 KEY INSIGHTS:")
for insight in insights:
    print(f"  {insight}")

print(f"\n💡 RECOMMENDATIONS:")
for rec in recommendations:
    print(f"  {rec}")

# Save insights
insights_df = pd.DataFrame({
    'Type': ['Insight'] * len(insights) + ['Recommendation'] * len(recommendations),
    'Description': insights + recommendations
})

insights_df.to_csv('output/insights_and_recommendations.csv', index=False)
print("✅ Saved insights and recommendations")

# ============================================================================
# PROJECT COMPLETION
# ============================================================================

print(f"\n🎉 PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 50)

print(f"\n📁 Generated Files:")
output_files = [
    'sales_data_enhanced.csv - Enhanced dataset with calculated columns',
    'product_analysis.csv - Product performance analysis',
    'category_analysis.csv - Category performance analysis',
    'sales_rep_performance.csv - Sales representative performance',
    'regional_analysis.csv - Regional sales analysis',
    'customer_analysis.csv - Customer behavior analysis',
    'monthly_trends.csv - Monthly sales trends',
    'executive_summary.csv - Executive summary report',
    'data_quality_report.csv - Data quality assessment',
    'insights_and_recommendations.csv - Key insights and recommendations'
]

for file in output_files:
    print(f"  ✅ {file}")

print(f"\n🎯 What You've Accomplished:")
accomplishments = [
    "Created and loaded a realistic sales dataset",
    "Performed comprehensive data exploration",
    "Cleaned and validated data quality",
    "Added calculated columns for enhanced analysis",
    "Conducted multi-dimensional analysis (product, customer, time, region)",
    "Generated executive summaries and detailed reports",
    "Created actionable insights and recommendations",
    "Demonstrated professional data analysis workflow"
]

for acc in accomplishments:
    print(f"  ✅ {acc}")

print(f"\n🚀 Next Steps:")
next_steps = [
    "Try modifying the analysis parameters",
    "Add your own business questions and analysis",
    "Create visualizations using matplotlib or seaborn",
    "Build a dashboard using the generated data",
    "Apply these techniques to your own datasets"
]

for step in next_steps:
    print(f"  🎯 {step}")

print("\nCongratulations! You've completed a full data analysis project! 🎊")