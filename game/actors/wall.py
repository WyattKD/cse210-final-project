from game.actors.actor import Actor
from game.point import Point
from game import constants
from math import sqrt


class Wall(Actor):

    def __init__(self, x, y, width, height, type, image):
        super().__init__()
        self.set_width(width)
        self.set_height(height)
        self.set_position(Point(x, y))
        self._type = type
        if type == "wall":
            self.set_color(constants.WALL_COLOR)
        else:
            self.set_color(constants.DOOR_COLOR)
        self.set_image(image)

    def get_type(self):
        return self._type

    def get_shortest_distance(self, entity):
        dx = (entity.get_position().get_x() + entity.get_width()/2) - self.get_left_edge()
        dy = (entity.get_position().get_y() + entity.get_height()/2) - (self.get_position().get_y() + self.get_height()/2)
        distance_from_left = sqrt(dx*dx + dy*dy)

        dx = (entity.get_position().get_x() + entity.get_width()/2) - self.get_right_edge()
        dy = (entity.get_position().get_y() + entity.get_height()/2) - (self.get_position().get_y() + self.get_height()/2)
        distance_from_right = sqrt(dx*dx + dy*dy)

        dx = (entity.get_position().get_x() + entity.get_width()/2) - (self.get_position().get_x() + self.get_width()/2)
        dy = (entity.get_position().get_y() + entity.get_height()/2) - self.get_top_edge()
        distance_from_top = sqrt(dx*dx + dy*dy)

        dx = (entity.get_position().get_x() + entity.get_width()/2) - (self.get_position().get_x() + self.get_width()/2)
        dy = (entity.get_position().get_y() + entity.get_height()/2) - self.get_bottom_edge()
        distance_from_bottom = sqrt(dx*dx + dy*dy)
        shortest_distance = min(distance_from_left, distance_from_right, distance_from_top, distance_from_bottom)
        return shortest_distance
    