import matplotlib.pyplot as plt
import seaborn as sns

# Example: Visualize age distribution of customers
sns.histplot(customers_df['age'], kde=True)
plt.title("Customer Age Distribution")
plt.show()
