from game.actors.actor import Actor
from game.point import Point
from game import constants



class Background(Actor):

    def __init__(self):
        super().__init__()
        self.set_image(constants.BACKGROUND_IMAGE)
        self.set_position(Point(0, 0))