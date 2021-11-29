from game.actor import Actor
from game.point import Point
from game import constants

class Enemy(Actor):

    def __init__(self, x, y):
        super().__init__()
        self.set_width(constants.ENEMY_WIDTH)
        self.set_height(constants.ENEMY_HEIGHT)
        self.set_position(Point(x, y))
        self.set_color(constants.ENEMY_COLOR)
        self.set_gravity(True)
        self._hp = 3
        self._is_on_wall = False
        
    def set_hp(self, amount):
        self._hp = amount

    def get_hp(self):
        return self._hp

    def set_is_on_wall(self, status):
        self._is_on_wall = status
    
    def get_is_on_wall(self):
        return self._is_on_wall

    def take_damage(self):
        self.set_hp(self.get_hp() - 1)

    def move(self, player):
        raise NotImplementedError("execute not implemented in superclass")