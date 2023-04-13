from consts import PlayerConsts
from objects.character import Character


class Player(Character):
    def __init__(self):
        self.axis = PlayerConsts.PLAYER_INIT_AXIS
        self.pixel_size = PlayerConsts.PLAYER_PIXEL_SIZE
        self.speed = PlayerConsts.PLAYER_SPEED
        super().__init__(self.axis, self.pixel_size)

    def set_speed(self, speed: float):
        if self.speed > PlayerConsts.MAX_SPEED:
            self.speed = PlayerConsts.MAX_SPEED
        else:
            self.speed = speed
