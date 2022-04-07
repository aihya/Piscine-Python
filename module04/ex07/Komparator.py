import matplotlib.pyplot as plt
#from FileLoader import FileLoader
import seaborn as sns
import warnings
import pandas


class Komparator:

    def __init__(self, dataset):
        self.dataset = dataset

    def compare_box_plots(self, categorical_var, numerical_var):
        if isinstance(self.dataset, pandas.DataFrame):
            if isinstance(categorical_var, str) and isinstance(numerical_var, str):
                with warnings.catch_warnings(record=True):
                    try:
                        sns.boxplot(data=self.dataset, x=numerical_var, y=categorical_var)
                        plt.show()
                    finally:
                        return None

    def density(self, categorical_var, numerical_var):
        if isinstance(self.dataset, pandas.DataFrame):
            if isinstance(categorical_var, str) and isinstance(numerical_var, str):
                with warnings.catch_warnings(record=True):
                    try:
                        order = self.dataset
                        sns.kdeplot(data=self.dataset, x=numerical_var, hue=categorical_var)
                        plt.show()
                    finally:
                        return None

    def compare_histograms(self, categorical_var, numerical_var):
        if isinstance(self.dataset, pandas.DataFrame):
            if isinstance(categorical_var, str) and isinstance(numerical_var, str):
                with warnings.catch_warnings(record=True):
                    try:
                        sns.FacetGrid(self.dataset, col=categorical_var).map(sns.histplot, numerical_var)
                        plt.show()
                    finally:
                        return None

    # def compare_histograms(self, categorical_var, numerical_var):
    #     if isinstance(self.dataset, pandas.DataFrame):
    #         if isinstance(categorical_var, str) and isinstance(numerical_var, str):
    #             with warnings.catch_warnings(record=True):
    #                 try:
    #                     sns.histplot(data=self.dataset, x=numerical_var, hue=categorical_var)
    #                     plt.show()
    #                 finally:
    #                     return None

# if __name__ == "__main__":
#     k = Komparator(FileLoader.load('../athlete_events.csv'))
#     k.compare_box_plots('Sex', 'Age')
#     k.density('Sex', 'Height')
#     k.compare_histograms('Sex', 'Age')
