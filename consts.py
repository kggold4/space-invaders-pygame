import numpy as np


class WindowConsts:
    WINDOW_SIZE = (800, 600)
    WINDOW_TITLE = "Space Invaders"
    WINDOW_ICON_PATH = r"files/icons/ufo.png"


class ScreenConsts:
    WHITE = (255, 255, 255)
    SCREEN_INIT_RGB = np.zeros(3)
    MAIN_FONT_FAMILY = r"files/fonts/prosto_one.ttf"
    MAIN_FONT_SIZE = 20
    SCORE_AXIS = np.array([10., 10.])


class CharacterConsts:
    CHARACTER_INIT_AXIS = np.zeros(2)
    CHARACTER_PIXEL_SIZE = 64


class PlayerConsts:
    MAX_SPEED = 1
    PLAYER_IMAGE_PATH = r"files/icons/arcade-game.png"
    PLAYER_PIXEL_SIZE = 64
    PLAYER_INIT_AXIS = np.array([370., 480.])
    PLAYER_INIT_DELTA_AXIS = np.zeros(2)
    PLAYER_SPEED = 0.3


class EnemyConsts:
    START_NUM_OF_ENEMIES = 1
    ENEMY_IMAGE_PATHS: list = [r"files/icons/invader-1.png", r"files/icons/invader-2.png"]
    ENEMY_PIXEL_SIZE = 64
    ENEMY_INIT_AXIS = np.array([370., 100.])
    ENEMY_INIT_DELTA_AXIS = np.zeros(2)
    ENEMY_SPEED = 0.05
    SET_ENEMY_EVERY_SECONDS = 1
    MAX_ENEMY_ON_SCREEN = 10


class BackgroundsConsts:
    STAR_IMAGE_PATH = r"files/icons/star.png"
    BULLET_IMAGE_PATH = r"files/icons/bullet.png"
    NUM_OF_STARS = 30
    SMALL_EXPLOSION_IMAGE_PATH = r"files/icons/small_explosion.png"
    MEDIUM_EXPLOSION_IMAGE_PATH = r"files/icons/medium_explosion.png"
    LARGE_EXPLOSION_IMAGE_PATH = r"files/icons/large_explosion.png"
    EXPLOSION_TIME = 0.1
    L_EXPLOSION = "large_explosion"
    M_EXPLOSION = "middle_explosion"
    S_EXPLOSION = "small_explosion"
