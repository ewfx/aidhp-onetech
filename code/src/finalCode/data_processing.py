import pandas as pd

# Load the dataset
df = pd.read_csv('customer_data.csv')

# Preprocess: Clean data and extract sentiment
df['Sentiment'] = df['ReviewSentiment'].apply(lambda x: 1 if x == 'Positive' else 0 if x == 'Negative' else 0.5)

# Preview the dataset
print(df.head())
