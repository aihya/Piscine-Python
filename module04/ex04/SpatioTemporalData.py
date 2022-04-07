import pandas
import warnings


class SpatioTemporalData:

    def __init__(self, data):
        self.df = data

    def when(self, location):
        if isinstance(location, str):
            with warnings.catch_warnings(record=True):
                city = self.df.where(self.df.City == location).dropna(how='all')
                return [int(year) for year in city.Year.drop_duplicates()]

    def where(self, date):
        if isinstance(date, int):
            with warnings.catch_warnings(record=True):
                year = self.df.where(self.df.Year == date).dropna(how='all')
                return list(year.City.drop_duplicates())
