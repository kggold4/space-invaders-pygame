import copy
import numpy as np
import pygame
from consts import EnemyConsts
from kg_logger import KGLogger
from objects.character import Character


class Enemy(Character):
    def __init__(self, speed: float):
        logger = KGLogger()
        self.axis = copy.copy(EnemyConsts.ENEMY_INIT_AXIS)
        self.axis[0] += np.random.randint(-300, 300)
        self.axis[1] += np.random.randint(-100, 100)
        self.pixel_size = EnemyConsts.ENEMY_PIXEL_SIZE
        random_img_path = np.random.choice(EnemyConsts.ENEMY_IMAGE_PATHS)
        self.img = pygame.image.load(random_img_path)
        logger.warning(random_img_path)
        # random moving
        self.direction = 0
        self.count_steps = 0
        self.delta_axis = np.zeros(2)
        self.number_of_steps = 200
        self.damage = 3
        self.speed = speed
        super().__init__(self.axis, self.pixel_size)

    def random_move(self):
        self.count_steps += 1
        if self.count_steps % self.number_of_steps == 0:
            random_axis = np.random.choice([0, 1])
            random_direction = np.random.choice([self.speed, -self.speed])
            self.delta_axis[random_axis] = random_direction
            self.count_steps = 0
            self.number_of_steps = np.random.randint(500, 1000)
        self.add_axis(delta_axis=self.delta_axis)

    def hit(self):
        self.damage -= 1

    def is_done(self) -> bool:
        return self.damage <= 0

    def is_axis_in_enemy(self, other_axis) -> bool:
        in_x_axis = self.axis[0] <= other_axis[0] <= (self.axis[0] + EnemyConsts.ENEMY_PIXEL_SIZE)
        in_y_axis = self.axis[1] <= other_axis[1] <= (self.axis[1] + EnemyConsts.ENEMY_PIXEL_SIZE)
        return in_x_axis and in_y_axis
