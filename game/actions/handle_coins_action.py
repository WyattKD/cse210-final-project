from game import constants
from game.actions.action import Action
from game.point import Point
from time import time

class HandleCoinsAction(Action):

    def __init__(self):
        super().__init__()

    def execute(self, cast):
        self._coin_physics(cast["coins"])

    def _coin_physics(self, coins):
        for coin in coins:
            if round(time(), 2) - coin.get_spawn_time() > constants.COIN_AIR_TIME:
                coin.set_gravity(True)
                dy = coin.get_velocity().get_y()
                dx = coin.get_velocity().get_x()
                if -0.5 <= dx <= 0.5:
                    dx = 0
                elif dx > 0:
                    dx -= 0.2
                elif dx < 0:
                    dx += 0.2
               
                coin.set_velocity(Point(dx, dy))
