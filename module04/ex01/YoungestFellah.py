import pandas as pd

def youngestfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year. ### Pleeease fix your subjects.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    Returns:
    dct: dictionary with 2 keys for female and male athlete.
    """
    result = {'f': 'nan', 'm': 'nan'}
    if not isinstance(df, pd.DataFrame) or not isinstance(year, int):
        return result
    result['f'] = df.where(df.Sex == 'F').where(df.Year == year)['Age'].min()
    result['m'] = df.where(df.Sex == 'M').where(df.Year == year)['Age'].min()
    return result