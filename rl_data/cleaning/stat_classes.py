from dataclasses import dataclass
from pandas import Int8Dtype, UInt8Dtype, UInt16Dtype, UInt32Dtype, Float32Dtype


# @dataclass
# class CameraSettings:
#     fov: UInt8Dtype
#     height: UInt8Dtype
#     pitch: Int8Dtype
#     distance: UInt16Dtype
#     stiffness: Float32Dtype
#     swivel_speed: Float32Dtype
#     transition_speed: Float32Dtype


# @dataclass
# class CoreStats:
#     shots: UInt8Dtype
#     shots_against: UInt8Dtype
#     goals: UInt8Dtype
#     goals_against: UInt8Dtype
#     saves: UInt8Dtype
#     assists: UInt8Dtype
#     score: UInt16Dtype
#     mvp: bool
#     shooting_percentage: Float32Dtype


# @dataclass
# class BoostStats:
#     bpm: Float32Dtype
#     bcpm: Float32Dtype
#     avg_amount: Float32Dtype
#     amount_collected: UInt16Dtype
#     amount_stolen: UInt16Dtype
#     amount_collected_big: UInt16Dtype
#     amount_stolen_big: UInt16Dtype
#     amount_collected_small: UInt16Dtype
#     amount_stolen_small: UInt16Dtype
#     count_collected_big: UInt8Dtype
#     count_stolen_big: UInt8Dtype
#     count_collected_small: UInt8Dtype
#     count_stolen_small: UInt8Dtype
#     amount_overfill: UInt16Dtype
#     amount_overfill_stolen: UInt16Dtype
#     amount_used_while_supersonic: UInt16Dtype
#     time_zero_boost: Float32Dtype
#     percent_zero_boost: Float32Dtype
#     time_full_boost: Float32Dtype
#     percent_full_boost: Float32Dtype
#     time_boost_0_25: Float32Dtype
#     time_boost_25_50: Float32Dtype
#     time_boost_50_75: Float32Dtype
#     time_boost_75_100: Float32Dtype
#     percent_boost_0_25: Float32Dtype
#     percent_boost_25_50: Float32Dtype
#     percent_boost_50_75: Float32Dtype
#     percent_boost_75_100: Float32Dtype


# @dataclass
# class MovementStats:
#     avg_speed: UInt16Dtype
#     total_distance: UInt32Dtype
#     time_supersonic_speed: Float32Dtype
#     time_boost_speed: Float32Dtype
#     time_slow_speed: Float32Dtype
#     time_ground: Float32Dtype
#     time_low_air: Float32Dtype
#     time_high_air: Float32Dtype
#     time_powerslide: Float32Dtype
#     count_powerslide: UInt8Dtype
#     avg_powerslide_duration: Float32Dtype
#     avg_speed_percentage: Float32Dtype
#     percent_slow_speed: Float32Dtype
#     percent_boost_speed: Float32Dtype
#     percent_supersonic_speed: Float32Dtype
#     percent_ground: Float32Dtype
#     percent_low_air: Float32Dtype
#     percent_high_air: Float32Dtype


# @dataclass
# class PositioningStats:
#     avg_distance_to_ball: UInt16Dtype
#     avg_distance_to_ball_possession: UInt16Dtype
#     avg_distance_to_ball_no_possession: UInt16Dtype
#     avg_distance_to_mates: UInt16Dtype
#     time_defensive_third: Float32Dtype
#     time_neutral_third: Float32Dtype
#     time_offensive_third: Float32Dtype
#     time_defensive_half: Float32Dtype
#     time_offensive_half: Float32Dtype
#     time_behind_ball: Float32Dtype
#     time_infront_ball: Float32Dtype
#     time_most_back: Float32Dtype
#     time_most_forward: Float32Dtype
#     goals_against_while_last_defender: UInt8Dtype
#     time_closest_to_ball: Float32Dtype
#     time_farthest_from_ball: Float32Dtype
#     percent_defensive_third: Float32Dtype
#     percent_offensive_third: Float32Dtype
#     percent_neutral_third: Float32Dtype
#     percent_defensive_half: Float32Dtype
#     percent_offensive_half: Float32Dtype
#     percent_behind_ball: Float32Dtype
#     percent_infront_ball: Float32Dtype
#     percent_most_back: Float32Dtype
#     percent_most_forward: Float32Dtype
#     percent_closest_to_ball: Float32Dtype
#     percent_farthest_from_ball: Float32Dtype 

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