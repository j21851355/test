import pandas as pd
def clean_data(df):
			# Basic cleaning
			df = df.dropna()
		df = df.drop_duplicates()
