from game.actor import Actor
from game.point import Point
from game import constants
class Player(Actor):

    def __init__(self):
        super().__init__()
        self.set_width(constants.PLAYER_WIDTH)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_position(Point(constants.MAX_X/2 - constants.PLAYER_WIDTH/2, constants.MAX_Y/2 - constants.PLAYER_HEIGHT/2))