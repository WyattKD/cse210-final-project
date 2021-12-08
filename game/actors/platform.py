from game.actors.actor import Actor
from game.point import Point
from game import constants

class Platform(Actor):

    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.set_width(width)
        self.set_height(height)
        self.set_position(Point(x, y))
        self.set_color(constants.PLATFORM_COLOR)
        self.set_image(image)