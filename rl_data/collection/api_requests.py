from typing import Any
from requests import get
from pandas import DataFrame, json_normalize, read_csv, concat, Series

def game_request(keywords: dict, num_req: int, API_KEY: str) -> Series:
    '''
    Calls ballchasing API and converts the response to a json
    and puts it into a Series

    Args:
        keywords (dict): search criteria, required
        num_requests (int): number of times to call from API 
        API_KEY (str): key to access API, required

    Returns: 
        Series: game-by-game info in json
    '''

    games = Series()

    api_url = 'https://ballchasing.com/api/replays'


    for _ in range(num_req):
        
        request = get(api_url, params=keywords, headers={'Authorization': API_KEY}, timeout=10)
        request_json = request.json()

        games.at[games.size] = request_json

        api_url = request_json['next']

    return games


def stat_request(id: str, API_KEY: str) -> Any:
    '''Calls ballchasing API and converts the response to a json

    Parameters
    ----------
    id : str
        game id
    API_KEY : str
        key to access API

    Returns
    -------
    Any
        stats of game in json
    '''    

    request = get(f'https://ballchasing.com/api/replays/{id}', headers={'Authorization': API_KEY}, timeout=10)

    return request.json()

# def get_games(parameters: dict, api_key: str, num_requests: int) -> DataFrame:

#     api_url = 'https://ballchasing.com/api/replays'
#     df = DataFrame()

#     for UNUSED in range(num_requests):

#         del UNUSED

#         api_request = get(api_url, params=parameters, headers={'Authorization': api_key})
#         request_json = api_request.json()

#         api_url = request_json['next']

#         new_data = json_normalize(request_json, record_path=['list'], sep='.')

#         new_data = new_data.drop(['link', 'rocket_league_id', 'replay_title', 'map_code',
#        'playlist_id', 'playlist_name', 'duration', 'overtime', 'season',
#        'season_type', 'date', 'date_has_tz', 'visibility', 'created',
#        'min_rank.tier', 'min_rank.division', 'min_rank.name', 'min_rank.id',
#        'max_rank.tier', 'max_rank.division', 'max_rank.name', 'max_rank.id',
#        'uploader.steam_id', 'uploader.name', 'uploader.profile_url',
#        'uploader.avatar', 'blue.goals', 'map_name', 'orange.goals',
#        'overtime_seconds', 'blue.players', 'orange.players'], axis=1)
        
#         for column_name in ['link', 'created', 'status', 'rocket_league_id', 'match_guid',
#        'title', 'map_code', 'match_type', 'team_size', 'playlist_id',
#        'duration', 'overtime', 'season', 'season_type', 'date',
#        'date_has_timezone', 'visibility', 'playlist_name', 'map_name',
#        'uploader.steam_id', 'uploader.name', 'uploader.profile_url',
#        'uploader.avatar', 'min_rank.id', 'min_rank.tier', 'min_rank.division',
#        'min_rank.name', 'max_rank.id', 'max_rank.tier', 'max_rank.division',
#        'max_rank.name','blue_p1','blue_p2','orange_p1','orange_p2']:
#             new_data.insert(new_data.columns.size, column_name, None, False)
        
        # new_data = new_data.astype(dtype={})
        
#         df = concat([df, new_data]).reset_index(drop=True)

#     return df

# what i want to do i think is to make a function that gets the json then passes it for cleaning and whatnot 
# instead of this giant crigne ass function bs 

def get_game_info(id: str, api_key: str) -> DataFrame:

    api_request = get(f'https://ballchasing.com/api/replays/{id}', headers={'Authorization': api_key}, timeout=10)
    request_json = api_request.json()
    request_json.pop('blue')
    request_json.pop('orange')

    base = DataFrame(columns=[\
    'start_time',
    'end_time',
    'name',
    'car_id',
    'car_name',
    'mvp',
    'steering_sensitivity',
    'id.platform',
    'id.id',
    'camera.fov',
    'camera.height',
    'camera.pitch',
    'camera.distance',
    'camera.stiffness',
    'camera.swivel_speed',
    'camera.transition_speed',
    'stats.core.shots',
    'stats.core.shots_against',
    'stats.core.goals',
    'stats.core.goals_against',
    'stats.core.saves',
    'stats.core.assists',
    'stats.core.score',
    'stats.core.mvp',
    'stats.core.shooting_percentage',
    'stats.boost.bpm',
    'stats.boost.bcpm',
    'stats.boost.avg_amount',
    'stats.boost.amount_collected',
    'stats.boost.amount_stolen',
    'stats.boost.amount_collected_big',
    'stats.boost.amount_stolen_big',
    'stats.boost.amount_collected_small',
    'stats.boost.amount_stolen_small',
    'stats.boost.count_collected_big',
    'stats.boost.count_stolen_big',
    'stats.boost.count_collected_small',
    'stats.boost.count_stolen_small',
    'stats.boost.amount_overfill',
    'stats.boost.amount_overfill_stolen',
    'stats.boost.amount_used_while_supersonic',
    'stats.boost.time_zero_boost',
    'stats.boost.percent_zero_boost',
    'stats.boost.time_full_boost',
    'stats.boost.percent_full_boost',
    'stats.boost.time_boost_0_25',
    'stats.boost.time_boost_25_50',
    'stats.boost.time_boost_50_75',
    'stats.boost.time_boost_75_100',
    'stats.boost.percent_boost_0_25',
    'stats.boost.percent_boost_25_50',
    'stats.boost.percent_boost_50_75',
    'stats.boost.percent_boost_75_100',
    'stats.movement.avg_speed',
    'stats.movement.total_distance',
    'stats.movement.time_supersonic_speed',
    'stats.movement.time_boost_speed',
    'stats.movement.time_slow_speed',
    'stats.movement.time_ground',
    'stats.movement.time_low_air',
    'stats.movement.time_high_air',
    'stats.movement.time_powerslide',
    'stats.movement.count_powerslide',
    'stats.movement.avg_powerslide_duration',
    'stats.movement.avg_speed_percentage',
    'stats.movement.percent_slow_speed',
    'stats.movement.percent_boost_speed',
    'stats.movement.percent_supersonic_speed',
    'stats.movement.percent_ground',
    'stats.movement.percent_low_air',
    'stats.movement.percent_high_air',
    'stats.positioning.avg_distance_to_ball',
    'stats.positioning.avg_distance_to_ball_possession',
    'stats.positioning.avg_distance_to_ball_no_possession',
    'stats.positioning.avg_distance_to_mates',
    'stats.positioning.time_defensive_third',
    'stats.positioning.time_neutral_third',
    'stats.positioning.time_offensive_third',
    'stats.positioning.time_defensive_half',
    'stats.positioning.time_offensive_half',
    'stats.positioning.time_behind_ball',
    'stats.positioning.time_infront_ball',
    'stats.positioning.time_most_back',
    'stats.positioning.time_most_forward',
    'stats.positioning.goals_against_while_last_defender',
    'stats.positioning.time_closest_to_ball',
    'stats.positioning.time_farthest_from_ball',
    'stats.positioning.percent_defensive_third',
    'stats.positioning.percent_offensive_third',
    'stats.positioning.percent_neutral_third',
    'stats.positioning.percent_defensive_half',
    'stats.positioning.percent_offensive_half',
    'stats.positioning.percent_behind_ball',
    'stats.positioning.percent_infront_ball',
    'stats.positioning.percent_most_back',
    'stats.positioning.percent_most_forward',
    'stats.positioning.percent_closest_to_ball',
    'stats.positioning.percent_farthest_from_ball',
    'stats.demo.inflicted',
    'stats.demo.taken',
    'rank.id',
    'rank.tier',
    'rank.division',
    'rank.name'])
    blue = json_normalize(api_request.json(), record_path=[['blue','players']]).drop('mvp', axis=1, errors='ignore')
    orange = json_normalize(api_request.json(), record_path=[['orange','players']]).drop('mvp', axis=1, errors='ignore')
    player_stats = concat([base, blue, orange], ignore_index=True)

    abc = json_normalize(request_json)

    for i, col in enumerate(['blue_p1','blue_p2','orange_p1','orange_p2']):
        
        cam_set = sc.CameraSettings(*player_stats.T[player_stats.columns.str.contains('camera')][i])
        core_stat = sc.CoreStats(*player_stats.T[player_stats.columns.str.contains('stats.core')][i])
        boost_stat = sc.BoostStats(*player_stats.T[player_stats.columns.str.contains('stats.boost')][i])
        move_stat = sc.MovementStats(*player_stats.T[player_stats.columns.str.contains('stats.movement')][i])
        pos_stat = sc.PositioningStats(*player_stats.T[player_stats.columns.str.contains('stats.positioning')][i])

        abc[col] = Player(
            *player_stats.T.loc['start_time':'id.id',i],
            *player_stats.T[player_stats.columns.str.contains('stats.demo')][i],
            *player_stats.T[player_stats.columns.str.contains('rank.')][i],
            camera_settings=cam_set, core_stats=core_stat, boost_stats=boost_stat, movement_stats=move_stat, positioning_stats=pos_stat
        )


    return abc


# def get_players_csv(id: str) -> DataFrame:

#     try:
#         df = read_csv(f'https://ballchasing.com/dl/stats/players/{id}/{id}-players.csv', sep=';')
#     except:
#         sleep(5)
#         df = read_csv(f'https://ballchasing.com/dl/stats/players/{id}/{id}-players.csv', sep=';')

#     df = df.T

#     return df


# def get_teams_csv(id: str) -> DataFrame:

#     try:
#         df = read_csv(f'https://ballchasing.com/dl/stats/teams/{id}/{id}-team-stats.csv', sep=';')
#     except:
#         sleep(5)
#         df = read_csv(f'https://ballchasing.com/dl/stats/teams/{id}/{id}-team-stats.csv', sep=';')
    
#     df = df.set_index('color').T

#     return df

# def add_player_data(id: str, dataframe: DataFrame) -> None:

#     players_csv = get_players_csv(id)

#     dataframe['blue_player1'].at[dataframe['blue_player1'].size - dataframe['blue_player1'].isna().sum()] = Player(*players_csv[0])
#     dataframe['blue_player2'].at[dataframe['blue_player2'].size - dataframe['blue_player2'].isna().sum()] = Player(*players_csv[1])
#     dataframe['orange_player1'].at[dataframe['orange_player1'].size - dataframe['orange_player1'].isna().sum()] = Player(*players_csv[2])
#     dataframe['orange_player2'].at[dataframe['orange_player2'].size - dataframe['orange_player2'].isna().sum()] = Player(*players_csv[3])


# def add_team_data(id: str, dataframe: DataFrame) -> None:

#     teams_csv = get_teams_csv(id)

#     dataframe['blue_team'].at[dataframe['blue_team'].size - dataframe['blue_team'].isna().sum()] = Team(*teams_csv['blue'])
#     dataframe['orange_team'].at[dataframe['orange_team'].size - dataframe['orange_team'].isna().sum()] = Team(*teams_csv['orange'])
