import numpy as np


class DriveConditions:
    def __init__(self, road_length, velocity, frequency):
        self.road_length = road_length
        self.velocity = velocity
        self.frequency = frequency
        self.total_time = road_length / velocity
        self.dt = 1 / self.frequency
        self.num_of_time_intervals = self.total_time / self.dt
        self.time_array = self.generate_time_series()
        self.x_array = self.generate_road_x_points()

    def generate_time_series(self):
        return np.array([i * self.dt for i in range(int(self.num_of_time_intervals) + 2)])

    def generate_road_x_points(self):
        return np.array([self.velocity * t_i for t_i in self.time_array])
