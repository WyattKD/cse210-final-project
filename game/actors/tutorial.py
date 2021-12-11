from game.actors.actor import Actor
from game.point import Point
from game import constants

class Tutorial(Actor):

    def __init__(self):
        super().__init__()
        self.set_gravity(False)
        self.set_position(Point(constants.MAX_X/2 - constants.TUTORIAL_WIDTH/2, constants.MAX_Y/3 - constants.TUTORIAL_HEIGHT/3))
        self.set_width(constants.TUTORIAL_WIDTH)
        self.set_height(constants.TUTORIAL_HEIGHT)
        self.set_image(constants.TUTORIAL_ANIMATION_1)
        self.set_animation(constants.TUTORIAL_ANIMATION)