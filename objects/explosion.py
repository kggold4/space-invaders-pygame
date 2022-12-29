import copy
from datetime import datetime
from typing import Tuple
import numpy as np
from consts import BackgroundsConsts


class Explosion:
    def __init__(self, axis: np.array, explosion_type: str):
        self.axis = copy.copy(axis)
        self.start_time = datetime.now()
        self.explosion_time = BackgroundsConsts.EXPLOSION_TIME + np.random.random()
        self.delta_axis = np.zeros(2)
        self.explosion_type = explosion_type

    def add_axis(self, delta_axis: np.array):
        self.axis += delta_axis

    def is_done(self):
        return (datetime.now() - self.start_time).total_seconds() > self.explosion_time

    def get_axis(self) -> Tuple[int, int]:
        return tuple(self.axis)

    def move(self):
        random_axis = np.random.choice([0, 1])
        random_direction = np.random.choice([0.1, -0.1])
        self.delta_axis[random_axis] = random_direction
        self.add_axis(delta_axis=self.delta_axis)
