# data_processor.py

import pandas as pd

def process_sales_data(file_path):
    """
    Process sales data from CSV file
    """
    df = pd.read_csv(file_path)
    
    # Basic processing
    df['total_amount'] = df['quantity'] * df['unit_price']
    df['date'] = pd.to_datetime(df['date'])
    
    return df

def generate_report(df):
    """
    Generate basic sales report
    """
    summary = {
        'total_sales': df['total_amount'].sum(),
        'total_transactions': len(df)
    }
    
    return summary

if __name__ == "__main__":
    sales_df = process_sales_data('sales_data.csv')
    report = generate_report(sales_df)
    print(report)
