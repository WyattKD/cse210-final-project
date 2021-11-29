from game.actors.actor import Actor
from game.point import Point
from game import constants
from time import *
class Player(Actor):

    def __init__(self):
        super().__init__()
        self.set_width(constants.PLAYER_WIDTH)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_position(Point(constants.MAX_X/2 - constants.PLAYER_WIDTH/2, constants.MAX_Y/2 - constants.PLAYER_HEIGHT/2))
        self.set_color(constants.PLAYER_COLOR)
        self._is_on_ground = True
        self.is_jumping = False
        self.set_gravity(True)
        self._hp = 3
        self._damage_time = 0
        self._is_dead = False

    def set_is_dead(self, status):
        self._is_dead = status

    def get_is_dead(self):
        return self._is_dead

    def set_hp(self, amount):
        self._hp = amount

    def get_hp(self):
        return self._hp

    def get_is_jumping(self):
        return self.is_jumping

    def set_is_jumping(self, status):
        self.is_jumping = status

    def get_is_on_ground(self):
        return self._is_on_ground

    def set_is_on_ground(self, status):
        self._is_on_ground = status

    def take_damage(self):
        if round(time(), 2) - self._damage_time  >= constants.INVINCIBLE_TIME:
            self._damage_time = round(time(), 2)
            self.set_hp(self.get_hp() - 1)

    def determine_damage_status(self):
        if self.get_hp() <= 0:
            self.set_color(constants.PLAYER_DEAD_COLOR)
            self.set_gravity(True)
            self.set_is_dead(True)
        elif round(time(), 2) - self._damage_time  >= constants.INVINCIBLE_TIME:
            self.set_color(constants.PLAYER_COLOR)
        else:
            self.set_color(constants.PLAYER_INV_COLOR)
            