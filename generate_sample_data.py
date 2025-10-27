import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def create_sample_datasets():
    """Create sample datasets for demonstration"""
    
    # Create data directory
    os.makedirs('sample_data', exist_ok=True)
    
    # 1. Sales Dataset
    np.random.seed(42)
    n_sales = 1000
    
    # Generate sample sales data
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]
    
    sales_data = {
        'Date': np.random.choice(dates, n_sales),
        'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Mouse', 'Keyboard'], n_sales),
        'Category': np.random.choice(['Electronics', 'Accessories', 'Computers'], n_sales),
        'Sales_Amount': np.random.normal(500, 200, n_sales).clip(50, 2000),
        'Quantity': np.random.randint(1, 10, n_sales),
        'Customer_Age': np.random.randint(18, 70, n_sales),
        'Customer_Gender': np.random.choice(['Male', 'Female', 'Other'], n_sales),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], n_sales),
        'Discount': np.random.uniform(0, 0.3, n_sales),
        'Satisfaction_Score': np.random.randint(1, 6, n_sales)
    }
    
    sales_df = pd.DataFrame(sales_data)
    sales_df['Total_Amount'] = sales_df['Sales_Amount'] * sales_df['Quantity'] * (1 - sales_df['Discount'])
    sales_df['Date'] = pd.to_datetime(sales_df['Date'])
    sales_df = sales_df.sort_values('Date').reset_index(drop=True)
    
    # Introduce some missing values for demonstration
    missing_indices = np.random.choice(sales_df.index, size=50, replace=False)
    sales_df.loc[missing_indices, 'Satisfaction_Score'] = np.nan
    
    sales_df.to_csv('sample_data/sales_data.csv', index=False)
    print("✅ Created sales_data.csv")
    
    # 2. Employee Dataset
    n_employees = 500
    
    employee_data = {
        'Employee_ID': range(1, n_employees + 1),
        'Name': [f'Employee_{i}' for i in range(1, n_employees + 1)],
        'Department': np.random.choice(['HR', 'Engineering', 'Sales', 'Marketing', 'Finance'], n_employees),
        'Position': np.random.choice(['Junior', 'Senior', 'Manager', 'Director'], n_employees),
        'Salary': np.random.normal(75000, 25000, n_employees).clip(30000, 200000),
        'Years_Experience': np.random.randint(0, 20, n_employees),
        'Age': np.random.randint(22, 65, n_employees),
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_employees),
        'Remote_Work': np.random.choice([True, False], n_employees),
        'Performance_Score': np.random.uniform(2.0, 5.0, n_employees),
        'Bonus': np.random.uniform(0, 20000, n_employees)
    }
    
    employee_df = pd.DataFrame(employee_data)
    
    # Make salary somewhat correlated with experience and position
    position_multiplier = {'Junior': 0.8, 'Senior': 1.0, 'Manager': 1.4, 'Director': 2.0}
    for pos, mult in position_multiplier.items():
        mask = employee_df['Position'] == pos
        employee_df.loc[mask, 'Salary'] *= mult
    
    # Add some correlation between experience and salary
    employee_df['Salary'] += employee_df['Years_Experience'] * 2000
    
    # Introduce some missing values
    missing_indices = np.random.choice(employee_df.index, size=30, replace=False)
    employee_df.loc[missing_indices, 'Bonus'] = np.nan
    
    employee_df.to_csv('sample_data/employee_data.csv', index=False)
    print("✅ Created employee_data.csv")
    
    # 3. Stock Market Dataset
    n_days = 252  # Trading days in a year
    
    # Generate stock price data for multiple companies
    companies = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    stock_data = []
    
    for company in companies:
        # Generate stock prices with some randomness
        initial_price = np.random.uniform(100, 300)
        prices = [initial_price]
        
        for i in range(n_days - 1):
            # Random walk with slight upward trend
            change = np.random.normal(0.001, 0.02)  # Small daily change
            new_price = prices[-1] * (1 + change)
            prices.append(max(new_price, 1))  # Ensure price doesn't go below $1
        
        volumes = np.random.lognormal(15, 0.5, n_days)  # Log-normal distribution for volume
        
        for i, (price, volume) in enumerate(zip(prices, volumes)):
            stock_data.append({
                'Date': start_date + timedelta(days=i),
                'Company': company,
                'Close_Price': price,
                'Volume': int(volume),
                'High_Price': price * np.random.uniform(1.0, 1.05),
                'Low_Price': price * np.random.uniform(0.95, 1.0),
                'Market_Cap': price * np.random.uniform(1e9, 1e12)  # Simplified market cap
            })
    
    stock_df = pd.DataFrame(stock_data)
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    stock_df['Price_Change'] = stock_df.groupby('Company')['Close_Price'].pct_change()
    
    stock_df.to_csv('sample_data/stock_data.csv', index=False)
    print("✅ Created stock_data.csv")
    
    # 4. Customer Survey Dataset
    n_responses = 800
    
    survey_data = {
        'Response_ID': range(1, n_responses + 1),
        'Age_Group': np.random.choice(['18-25', '26-35', '36-45', '46-55', '56+'], n_responses),
        'Income_Level': np.random.choice(['Low', 'Medium', 'High'], n_responses),
        'Product_Usage': np.random.choice(['Daily', 'Weekly', 'Monthly', 'Rarely'], n_responses),
        'Satisfaction_Rating': np.random.randint(1, 11, n_responses),  # 1-10 scale
        'Recommendation_Score': np.random.randint(0, 11, n_responses),  # NPS score 0-10
        'Customer_Service_Rating': np.random.randint(1, 6, n_responses),  # 1-5 scale
        'Price_Perception': np.random.choice(['Too Expensive', 'Fair', 'Good Value'], n_responses),
        'Brand_Loyalty': np.random.choice(['Very Low', 'Low', 'Medium', 'High', 'Very High'], n_responses),
        'Purchase_Frequency': np.random.randint(1, 12, n_responses),  # Times per year
        'Online_Purchase': np.random.choice([True, False], n_responses, p=[0.7, 0.3])
    }
    
    survey_df = pd.DataFrame(survey_data)
    
    # Add some correlations to make the data more realistic
    # Higher satisfaction should correlate with higher recommendation
    mask = survey_df['Satisfaction_Rating'] >= 8
    survey_df.loc[mask, 'Recommendation_Score'] = np.random.randint(7, 11, mask.sum())
    
    # Introduce missing values in some columns
    missing_indices = np.random.choice(survey_df.index, size=40, replace=False)
    survey_df.loc[missing_indices, 'Income_Level'] = np.nan
    
    survey_df.to_csv('sample_data/customer_survey.csv', index=False)
    print("✅ Created customer_survey.csv")
    
    # 5. IoT Sensor Dataset
    n_readings = 2000
    
    # Generate timestamp data for hourly readings over ~83 days
    timestamps = pd.date_range(start='2023-01-01', periods=n_readings, freq='H')
    
    sensor_data = {
        'Timestamp': timestamps,
        'Sensor_ID': np.random.choice(['TEMP_01', 'TEMP_02', 'HUM_01', 'HUM_02', 'PRESS_01'], n_readings),
        'Temperature': np.random.normal(22, 5, n_readings) + 3 * np.sin(np.arange(n_readings) * 2 * np.pi / 24),  # Daily cycle
        'Humidity': np.random.normal(45, 10, n_readings).clip(0, 100),
        'Pressure': np.random.normal(1013, 20, n_readings),
        'Location': np.random.choice(['Building_A', 'Building_B', 'Building_C'], n_readings),
        'Floor': np.random.choice([1, 2, 3, 4, 5], n_readings),
        'Room_Type': np.random.choice(['Office', 'Conference', 'Storage', 'Laboratory'], n_readings),
        'Occupancy': np.random.randint(0, 20, n_readings),
        'Alert_Status': np.random.choice(['Normal', 'Warning', 'Critical'], n_readings, p=[0.85, 0.12, 0.03])
    }
    
    sensor_df = pd.DataFrame(sensor_data)
    
    # Add some sensor malfunctions (missing data)
    malfunction_indices = np.random.choice(sensor_df.index, size=100, replace=False)
    sensor_df.loc[malfunction_indices, 'Temperature'] = np.nan
    
    sensor_df.to_csv('sample_data/iot_sensor_data.csv', index=False)
    print("✅ Created iot_sensor_data.csv")
    
    print(f"\n🎉 All sample datasets created in 'sample_data/' directory!")
    print(f"📊 Total datasets: 5")
    print(f"📈 Total records: {len(sales_df) + len(employee_df) + len(stock_df) + len(survey_df) + len(sensor_df):,}")

if __name__ == "__main__":
    create_sample_datasets()