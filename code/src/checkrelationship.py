# Example: Visualize correlation matrix for purchase amounts
sns.heatmap(purchase_history_df.corr(), annot=True)
plt.title("Purchase History Correlation Matrix")
plt.show()
