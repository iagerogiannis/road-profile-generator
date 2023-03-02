from .hump import Hump


class HumpTrapezoid(Hump):
    def __init__(self, road_length, hump_position, height, length_big, length_small):
        super().__init__(road_length, hump_position, height)
        self.length_big = length_big
        self.length_small = length_small
        self.a = (self.length_big - self.length_small) / 2.

    def calculate_y(self, x):
        if (0 <= x <= self.hump_position) or (self.hump_position + self.length_big <= x <= self.road_length):
            return 0.
        if self.hump_position + self.a <= x <= self.hump_position + self.a + self.length_small:
            return self.height
        if self.hump_position < x < self.hump_position + self.a:
            return 2 * self.height * (x - self.hump_position) / (self.length_big - self.length_small)
        if self.hump_position + self.length_big - self.a < x < self.hump_position + self.length_big:
            return - 2 * self.height * (x - self.hump_position - self.length_big + self.a) / \
                (self.length_big - self.length_small) + self.height
        return None
