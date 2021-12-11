from game.actors.enemies.enemy import Enemy
from game.point import Point
from game import constants
from math import sqrt

class Flyer(Enemy):

    def __init__(self, x, y, extra_hp, extra_speed):
        super().__init__(x, y)
        self.set_hp(3 + extra_hp)
        self.set_gravity(False)
        self.set_width(constants.FLYER_WIDTH)
        self.set_height(constants.FLYER_HEIGHT)
        self.set_collision(False)
        self.set_animation(constants.FLYER_ANIMATION)
        self.set_image(constants.FLYER_ANIMATION_1)
        self.switch_animation()
        self._extra_speed = extra_speed

    def switch_animation(self):
        if self.get_velocity().get_x() > 0:
            self.set_animation(constants.FLYER_ANIMATIONF)
        else:
            self.set_animation(constants.FLYER_ANIMATION)


    def move(self, player):

        dx = player.get_position().get_x() - self.get_position().get_x()
        dy = player.get_position().get_y() - self.get_position().get_y()

        distance = sqrt(dx*dx + dy*dy)
        dx /= distance
        dy /= distance

        dx *= (constants.FLYER_SPEED + self._extra_speed)
        dy *= (constants.FLYER_SPEED + self._extra_speed)
        self.set_velocity(Point(dx, dy))