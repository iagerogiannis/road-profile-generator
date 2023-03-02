import os.path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class RoadProfile:
    def __init__(self):
        self.x = np.array([])
        self.y = np.array([])

    def calculate_y(self, x):
        return

    def generate_profile(self, x_array):
        self.x = x_array
        self.y = np.array([self.calculate_y(x_i) for x_i in x_array])
        return self.y

    def plot_profile(self, x_start=-np.inf, x_end=np.inf, apply_y_limits=True):
        i_start = np.nonzero(self.x > x_start)[0][0]
        i_end = np.nonzero(self.x < x_end)[0][-1]
        plt.plot(self.x[i_start:i_end], self.y[i_start:i_end])
        if apply_y_limits:
            plt.ylim(-0.1, 1.1)
        plt.show()

    def export_profile(self, file_name="road_profile", path="../results", time_array=None):
        df = pd.DataFrame({
            "X (m)": self.x,
            "Y (m)": self.y
        })

        if time_array is not None:
            df.insert(loc=0, column='Time (s)', value=time_array)

        if not os.path.exists(path):
            os.mkdir(path)
        df.to_csv('{}/{}.csv'.format(path, file_name), sep=",", index=False)
