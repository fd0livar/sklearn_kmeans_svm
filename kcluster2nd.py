import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

# x = [1, 5, 1.5, 8, 1, 9]
# y = [2, 8, 1.8, 8, 0.6, 11]

X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])  # sklearn expects numpy arrays
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)  # we fit the data to sklearn, so we can learn from it

centroids = kmeans.cluster_centers_  # we grab the values found from the fit
labels = kmeans.labels_

print(np.size(centroids), centroids)
print(np.size(labels), labels)
# print(len(X))

colors = ["g.", "r.", "c.", "y."]

for i in range(len(X)):
    print('coordinate:', X[i], 'label:', labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=50, linewidths=5, zorder=10)

plt.show()
