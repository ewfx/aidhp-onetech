from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Example of sentiment analysis
text = "I absolutely love this product, it's amazing!"
result = sentiment_analyzer(text)
print(result)  

# Output: [{'label': 'POSITIVE', 'score': 0.999}]
