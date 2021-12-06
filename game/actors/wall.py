from game.actors.actor import Actor
from game.point import Point
from game import constants

class Wall(Actor):

    def __init__(self, x, y, width, height, type):
        super().__init__()
        self.set_width(width)
        self.set_height(height)
        self.set_position(Point(x, y))
        self._type = type
        if type == "wall":
            self.set_color(constants.WALL_COLOR)
        else:
            self.set_color(constants.DOOR_COLOR)

    def get_type(self):
        return self._type
    