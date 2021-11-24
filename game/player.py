from game.actor import Actor
from game.point import Point
from game import constants
class Player(Actor):

    def __init__(self):
        super().__init__()
        self.set_width(constants.PLAYER_WIDTH)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_position(Point(constants.MAX_X/2 - constants.PLAYER_WIDTH/2, constants.MAX_Y/2 - constants.PLAYER_HEIGHT/2))
        self.set_color(constants.PLAYER_COLOR)
        self.is_on_ground = False
        self.is_jumping = False

    def get_is_on_ground(self):
        return self.is_on_ground

    def set_is_on_ground(self, status):
        self.is_on_ground = status

    def get_is_jumping(self):
        return self.is_jumping

    def set_is_jumping(self, status):
        self.is_jumping = status