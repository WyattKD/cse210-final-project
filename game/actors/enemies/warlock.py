from game.actors.enemies.enemy import Enemy
from game.actors.bullet import Bullet
from game.point import Point
from game import constants
from random import randint
from math import sqrt

class Warlock(Enemy):

    def __init__(self, x, y, extra_hp, extra_speed):
        super().__init__(x, y)
        self.set_hp(5 + extra_hp)
        self.set_gravity(False)
        self.set_width(constants.WARLOCK_WIDTH)
        self.set_height(constants.WARLOCK_HEIGHT)
        self.set_collision(False)
        self.set_animation(constants.WARLOCK_ANIMATION)
        self.set_image(constants.WARLOCK_ANIMATIONF_7)
        self.set_color(constants.WARLOCK_COLOR)
        self.switch_animation()
        self._speed = 0
        self._extra_speed = extra_speed
        self._has_shot = False
        self.set_sound(constants.WARLOCK_DEATH_SOUND)
        self.set_shot_sound(constants.WARLOCK_SHOT_SOUND)
        self.set_volume(3.0)


    def switch_animation(self):
        if self.get_image() == constants.WARLOCK_ANIMATION_17:
            self.set_animation(constants.WARLOCK_ANIMATIONF)
            self.set_frame_index(0)
        elif self.get_image() == constants.WARLOCK_ANIMATIONF_7:
            self.set_animation(constants.WARLOCK_ANIMATION)
            self.set_frame_index(0)

    def move(self, player):
        self.set_velocity(Point(0, 0))
        if self.get_image() == constants.WARLOCK_ANIMATIONF_7:
            distance = 0
            while distance <= 300:
                x = randint(40, 816)
                y = randint(40, 616)
                dx = player.get_position().get_x() - x
                dy = player.get_position().get_y() - y
                distance = sqrt(dx*dx + dy*dy)
            self.set_position(Point(x, y))
        if self.get_animation() == constants.WARLOCK_ANIMATIONF and self.get_frame_index() > 2:
            self.set_color(constants.HARMLESS_COLOR)
        elif self.get_frame_index() < 4 and self.get_animation() == constants.WARLOCK_ANIMATION:
            self.set_color(constants.HARMLESS_COLOR)
        else:
            self.set_color(constants.WARLOCK_COLOR)

    def shoot(self, cast, audio_service):
        if not cast["players"][0].get_is_dead():
            if self.get_image() == constants.WARLOCK_ANIMATION_11 and not self._has_shot:
                stats = [24, 24, 0, 5 + (2 * self._extra_speed), 0, 1, 0, 10000, 1, 0, constants.ENEMY_BULLET, constants.SHOOT_SOUND, 0.7]
                player = cast["players"][0]
                cast["bullets"].append(Bullet("player", self.get_position().get_x() + self.get_width()/2, self.get_position().get_y() + self.get_height()/2, stats, player.get_position().get_x(), player.get_position().get_y(), "enemy"))
                cast["bullets"][-1].set_collision(False)
                audio_service.play_sound(self.get_shot_sound())
                self._has_shot = True
            elif self.get_image() != constants.WARLOCK_ANIMATION_11:
                self._has_shot = False
            if self.get_image() == constants.WARLOCK_ANIMATIONF_2:
                audio_service.play_sound(constants.WARLOCK_TELEPORT_SOUND)
