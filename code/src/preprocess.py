# Checking for missing values
print(customers_df.isnull().sum())

# Fill missing values or drop them based on your data
customers_df.fillna('Unknown', inplace=True)

# Convert columns to appropriate data types (e.g., dates)
purchase_history_df['date'] = pd.to_datetime(purchase_history_df['date'])
