from typing import Tuple

from consts import WindowConsts
import numpy as np


class Star:
    def __init__(self):
        random_axis_x = np.random.randint(0, WindowConsts.WINDOW_SIZE[0])
        random_axis_y = np.random.choice([-0.1, 0, 0.1])
        self.axis = np.array([random_axis_x, random_axis_y])
        self.star_speed = 0.1 + np.random.randint(1, 4)
        self.delta_axis = np.array([0.1, self.star_speed])

    def add_axis(self, delta_axis: np.array):
        self.axis += delta_axis

    def get_axis(self) -> Tuple[int, int]:
        return tuple(self.axis)

    def move(self):
        self.add_axis(delta_axis=self.delta_axis)

    def is_done(self) -> bool:
        return self.axis[1] > WindowConsts.WINDOW_SIZE[1]
