from game.actors.actor import Actor
from game.point import Point
from game import constants

class HealthPickup(Actor):

    def __init__(self, position):
        super().__init__()
        self.set_gravity(False)
        self.set_width(constants.HEALTH_PICKUP_WIDTH)
        self.set_height(constants.HEALTH_PICKUP_HEIGHT)
        self.set_color(constants.HEALTH_PICKUP_COLOR)
        self.set_position(position)
        self._type = "health"

    def get_type(self):
        return self._type