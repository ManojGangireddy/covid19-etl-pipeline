import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load cleaned data
df = pd.read_csv("clean_covid_data.csv")

# KMeans clustering using cases and deaths
features = df[['cases', 'deaths']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(features)

# Save with clusters
df.to_csv("clustered_covid_data.csv", index=False)

# Scatter plot with annotations
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='cases', y='deaths', hue='cluster', palette='Set2', s=100)

# Annotate countries
for i in range(len(df)):
    plt.text(df['cases'].iloc[i], df['deaths'].iloc[i], df['country'].iloc[i], fontsize=7)

plt.title("COVID-19 Clusters by Cases and Deaths")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.legend(title='Cluster')
plt.tight_layout()
plt.savefig("clustering_plot.png")
plt.show()
