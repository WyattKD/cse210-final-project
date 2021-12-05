from game.actors.actor import Actor
from game.point import Point
from game import constants
from time import time
from random import randint
from math import sqrt

class Coin(Actor):

    def __init__(self, position):
        super().__init__()
        self.set_gravity(False)
        self.set_position(position)
        self.set_width(constants.COIN_WIDTH)
        self.set_height(constants.COIN_HEIGHT)
        self.set_color(constants.COIN_COLOR)
        self._spawn_time = round(time(), 2)
        self.random_velocity()

    def get_is_crouched(self):
        return False

    def random_velocity(self):
        dx = randint(0, 1000) - self.get_position().get_x()
        dy = randint(0, int(self.get_position().get_y())) - self.get_position().get_y()

        distance = sqrt(dx*dx + dy*dy)
        dx /= distance
        dy /= distance

        dx *= constants.COIN_SPEED
        dy *= constants.COIN_SPEED

        self.set_velocity(Point(dx, dy))

    def get_spawn_time(self):
        return self._spawn_time

