from game.actor import Actor
from game.point import Point
from game import constants

class Wall(Actor):

    def __init__(self, x, y):
        super().__init__()
        self.set_width(constants.WALL_WIDTH)
        self.set_height(constants.WALL_HEIGHT)
        self.set_position(Point(x, y))
        self.set_color(constants.WALL_COLOR)
    