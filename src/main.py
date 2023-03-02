from src.lib.drive_conditions import DriveConditions
from src.lib.road_profiles import HumpTrapezoid, HumpCircular, ISO8608
from src.utils import *


# -- Export settings
path = r"../results"

# -- Drive & Sampling Conditions
road_length = 250.
velocity = kmph2mps(60)
sampling_frequency = 200.
drive_conditions = DriveConditions(road_length, velocity, sampling_frequency)

# -- Hump Geometry & Generation
hump_length = 3.5
hump_position = 50.
hump_height = 0.08

# -- Plot Options
x_start = 48.
x_end = 58.

# -- Hump Profiles Generation
humps = [
    {
        "label": "trapezoid",
        "hump": HumpTrapezoid(road_length, hump_position, hump_height, hump_length, 0.6 * hump_length)
    },
    {
        "label": "circular",
        "hump": HumpCircular(road_length, hump_position, hump_height, hump_length)
    },
]

for hump in humps:
    hump["hump"].generate_profile(drive_conditions.x_array)
    hump["hump"].plot_profile(x_start, x_end)
    hump["hump"].export_profile(time_array=drive_conditions.time_array,
                                file_name='{}-hump-road-profile'.format(hump["label"]), path=path)

# -- ISO Road Profile Generation
mid_quality_road_profile = ISO8608("D", road_length)

for item in ['left', 'right']:
    mid_quality_road_profile.generate_profile(drive_conditions.x_array, center=True)
    mid_quality_road_profile.plot_profile()
    mid_quality_road_profile.export_profile(time_array=drive_conditions.time_array,
                                            file_name='mid-quality-road-profile-{}'.format(item), path=path)

flat_road = HumpCircular(road_length, road_length + 1, hump_height, hump_length)

flat_road.generate_profile(drive_conditions.x_array)
flat_road.plot_profile(x_start, x_end)
flat_road.export_profile(time_array=drive_conditions.time_array,
                         file_name='flat-road-profile', path=path)
