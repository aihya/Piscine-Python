import pandas


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
    if not isinstance(df, pandas.DataFrame) or not isinstance(year, int):
        return result
    result = df.where(df.Year == year)
    result['f'] = result.where(result.Sex == 'F')['Age'].min()
    result['m'] = result.where(result.Sex == 'M')['Age'].min()
    return result