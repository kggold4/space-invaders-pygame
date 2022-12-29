import copy
from typing import Tuple

import numpy as np

from consts import PlayerConsts
from objects.character import Character


class Player(Character):
    def __init__(self):
        self.axis = PlayerConsts.PLAYER_INIT_AXIS
        self.pixel_size = PlayerConsts.PLAYER_PIXEL_SIZE
        self.speed = PlayerConsts.PLAYER_SPEED
        super().__init__(self.axis, self.pixel_size)

    def add_axis(self, delta_axis: np.array):
        self.axis += delta_axis

    def get_axis(self) -> Tuple[int, int]:
        return tuple(self.axis)

    def get_middle_axis(self) -> Tuple[int, int]:
        middle_axis = copy.copy(self.axis)
        middle_axis += np.array([PlayerConsts.PLAYER_PIXEL_SIZE / 2, PlayerConsts.PLAYER_PIXEL_SIZE / 2])
        return tuple(middle_axis)

    def set_speed(self, speed: float):
        if self.speed > PlayerConsts.MAX_SPEED:
            self.speed = PlayerConsts.MAX_SPEED
        else:
            self.speed = speed
