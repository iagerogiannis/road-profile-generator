import numpy as np
from src.lib.road_profiles.road_profile import RoadProfile


class ISO8608(RoadProfile):
    n_min = 0.0078              # min spatial frequency
    n_max = 4.0                 # max spatial frequency
    n0 = 0.1                    # reference spatial frequency
    w = 2                       # set according to the value in page 14 of ISO

    def __init__(self, road_class, road_length):
        super().__init__()
        self.Gdn0 = self.get_Gdn0(road_class)
        self.L = road_length

    def generate_profile(self, x_array, center=False):
        self.x = x_array

        dx = x_array[1] - x_array[0]
        components = int(self.L / dx / 2)
        ns = np.linspace(self.n_min, self.n_max, components)

        Gd = np.sqrt(self.Gdn0 * (ns / self.n0) ** (- self.w) * 2 * (self.n_max - self.n_min) / components)

        phase = np.random.rand(components) * 2 * np.pi
        self.y = np.array([np.sum(Gd * np.cos(2 * np.pi * ns * x_array[i] - phase)) for i in range(len(x_array))])

        if center:
            self.y -= np.mean(self.y)

        return self.y

    def plot_profile(self, x_start=-np.inf, x_end=np.inf, **kwargs):
        super().plot_profile(x_start, x_end, apply_y_limits=False)

    @staticmethod
    def get_Gdn0(profile_class="A"):
        Gdn0_mapper = {"A": 32E-6,
                       "B": 128E-6,
                       "C": 512E-6,
                       "D": 2048E-6,
                       "E": 8192E-6,
                       "F": 32768E-6}

        try:
            return Gdn0_mapper[profile_class]
        except KeyError:
            raise ValueError("Profile name is not predefined.")
