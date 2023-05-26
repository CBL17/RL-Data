from dataclasses import dataclass
from pandas import Int8Dtype, UInt16Dtype, UInt32Dtype, Float32Dtype, StringDtype
import stat_classes as sc


@dataclass
class Player: 
    start_time: UInt16Dtype
    end_time: UInt16Dtype
    name: StringDtype
    car_id: UInt32Dtype
    car_name: StringDtype
    mvp: bool
    steering_sensitivity: UInt16Dtype
    platform: StringDtype
    platform_id: StringDtype
    demo_inflicted: Int8Dtype
    demo_taken: Int8Dtype
    rank_id: StringDtype
    rank_tier: Int8Dtype
    rank_division: Int8Dtype
    rank_name: StringDtype
    camera_settings: sc.CameraSettings
    core_stats: sc.CoreStats
    boost_stats: sc.BoostStats
    movement_stats: sc.MovementStats
    positioning_stats: sc.PositioningStats

# @dataclass
# class Player: 
#     start_time: object
#     end_time: object
#     name: object
#     car_id: object
#     car_name: object
#     mvp: object
#     steering_sensitivity: object
#     platform: object
#     platform_id: object
#     demo_inflicted: object
#     demo_taken: object
#     rank_id: object
#     rank_tier: object
#     rank_division: object
#     rank_name: object
#     camera_settings: sc.CameraSettings
#     core_stats: sc.CoreStats
#     boost_stats: sc.BoostStats
#     movement_stats: sc.MovementStats
#     positioning_stats: sc.PositioningStats