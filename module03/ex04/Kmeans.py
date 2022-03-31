import numpy


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        # ... parameters control ...
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    @staticmethod
    def get_limits(X):
        limits = []
        for c in range(X.shape[1]):
            limits.append([X[:, c].min(), X[:, c].max()])
        return numpy.array(limits)

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        """
        pass

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        """
        pass
