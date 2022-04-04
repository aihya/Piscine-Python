import matplotlib.pyplot as plt
from FileLoader import FileLoader
from pylab import rcParams
import seaborn as sns
import pandas

rcParams['figure.figsize'] = 10, 5
sns.set_theme(style='whitegrid')


class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        if isinstance(data, pandas.DataFrame) and isinstance(features, list):
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
            try:
                for feature in features:
                    sns.kdeplot(data[feature])
                    sns.kdeplot(data[feature])
                    sns.kdeplot(data[feature])
                plt.show()
            finally:
                return None

    @staticmethod
    def pair_plot(data, features):
        if isinstance(data, pandas.DataFrame) and isinstance(features, list):
            try:
                sns.pairplot(pandas.DataFrame([data[features[i]] for i in range(len(features))]).T)
                plt.show()
            finally:
                return None

    @staticmethod
    def box_plot(data, features):
        if isinstance(data, pandas.DataFrame) and isinstance(features, list):
            try:
                sns.boxplot(y=features[0], data=data, orient='v')
                # sns.boxplot(y=features[1], data=data, orient='v')
                # sns.boxplot(features[1], x=features[1], data=data)
                plt.show()
            finally:
                return None


if __name__ == "__main__":
    data = FileLoader.load('../athlete_events.csv')
    # MyPlotLib.histogram(data, ['Height', 'Weight', 'Age'])
    # MyPlotLib.density(data, ['Height', 'Weight'])
    # MyPlotLib.pair_plot(data, [])
    MyPlotLib.box_plot(data, ['Height', 'Weight'])