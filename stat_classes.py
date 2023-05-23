from dataclasses import dataclass
from numpy import int8, uint8, uint16, uint32, float16


# @dataclass
# class CameraSettings:
#     fov: uint8
#     height: uint8
#     pitch: int8
#     distance: uint16
#     stiffness: float16
#     swivel_speed: float16
#     transition_speed: float16


# @dataclass
# class CoreStats:
#     shots: uint8
#     shots_against: uint8
#     goals: uint8
#     goals_against: uint8
#     saves: uint8
#     assists: uint8
#     score: uint16
#     mvp: bool
#     shooting_percentage: float16


# @dataclass
# class BoostStats:
#     bpm: float16
#     bcpm: float16
#     avg_amount: float16
#     amount_collected: uint16
#     amount_stolen: uint16
#     amount_collected_big: uint16
#     amount_stolen_big: uint16
#     amount_collected_small: uint16
#     amount_stolen_small: uint16
#     count_collected_big: uint8
#     count_stolen_big: uint8
#     count_collected_small: uint8
#     count_stolen_small: uint8
#     amount_overfill: uint16
#     amount_overfill_stolen: uint16
#     amount_used_while_supersonic: uint16
#     time_zero_boost: float16
#     percent_zero_boost: float16
#     time_full_boost: float16
#     percent_full_boost: float16
#     time_boost_0_25: float16
#     time_boost_25_50: float16
#     time_boost_50_75: float16
#     time_boost_75_100: float16
#     percent_boost_0_25: float16
#     percent_boost_25_50: float16
#     percent_boost_50_75: float16
#     percent_boost_75_100: float16


# @dataclass
# class MovementStats:
#     avg_speed: uint16
#     total_distance: uint32
#     time_supersonic_speed: float16
#     time_boost_speed: float16
#     time_slow_speed: float16
#     time_ground: float16
#     time_low_air: float16
#     time_high_air: float16
#     time_powerslide: float16
#     count_powerslide: uint8
#     avg_powerslide_duration: float16
#     avg_speed_percentage: float16
#     percent_slow_speed: float16
#     percent_boost_speed: float16
#     percent_supersonic_speed: float16
#     percent_ground: float16
#     percent_low_air: float16
#     percent_high_air: float16


# @dataclass
# class PositioningStats:
#     avg_distance_to_ball: uint16
#     avg_distance_to_ball_possession: uint16
#     avg_distance_to_ball_no_possession: uint16
#     avg_distance_to_mates: uint16
#     time_defensive_third: float16
#     time_neutral_third: float16
#     time_offensive_third: float16
#     time_defensive_half: float16
#     time_offensive_half: float16
#     time_behind_ball: float16
#     time_infront_ball: float16
#     time_most_back: float16
#     time_most_forward: float16
#     goals_against_while_last_defender: uint8
#     time_closest_to_ball: float16
#     time_farthest_from_ball: float16
#     percent_defensive_third: float16
#     percent_offensive_third: float16
#     percent_neutral_third: float16
#     percent_defensive_half: float16
#     percent_offensive_half: float16
#     percent_behind_ball: float16
#     percent_infront_ball: float16
#     percent_most_back: float16
#     percent_most_forward: float16
#     percent_closest_to_ball: float16
#     percent_farthest_from_ball: float16 

@dataclass
class CameraSettings:
    fov: object
    height: object
    pitch: object
    distance: object
    stiffness: object
    swivel_speed: object
    transition_speed: object


@dataclass
class CoreStats:
    shots: object
    shots_against: object
    goals: object
    goals_against: object
    saves: object
    assists: object
    score: object
    mvp: object
    shooting_percentage: object


@dataclass
class BoostStats:
    bpm: object
    bcpm: object
    avg_amount: object
    amount_collected: object
    amount_stolen: object
    amount_collected_big: object
    amount_stolen_big: object
    amount_collected_small: object
    amount_stolen_small: object
    count_collected_big: object
    count_stolen_big: object
    count_collected_small: object
    count_stolen_small: object
    amount_overfill: object
    amount_overfill_stolen: object
    amount_used_while_supersonic: object
    time_zero_boost: object
    percent_zero_boost: object
    time_full_boost: object
    percent_full_boost: object
    time_boost_0_25: object
    time_boost_25_50: object
    time_boost_50_75: object
    time_boost_75_100: object
    percent_boost_0_25: object
    percent_boost_25_50: object
    percent_boost_50_75: object
    percent_boost_75_100: object


@dataclass
class MovementStats:
    avg_speed: object
    total_distance: object
    time_supersonic_speed: object
    time_boost_speed: object
    time_slow_speed: object
    time_ground: object
    time_low_air: object
    time_high_air: object
    time_powerslide: object
    count_powerslide: object
    avg_powerslide_duration: object
    avg_speed_percentage: object
    percent_slow_speed: object
    percent_boost_speed: object
    percent_supersonic_speed: object
    percent_ground: object
    percent_low_air: object
    percent_high_air: object


@dataclass
class PositioningStats:
    avg_distance_to_ball: object
    avg_distance_to_ball_possession: object
    avg_distance_to_ball_no_possession: object
    avg_distance_to_mates: object
    time_defensive_third: object
    time_neutral_third: object
    time_offensive_third: object
    time_defensive_half: object
    time_offensive_half: object
    time_behind_ball: object
    time_infront_ball: object
    time_most_back: object
    time_most_forward: object
    goals_against_while_last_defender: object
    time_closest_to_ball: object
    time_farthest_from_ball: object
    percent_defensive_third: object
    percent_offensive_third: object
    percent_neutral_third: object
    percent_defensive_half: object
    percent_offensive_half: object
    percent_behind_ball: object
    percent_infront_ball: object
    percent_most_back: object
    percent_most_forward: object
    percent_closest_to_ball: object
    percent_farthest_from_ball: object 