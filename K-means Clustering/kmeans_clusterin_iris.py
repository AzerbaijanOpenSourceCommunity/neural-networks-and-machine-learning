import sklearn
from sklearn import cluster
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt

# Loading iris dataset
iris = load_iris()
X = iris.data[:, :2]  # use only sepal length & sepal width
y_iris = iris.target

km2 = cluster.KMeans(n_clusters=2).fit(X)
km3 = cluster.KMeans(n_clusters=3).fit(X)
km4 = cluster.KMeans(n_clusters=4).fit(X)

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.scatter(X[:,0], X[:, 1], c=km2.labels_)
plt.title("K = 2 , J =%.2f" % km2.inertia_)


plt.subplot(132)
plt.scatter(X[:,0], X[:, 1], c=km3.labels_)
plt.title("K = 3 , J =%.2f" % km3.inertia_)

plt.subplot(133)
plt.scatter(X[:,0], X[:, 1], c=km4.labels_)
plt.title("K = 4 , J =%.2f" % km4.inertia_)

plt.legend()
plt.show()

