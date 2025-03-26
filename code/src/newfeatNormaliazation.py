# Aggregate sentiment scores for each customer
sentiment_scores = sentiment_df.groupby('customer_id')['sentiment'].apply(lambda x: (x == 'positive').sum() - (x == 'negative').sum())
customers_df['sentiment_score'] = customers_df['customer_id'].map(sentiment_scores)

# Total spent by customer
total_spent = purchase_history_df.groupby('customer_id')['amount'].sum()
customers_df['total_spent'] = customers_df['customer_id'].map(total_spent)



from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Normalize 'age' and 'total_spent'
customers_df[['age', 'total_spent']] = scaler.fit_transform(customers_df[['age', 'total_spent']])




from sklearn.metrics.pairwise import cosine_similarity

# Example: Collaborative Filtering using similarity between customers
user_product_matrix = purchase_history_df.pivot(index='customer_id', columns='product_name', values='amount').fillna(0)
cosine_sim = cosine_similarity(user_product_matrix)

# Recommend products based on cosine similarity
def get_recommendations(user_id, top_n=5):
    user_index = user_product_matrix.index.get_loc(user_id)
    similarity_scores = cosine_sim[user_index]
    similar_users = similarity_scores.argsort()[-top_n:][::-1]  # Top N similar users
    return user_product_matrix.iloc[similar_users]

recommended_products = get_recommendations(1)  # Example for customer with ID=1
print(recommended_products)


from sklearn.metrics import mean_squared_error

# Assume true_ratings and predicted_ratings are lists of actual and predicted ratings.
rmse = mean_squared_error(true_ratings, predicted_ratings, squared=False)
print(f"RMSE: {rmse}")


# Example: Create customer segments based on total_spent
customers_df['segment'] = pd.cut(customers_df['total_spent'], bins=[0, 500, 1000, 2000], labels=['Low', 'Medium', 'High'])


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    recommendations = get_recommendations(user_id)
    return jsonify(recommendations.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
