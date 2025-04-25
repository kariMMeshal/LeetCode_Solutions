import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    rslt = views[ views['author_id'] == views['viewer_id']  ].rename(columns={'author_id':'id'})
    rslt.drop_duplicates(inplace=True ,subset=['id'])
    rslt.sort_values(by=['id']  , inplace=True)
    return rslt[['id']]