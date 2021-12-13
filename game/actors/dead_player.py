from game.actors.actor import Actor
from game import constants

class DeadPlayer(Actor):

    def __init__(self, position, animation):
        super().__init__()
        self.set_gravity(False)
        self.set_position(position)
        self.set_width(constants.PLAYER_HEIGHT)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_animation(animation)
        self.set_image(animation[0])