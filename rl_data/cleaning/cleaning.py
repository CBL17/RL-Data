from typing import Any
from pandas import DataFrame, Series, json_normalize

def json_to_df(game: Any) -> DataFrame:
    '''
    Converts json game data into a DataFrame

    Args:
        game (Any): json data for a single game

    Returns: 
        Dataframe: contains game data
    '''

    return json_normalize(game, record_path=['list'], sep='.')


