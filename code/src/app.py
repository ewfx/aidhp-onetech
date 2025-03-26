import pandas as pd

# Load the CSV files into DataFrames
customers_df = pd.read_csv('src/data/customers.csv')
# purchase_history_df = pd.read_csv('src/data/purchase_history.csv')
# social_media_df = pd.read_csv('src/data/social_media_activity.csv')
# sentiment_df = pd.read_csv('src/data/sentiment_analysis.csv')

# Check the first few rows of the data
print(customers_df.head())
