import pandas

def proportionBySport(df, year, sport, sex):
    sel = df.where(df.Sex == sex).where(df.Year == year).where(df.Sport == sport)
    all = df.where(df.Sex == sex).where(df.Year == year)
    sel = sel.drop_duplicates(subset=['Name']).dropna(how='all')
    all = all.drop_duplicates(subset=['Name']).dropna(how='all')
    return sel.shape[0] / all.shape[0]
