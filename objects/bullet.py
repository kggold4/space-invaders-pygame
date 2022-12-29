import copy
from typing import Tuple
import numpy as np

from kg_logger import KGLogger


class Bullet:
    def __init__(self, axis: np.array):
        self.logger = KGLogger()
        self.axis = copy.copy(axis)
        self.bullet_speed = 0.5
        self.delta_axis = np.array([0., -self.bullet_speed])
        self.done = False
        self.hit_enemy = False
        self.logger.warning(f"Create bullet, axis: {self.axis}")

    def add_axis(self, delta_axis: np.array):
        self.axis += delta_axis

    def get_axis(self) -> Tuple[int, int]:
        return tuple(self.axis)

    def move(self):
        self.add_axis(delta_axis=self.delta_axis)

    def is_done(self) -> bool:
        return self.done or self.axis[1] < 0

    def set_done(self):
        self.done = True
