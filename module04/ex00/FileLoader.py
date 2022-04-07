import pandas as pd


class FileLoader:

    @staticmethod
    def load(path):
        if isinstance(path, str):
            try:
                data = pd.read_csv(path, sep=',')
                print(f'Loading data set of dimensions: {data.shape[0]} x {data.shape[1]}')
                return data
            except FileNotFoundError:
                return None

    @staticmethod
    def display(df, n):
        if isinstance(df, pd.DataFrame) and isinstance(n, int):
            if n >= 0:
                print(df[:n])
            else:
                print(df[df.shape[0] + n:])
