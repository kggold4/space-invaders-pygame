import copy
from typing import Tuple

from consts import WindowConsts, EnemyConsts
import numpy as np


class Character:
    def __init__(self, axis: np.array, pixel_size: int):
        self.axis = axis
        self.pixel_size = pixel_size

    def handle_out_of_board(self):
        if self.axis[0] <= 0:
            self.axis[0] = 0

        if self.axis[0] >= WindowConsts.WINDOW_SIZE[0] - self.pixel_size:
            self.axis[0] = WindowConsts.WINDOW_SIZE[0] - self.pixel_size

        if self.axis[1] <= 0:
            self.axis[1] = 0

        if self.axis[1] >= WindowConsts.WINDOW_SIZE[1] - self.pixel_size:
            self.axis[1] = WindowConsts.WINDOW_SIZE[1] - self.pixel_size

    def get_middle_axis(self) -> Tuple[int, int]:
        middle_axis = copy.copy(self.axis)
        middle_axis += np.array([EnemyConsts.ENEMY_PIXEL_SIZE / 2, EnemyConsts.ENEMY_PIXEL_SIZE / 2])
        return tuple(middle_axis)

    def add_axis(self, delta_axis: np.array):
        self.axis += delta_axis

    def get_axis(self) -> Tuple[int, int]:
        return tuple(self.axis)
