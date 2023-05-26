import config as config
import data_requests as dr
from time import sleep
from pickle import dumps, load
from pandas import concat, read_parquet, DataFrame

# continually save to parquet file for deep storage, possible off-site backup

# can just add to file instead of reloading each time

# might be nice to have a way to call data from parquet instead of loading in data each time i need it 

new_data = DataFrame()



for col in ['blue_team','blue_player1','blue_player2','orange_team','orange_player1','orange_player2']:
    new_data[col] = new_data[col].map(dumps)

old_data = read_parquet('RL Data 1.parquet')

old_data = concat([old_data, new_data]).reset_index(drop=True)

old_data.to_parquet('RL Data 1.parquet')