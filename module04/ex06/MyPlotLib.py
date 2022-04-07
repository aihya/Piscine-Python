import matplotlib.pyplot as plt
# from FileLoader import FileLoader
from pylab import rcParams
import seaborn as sns
import pandas
import warnings

rcParams['figure.figsize'] = 10, 5


class MyPlotLib:

    def __init__(self):
        pass

    @staticmethod
    def histogram(data, features):
        if isinstance(data, pandas.DataFrame) and isinstance(features, list):
            with warnings.catch_warnings(record=True):
                try:
                    if len(features) > 1:
                        fig, axis = plt.subplots(1, len(features))
                        for i, ax in enumerate(list(axis)):
                            ax.hist(data[features[i]], edgecolor='black')
                            ax.set_title(features[i])
                    elif len(features) == 1:
                        plt.hist(data[features[0]], edgecolor='black')
                    plt.show()
                finally:
                    return None

    @staticmethod
    def density(data, features):
        if isinstance(data, pandas.DataFrame) and isinstance(features, list):
            with warnings.catch_warnings(record=True):
                try:
                    sns.kdeplot(data=data[features])
                    plt.show()
                finally:
                    return None

    @staticmethod
    def pair_plot(data, features):
        if isinstance(data, pandas.DataFrame) and isinstance(features, list):
            with warnings.catch_warnings(record=True):
                try:
                    sns.pairplot(data=data, vars=features, diag_kws={'bins': 20}, plot_kws={'s': 5})
                    plt.show()
                finally:
                    return None

    @staticmethod
    def box_plot(data, features):
        if isinstance(data, pandas.DataFrame) and isinstance(features, list):
            with warnings.catch_warnings(record=True):
                try:
                    plt.boxplot(data[features].dropna(), labels=features)
                    plt.show()
                finally:
                    return None


# if __name__ == "__main__":
#     data = FileLoader.load('../athlete_events.csv')
#     MyPlotLib.histogram(data, ['Height', 'Weight', 'Age'])
#     MyPlotLib.density(data, ['Height', 'Weight'])
#     MyPlotLib.pair_plot(data, ['Weight', 'Height'])
#     MyPlotLib.box_plot(data, ['Weight', 'Height'])