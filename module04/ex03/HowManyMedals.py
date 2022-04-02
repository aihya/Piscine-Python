import pandas


def howManyMedals(df, name):
    if not isinstance(df, pandas.DataFrame) or not isinstance(name, str):
        return None
    medals = {}
    target = df.where(df.Name == name).dropna(how='all')
    years = target.drop_duplicates(subset=['Year'])['Year']
    for year in years:
        medals[year] = {'G': 0, 'S': 0, 'B': 0}
        medals[year]['G'] = target.where(target.Year == year).where(target.Medal == 'Gold').dropna(how='all').shape[0]
        medals[year]['S'] = target.where(target.Year == year).where(target.Medal == 'Silver').dropna(how='all').shape[0]
        medals[year]['B'] = target.where(target.Year == year).where(target.Medal == 'Bronze').dropna(how='all').shape[0]
    return medals
