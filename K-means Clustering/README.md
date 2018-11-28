
<h1>Simple K-means Clustering Examples</h1>
<p>K Means Clustering is an unsupervised learning algorithm that will attempt to group similar clusters in your data</p>
<p>The overall goal is to divide data into distinct groups such that observations within each group are similar</p> 

* First we import libraries
```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
```

* With these 2 lines below, we create an array and assign it to X , then we just visualize it with **matplotlib's scatter** method
```python
X = np.array([[5,3],[10,15],[15,12],[24,10],[30,45],[85,70],[71,80],[60,78],[55,52],[80,91]])
plt.scatter(X[:,0],X[:,1],label="True Position")
```
* After this, we use scikit-learn's **KMeans** class to find clusters' center points , we compute k-means clustering  with using **fit()** function, X parameter here is a **training instance** to cluster
```python
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
```
Finally, we can differ labels, and clusters' center points with painting those points in different colors.So , we use **scatter** function again.
You can find more about **scatter** function  [here](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html) 
```python
plt.scatter(X[:,0],X[:,1],c=kmeans.labels_,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="black")
```

<div align="center">
<h4 text-align='center'>Visualization of labels & clusters' centers</h4>
<img text-align='center' src='https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/k-means-clustering-visualization.png'>
</div>
