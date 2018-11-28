import matplotlib.pyplot as plt
import numpy as np
import sys
from sklearn.cluster import KMeans

X = np.array([[5,3],[10,15],[15,12],[24,10],[30,45],[85,70],[71,80],[60,78],[55,52],[80,91]])
plt.scatter(X[:,0],X[:,1],label="True Position")
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.scatter(X[:,0],X[:,1],c=kmeans.labels_,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="black")
plt.show()
url = str(sys.argv[1:])
url2 = sys.argv[1]
print(url ,url2)