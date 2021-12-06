from game.actors.actor import Actor
from game.point import Point
from game import constants

class WeaponPickup(Actor):

    def __init__(self, position):
        super().__init__()
        self.set_gravity(False)
        self.set_width(constants.WEAPON_PICKUP_WIDTH)
        self.set_height(constants.WEAPON_PICKUP_HEIGHT)
        self.set_color(constants.WEAPON_PICKUP_COLOR)
        self.set_position(position)
        self._type = "weapon"

    def get_type(self):
        return self._type