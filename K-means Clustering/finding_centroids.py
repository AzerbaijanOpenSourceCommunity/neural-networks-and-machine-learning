import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.patches as mpatches

X = np.array([[5,3],[10,15],[15,12],[24,10],[30,45],[85,70],[71,80],[60,78],[55,52],[80,91]])
plt.scatter(X[:,0],X[:,1])
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)


plt.scatter(X[:,0],X[:,1],c=kmeans.labels_,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="green", label="Clusters' center points")

red_patch = mpatches.Patch(color='red', label='Cluster points')
purple_patch = mpatches.Patch(color='purple',label='Another cluster points')
green_patch = mpatches.Patch(color='green',label="Clusters' centers")
plt.legend(handles=[red_patch,purple_patch,green_patch])
plt.title('Visualization of clusters & centroids')
plt.show()