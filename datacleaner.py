import pandas as pd
def clean_data(df):
			# Basic cleaning
			df = df.dropna()
		df = df.drop_duplicates()
def analyze_dataset(df: pd.DataFrame,
                   numeric_cols: Optional[List[str]] = None,
                   categorical_cols: Optional[List[str]] = None,
                   target_col: Optional[str] = None) -> dict:
