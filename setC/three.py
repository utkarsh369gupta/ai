import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Hardcoded dataset
data = {
    "Income": [40000, 50000, 60000, 70000, 80000, 30000, 90000, 100000, 110000, 120000],
    "Age": [22, 25, 30, 35, 40, 20, 45, 50, 55, 60],
    "Spending Score": [65, 55, 50, 40, 45, 70, 30, 20, 15, 10]
}
df = pd.DataFrame(data)

# Preprocess the data (scale the features)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize the clusters using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Income'], df['Spending Score'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.title('K-Means Clustering')
plt.colorbar(label='Cluster')
plt.show()
