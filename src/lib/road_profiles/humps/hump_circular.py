import math
from .hump import Hump


class HumpCircular(Hump):
    def __init__(self, road_length, hump_position, height, length):
        super().__init__(road_length, hump_position, height)
        self.length = length
        self.radius = self.calculate_radius()
        self.x0 = self.calculate_x0()

    def calculate_radius(self):
        return (4 * self.height ** 2 + self.length ** 2) / (8 * self.height)

    def calculate_x0(self):
        return self.radius * math.sqrt(1 - (1 - self.height / self.radius) ** 2)

    def calculate_y(self, x):
        if (0 <= x <= self.hump_position) or (self.hump_position + self.length <= x <= self.road_length):
            return 0.
        if self.hump_position < x < self.hump_position + self.length:
            return self.radius * math.sqrt(1 - ((x - self.x0 - self.hump_position) / self.radius) ** 2) - \
                (self.radius - self.height)
        return None
