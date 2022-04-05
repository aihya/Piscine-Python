import numpy
import pandas
import argparse
import time
import matplotlib.pyplot as plt
import copy


def progress(it):
    start = time.time()
    t1 = 0.0
    t2 = 0.0
    for c in it:
        eta = (t2 - t1) * (it[-1] - c)
        per = ((c * 100) // it[-1])
        prg = "{}>".format('=' * ((int(per) // 5) - 1))
        div = "{}/{}".format(c+1, it[-1]+1)
        et = time.time() - start

        print("\033[2KETA: {:.2f}s [{:3.0f}%] [{:20}] {} | elapsed time {:.2f}s\r".format(eta, per, prg, div, et), end='')

        t1 = time.time()
        yield c
        t2 = time.time()

def variance(centroids):
    centroids = numpy.array([c for c in centroids if len(c)])
    means = numpy.array([col.mean() for col in centroids.T])
    # return numpy.sum([(centroid - means) ** 2 for centroid in centroids]) / len(centroids)
    return numpy.sum([KmeansClustering.euclidean(cent, means) for cent in centroids]) / len(centroids)


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        assert type(max_iter) == int and type(ncentroid) == int, None
        assert max_iter > 0, "max_iter must be positive non-null number."
        assert ncentroid > 0, "ncentroid must be positive non-null number."
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    @staticmethod
    def get_limits(X):
        """
        Calculate the boundaries of every column in X.
        Args:
            X: a numpy.ndarray, a matrix of dimension m * n
        Returns:
            A numpy.ndarray containing the min & max values of every column.
        """
        limits = []
        for c in range(X.shape[1]):
            limits.append([X[:, c].min(), X[:, c].max()])
        return numpy.array(limits)

    @staticmethod
    def euclidean(pos1, pos2):
        return numpy.sqrt(numpy.sum([(x1-x2)**2 for x1, x2 in zip(pos1, pos2)]))

    def init_centroids(self, limits):
        self.centroids = []
        for n in range(self.ncentroid):
            self.centroids.append([])
            for limit in limits:
                high = limit[1] - limit[0]
                low = limit[0]
                self.centroids[-1].append(numpy.random.random() * high + low)

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroid from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrix of dimension m * n.
        Returns:
            None.
        """

        # Initialize centroids.
        self.init_centroids(KmeansClustering.get_limits(X))
        # print("Initial centroids coordinates:")
        # for i, centroid in enumerate(self.centroids):
        #     print('Centroid {}:  {}'.format(i, centroid))
        for _ in range(self.max_iter):
            clusters = [[] for _ in range(self.ncentroid)]
            # Find target cluster of each point.
            # Compare the distance of each point with all centroids,
            # and put the point in the cluster corresponding to the closest centroid.
            for point in X:
                distances = [KmeansClustering.euclidean(point, cent) for cent in self.centroids if len(cent)]
                clusters[numpy.argmin(distances)].append(point)
            # Calculate the new positions of the centroids.
            for i, cluster in enumerate(clusters):
                # Calculate the mean of the clusters.
                self.centroids[i] = [col.mean() for col in numpy.array(cluster).T]

    def predict(self, X):
        """
        Predict from which cluster each data point belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrix of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        """
        predictions = []
        for point in X:
            distances = [KmeansClustering.euclidean(point, cent) for cent in self.centroids if len(cent)]
            predictions.append([numpy.argmin(distances)])
        return numpy.array(predictions)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='Path to .csv file')
    parser.add_argument('ncentroid', type=int, help='Number of centroids or clusters to create')
    parser.add_argument('max_iter', type=int, help='Maximum number of iterations.')
    parser.add_argument('epochs', type=int, help='Number of times to repeat the iterations.')
    args = parser.parse_args()

    kmc = KmeansClustering(args.max_iter, args.ncentroid)
    best_centroids = None
    best_variance = 1000000000
    try:
        data = numpy.array(pandas.read_csv(args.filepath, sep=',').iloc[:, 1:])

        for epoch in progress(range(args.epochs)):
            kmc.fit(data)

            invalid_centroids = False
            for c in kmc.centroids:
                if not c:
                    invalid_centroids = True

            if invalid_centroids:
                continue

            if best_centroids == None:
                best_centroids = copy.deepcopy(kmc.centroids)
                continue

            __variance = variance(kmc.centroids)
            if __variance < best_variance:
                print("\nNew Best Variance: {}".format(__variance))
                best_centroids = copy.deepcopy(kmc.centroids)
                best_variance = __variance

        kmc.centroids = best_centroids

    except FileNotFoundError as E:
        print("{}: {}".format(type(E).__name__, args.filepath))
        exit(1)
    except AssertionError:
        exit(1)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    colors = [[numpy.random.random(), numpy.random.random(), numpy.random.random()] for _ in range(args.ncentroid)]

    # Put all centroids on the scatter plot
    for i, centroid in enumerate(kmc.centroids):
        if len(centroid):
            ax.scatter(centroid[0], centroid[1], centroid[2], marker='^', color=colors[i], edgecolor='black', s=50)

    pred = kmc.predict(data)
    clusters = [0] * args.ncentroid

    # Put all data points on the scatter plot
    for i, p in enumerate(pred):
        ax.scatter(data[i][0], data[i][1], data[i][2], color=colors[p[0]], s=20)
        clusters[p[0]] += 1

    print("\nFinal centroids coordinates:")
    for i, centroid in enumerate(best_centroids):
        print('Centroid {} ({}):  {}'.format(i, clusters[i], centroid))

    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Density')
    plt.show()