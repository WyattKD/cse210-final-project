from game.actors.enemies.enemy import Enemy
from game.point import Point
from game import constants
from math import sqrt

class Flyer(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_hp(3)
        self.set_gravity(False)
        self.set_width(constants.FLYER_WIDTH)
        self.set_height(constants.FLYER_HEIGHT)

    def move(self, player):

        dx = player.get_position().get_x() - self.get_position().get_x()
        dy = player.get_position().get_y() - self.get_position().get_y()

        distance = sqrt(dx*dx + dy*dy)
        dx /= distance
        dy /= distance

        dx *= constants.FLYER_SPEED
        dy *= constants.FLYER_SPEED

        self.set_velocity(Point(dx, dy))