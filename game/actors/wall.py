from game.actors.actor import Actor
from game.point import Point
from game import constants

class Wall(Actor):

    def __init__(self, x, y, width, height, door):
        super().__init__()
        self.set_width(width)
        self.set_height(height)
        self.set_position(Point(x, y))
        self._is_door = door
        if door:
            self.set_color(constants.DOOR_COLOR)
        else:
            self.set_color(constants.WALL_COLOR)

    def get_is_door(self):
        return self._is_door
    