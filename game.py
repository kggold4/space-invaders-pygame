import numpy as np
import pygame
from consts import WindowConsts, ScreenConsts, PlayerConsts, BackgroundsConsts, EnemyConsts
from kg_logger import KGLogger, log_function
from objects.bullet import Bullet
from objects.enemy import Enemy
from objects.explosion import Explosion
from objects.player import Player
from objects.star import Star
from utils.timer import Timer


class Game:
    def __init__(self):
        self.logger = KGLogger()
        pygame.init()
        self.screen = pygame.display.set_mode(size=WindowConsts.WINDOW_SIZE)
        self.delta_axis = PlayerConsts.PLAYER_INIT_DELTA_AXIS
        pygame.display.set_caption(WindowConsts.WINDOW_TITLE)
        icon = pygame.image.load(WindowConsts.WINDOW_ICON_PATH)
        pygame.display.set_icon(icon)
        self._load_images()
        self._load_objects()
        self.running = True
        self._player_score = 0
        self._timer = Timer()

    @log_function
    def _load_images(self):
        self._bullet_img = pygame.image.load(BackgroundsConsts.BULLET_IMAGE_PATH)
        self._star_img = pygame.image.load(BackgroundsConsts.STAR_IMAGE_PATH)
        self.small_explosion_img = pygame.image.load(BackgroundsConsts.SMALL_EXPLOSION_IMAGE_PATH)
        self.medium_explosion_img = pygame.image.load(BackgroundsConsts.MEDIUM_EXPLOSION_IMAGE_PATH)
        self.large_explosion_img = pygame.image.load(BackgroundsConsts.LARGE_EXPLOSION_IMAGE_PATH)
        self.player_img = pygame.image.load(PlayerConsts.PLAYER_IMAGE_PATH)

    @log_function
    def _load_objects(self):
        self._stars = []
        self._enemies = []
        self.add_enemy_each_seconds = 3
        self._player = Player()
        self._bullets = []
        self._explosions = []

    @log_function
    def _quit_running(self):
        self.running = False

    def show_score(self):
        font = pygame.font.Font(ScreenConsts.MAIN_FONT_FAMILY, ScreenConsts.MAIN_FONT_SIZE)
        score = font.render(f"Score: {str(self._player_score)}", True, ScreenConsts.WHITE)
        self.screen.blit(score, ScreenConsts.SCORE_AXIS)

    def _set_player(self):
        self.screen.blit(self.player_img, self._player.get_axis())
        self._player.set_speed(speed=PlayerConsts.PLAYER_SPEED + self._speed_depends_time())

    @log_function
    def _create_new_enemies(self):
        new_enemy = Enemy(speed=EnemyConsts.ENEMY_SPEED + self._speed_depends_time())
        self._enemies.append(new_enemy)
        self.logger.info(f"Created enemy")

    def _set_enemy(self):
        if self._timer.time_pass_in_seconds() > self.add_enemy_each_seconds:
            self.add_enemy_each_seconds += EnemyConsts.SET_ENEMY_EVERY_SECONDS + np.random.randint(0, 3)
            if len(self._enemies) < EnemyConsts.MAX_ENEMY_ON_SCREEN:
                self._create_new_enemies()
            self.logger.debug(f"Next enemy will appears at {self.add_enemy_each_seconds} sec")
        for enemy in self._enemies:
            if enemy.is_done():
                self._player_score += 3
                self._enemies.remove(enemy)
            enemy.random_move()
            enemy.handle_out_of_board()
            self.screen.blit(enemy.img, enemy.get_axis())

    def _create_new_star(self):
        if len(self._stars) < BackgroundsConsts.NUM_OF_STARS:
            new_star = Star()
            self._stars.append(new_star)

    def _set_starts(self):
        self._create_new_star()
        for star in self._stars:
            if star.is_done():
                self._stars.remove(star)
            star.move()
            self.screen.blit(self._star_img, star.get_axis())

    def _shoot_bullet(self):
        bullet_axis = self._player.get_middle_axis()
        bullet = Bullet(axis=bullet_axis)
        self._bullets.append(bullet)

    def _add_explosion(self, axis: np.array, explosion_type: str):
        explosion = Explosion(axis=axis, explosion_type=explosion_type)
        self._explosions.append(explosion)

    def _get_explosion_image(self, explosion_type):
        if explosion_type == BackgroundsConsts.S_EXPLOSION:
            return self.small_explosion_img
        elif explosion_type == BackgroundsConsts.M_EXPLOSION:
            return self.medium_explosion_img
        elif explosion_type == BackgroundsConsts.L_EXPLOSION:
            return self.large_explosion_img

    def _set_explosion(self):
        for explosion in self._explosions:
            if explosion.is_done():
                self._explosions.remove(explosion)
            explosion.move()
            self.screen.blit(self._get_explosion_image(explosion.explosion_type), explosion.get_axis())

    def _bullet_hit_enemy(self, bullet: Bullet):
        for enemy in self._enemies:
            if enemy.is_axis_in_enemy(other_axis=bullet.get_axis()):
                self.logger.error(f"hit enemy")
                bullet.set_done()
                enemy.hit()
                enemy_axis = enemy.get_middle_axis()
                explosion_type = BackgroundsConsts.S_EXPLOSION
                if enemy.damage == 2:
                    explosion_type = BackgroundsConsts.S_EXPLOSION
                elif enemy.damage == 1:
                    explosion_type = BackgroundsConsts.M_EXPLOSION
                elif enemy.damage == 0:
                    explosion_type = BackgroundsConsts.L_EXPLOSION
                self._add_explosion(axis=enemy_axis, explosion_type=explosion_type)
                self._player_score += 1

    def _set_bullets(self):
        for bullet in self._bullets:
            if bullet.is_done():
                self._bullets.remove(bullet)
            if not bullet.is_done():
                self._bullet_hit_enemy(bullet=bullet)
            bullet.move()
            self.screen.blit(self._bullet_img, bullet.get_axis())

    def _speed_depends_time(self) -> float:
        return self._timer.time_pass_in_seconds() / 500

    def _handle_key_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.delta_axis[0] = 0.
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.delta_axis[1] = 0.

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.delta_axis[0] -= self._player.speed
            if event.key == pygame.K_RIGHT:
                self.delta_axis[0] += self._player.speed
            if event.key == pygame.K_UP:
                self.delta_axis[1] -= self._player.speed
            if event.key == pygame.K_DOWN:
                self.delta_axis[1] += self._player.speed
            if event.key == pygame.K_SPACE:
                self._shoot_bullet()

    def run(self):
        while self.running:
            self.screen.fill(ScreenConsts.SCREEN_INIT_RGB)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit_running()
                self._handle_key_events(event)

            self._player.add_axis(self.delta_axis)
            self._player.handle_out_of_board()
            self._set_player()
            self._set_enemy()
            self._set_starts()
            self._set_bullets()
            self._set_explosion()
            self.show_score()
            self._timer.print_seconds()
            pygame.display.update()
        self.logger.info(f"Time played in total seconds: {self._timer.time_pass_in_seconds()}")
