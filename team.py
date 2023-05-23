from dataclasses import dataclass
from numpy import uint8, uint16, uint32, float16

# 0_boost_time == no_boost_time
# 100_boost_time == full_boost_time

@dataclass
class Team:
    team_name: object
    game_duration: uint16
    score: uint16
    goals: uint8
    assists: uint8
    saves: uint8
    shots: uint8
    shots_conceded: uint8
    goals_conceded: uint8
    shooting_percentage: float16
    bpm: uint16
    avg_boost_amount: float16
    amount_collected: uint16
    amount_collected_big_pads: uint16
    amount_collected_small_pads: uint16
    count_collected_big_pads: uint8
    count_collected_small_pads: uint8
    amount_stolen: uint16
    amount_stolen_big_pads: uint16
    amount_stolen_small_pads: uint16
    count_stolen_big_pads: uint8
    count_stolen_small_pads: uint8
    no_boost_time: float16
    full_boost_time: float16
    amount_used_while_supersonic: uint16
    amount_overfill_total: uint16
    amount_overfill_stolen: uint16
    total_distance: uint32
    time_slow_speed: float16
    time_boost_speed: float16
    time_supersonic_speed: float16
    time_on_ground: float16
    time_low_in_air: float16
    time_high_in_air: float16
    time_powerslide: float16
    count_powerslide: float16
    time_behind_ball: float16
    time_in_front_of_ball: float16
    time_defensive_half: float16
    time_offensive_half: float16
    time_defensive_third: float16
    time_neutral_third: float16
    time_offensive_third: float16
    time_ball_possession: float16
    time_ball_in_own_side: float16
    demos_inflicted: uint8
    demos_taken: uint8