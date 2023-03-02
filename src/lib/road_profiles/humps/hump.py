from ..road_profile import RoadProfile


class Hump(RoadProfile):
    def __init__(self, road_length, hump_position, height):
        super().__init__()
        self.road_length = road_length
        self.hump_position = hump_position
        self.height = height
