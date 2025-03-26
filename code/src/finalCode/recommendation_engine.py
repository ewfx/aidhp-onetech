from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd

# Load data
df = pd.read_csv('customer_data.csv')

# Feature matrix based on Age, Income, Sentiment
features = df[['Age', 'Income', 'Sentiment']].values

# Fit the nearest neighbor model
knn = NearestNeighbors(n_neighbors=3, metric='cosine')
knn.fit(features)

# Find similar customers to Customer 1
customer_id = 0  # Customer 1
distances, indices = knn.kneighbors([features[customer_id]])

# Display recommendations
print(f"Recommendations for Customer {customer_id + 1}:")
for idx in indices[0]:
    print(f"- Customer {idx + 1}: {df.iloc[idx]['ProductCategory']}")
