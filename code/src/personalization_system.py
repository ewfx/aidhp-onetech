import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')


# Load dataset
df = pd.read_csv('customers.csv')

# Display the first few rows of the dataset
print(df.head())

# PreProcess the data
# Fill missing values if any
df.fillna("", inplace=True)

# Encode categorical variables such as 'Gender' and 'Location'
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df['Location'] = label_encoder.fit_transform(df['Location'])

# Calculate sentiment score based on 'Social_Media_Activity' column
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['Sentiment_Score'] = df['Social_Media_Activity'].apply(get_sentiment)


#Feature Engineering
# Assume we have a simple recommendation model that returns products based on sentiment and preferences
def recommend_products(customer_row):
    recommendations = []
    if customer_row['Sentiment_Score'] > 0.5:
        recommendations.append('Fitness Tracker')
    else:
        recommendations.append('Coffee Machine')
    
    return recommendations

df['Recommended_Products'] = df.apply(recommend_products, axis=1)


#Geneerate Insights
# Visualize the sentiment score by age group
sns.boxplot(x='Age', y='Sentiment_Score', data=df)
plt.title('Sentiment Score by Age Group')
plt.show()

# Visualize purchase preferences by gender
sns.countplot(x='Product_Preference', hue='Gender', data=df)
plt.title('Product Preferences by Gender')
plt.xticks(rotation=45)
plt.show()


