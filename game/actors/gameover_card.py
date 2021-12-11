from game.actors.actor import Actor
from game.point import Point
from game import constants

class GameoverCard(Actor):

    def __init__(self):
        super().__init__()
        self.set_gravity(False)
        self.set_position(Point(100, 100))
        self.set_image(constants.GAMEOVER_1)
