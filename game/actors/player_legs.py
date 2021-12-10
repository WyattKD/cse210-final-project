from game.actors.actor import Actor
from game import constants

class PlayerLegs(Actor):

    def __init__(self):
        super().__init__()
        self.set_width(constants.PLAYER_WIDTH)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_image(constants.WALK_ANIMATION2[0])
        self.set_color(constants.PLAYER_COLOR)
