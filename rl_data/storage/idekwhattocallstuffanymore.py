from pandas import DataFrame, concat
import collection.api_requests as api
from cleaning.cleaning import json_to_df

def get_games(keywords: dict, num_req: int, API_KEY: str) -> DataFrame:
    '''
    this function belongs not in here as it is doing no cleaning lol

    Args:
        

    Returns: 
        
    '''

    games = api.game_request(keywords, num_req, API_KEY)

    games = games.map(json_to_df)

    return concat([x for x in games]).reset_index(drop=True)