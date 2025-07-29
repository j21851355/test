# data_cleaner.py

import pandas as pd

def clean_data(df):
    # Basic cleaning
    df = df.dropna()
    df = df.drop_duplicates()
    return df

# Example usage
if __name__ == "__main__":
    df = pd.read_csv('data.csv')
    clean_df = clean_data(df)
    print("Rows after cleaning:", len(clean_df))
