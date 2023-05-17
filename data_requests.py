import requests
from pandas import DataFrame, Series, json_normalize, read_csv
from time import sleep

def get_games(parameters: dict, api_key: str) -> DataFrame:

    api_request = requests.get('https://ballchasing.com/api/replays', params=parameters, headers={'Authorization': api_key})
    request_json = api_request.json()

    df = json_normalize(request_json, record_path=['list'], sep='.')
    
    df = df.drop(['blue.players','orange.players'], axis=1)

    for column_name in ['blue_team','blue_player1','blue_player2','orange_team','orange_player1','orange_player2']:
        df.insert(df.columns.size, column_name, Series(None, dtype='object'))

    return df


def get_players_csv(id: str) -> DataFrame:

    try:
        df = read_csv(f'https://ballchasing.com/dl/stats/players/{id}/{id}-players.csv', sep=';')
    except:
        sleep(5)
        df = read_csv(f'https://ballchasing.com/dl/stats/players/{id}/{id}-players.csv', sep=';')

    df = df.T

    return df


def get_teams_csv(id: str) -> DataFrame:

    try:
        df = read_csv(f'https://ballchasing.com/dl/stats/teams/{id}/{id}-team-stats.csv', sep=';') # need to build in error handlding to the function here
    except:
        sleep(5)
        df = read_csv(f'https://ballchasing.com/dl/stats/teams/{id}/{id}-team-stats.csv', sep=';')
    
    df = df.set_index('color').T

    return df