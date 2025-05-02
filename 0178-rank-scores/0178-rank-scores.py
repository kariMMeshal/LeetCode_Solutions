import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by='score' , inplace=True , ascending=False)
    scores.reset_index(inplace=True , drop=True )
    scores['rank'] = 1
    rank = 1
    for i in range (1, len(scores)):
        if(scores['score'][i] < scores['score'][i-1] ):
            rank+=1
        scores['rank'][i] = rank
        i+=1  
  
    return scores[['score','rank']]