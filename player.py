from dataclasses import dataclass
from numpy import int8, uint8, uint16, uint32, float16
import stat_classes as sc

# @dataclass
# class Player: 
#     start_time: float16
#     end_time: float16
#     name: object
#     car_id: uint32
#     car_name: object
#     mvp: bool
#     steering_sensitivity: float16
#     platform: object
#     platform_id: object
#     demo_inflicted: uint8
#     demo_taken: uint8
#     rank_id: object
#     rank_tier: uint8
#     rank_division: uint8
#     rank_name: object
#     camera_settings: sc.CameraSettings
#     core_stats: sc.CoreStats
#     boost_stats: sc.BoostStats
#     movement_stats: sc.MovementStats
#     positioning_stats: sc.PositioningStats

@dataclass
class Player: 
    start_time: object
    end_time: object
    name: object
    car_id: object
    car_name: object
    mvp: object
    steering_sensitivity: object
    platform: object
    platform_id: object
    demo_inflicted: object
    demo_taken: object
    rank_id: object
    rank_tier: object
    rank_division: object
    rank_name: object
    camera_settings: sc.CameraSettings
    core_stats: sc.CoreStats
    boost_stats: sc.BoostStats
    movement_stats: sc.MovementStats
    positioning_stats: sc.PositioningStats