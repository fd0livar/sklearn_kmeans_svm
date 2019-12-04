import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

centers = [[1, 1], [5, 5], [3, 10]]
X, _ = make_blobs(n_samples=500, centers=centers, cluster_std=1)
