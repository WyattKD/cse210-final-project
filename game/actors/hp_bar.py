from game.actors.actor import Actor
from game.point import Point
from game import constants



class HpBar(Actor):

    def __init__(self):
        super().__init__()
        self.set_image(constants.HP_BAR_3)
        self.set_position(Point(110, 0))