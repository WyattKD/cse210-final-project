from game import constants
from game.action import Action
from game.point import Point
from time import time

class ControlActorsAction(Action):

    def __init__(self, input_service):
        super().__init__()
        self._input_service = input_service
        self._old_time = round(time(), 2)

    def execute(self, cast):
        self._move_player(cast)

    def _move_player(self, cast):
        player = cast["players"][0] 
        dx = player.get_velocity().get_x()
        dy = player.get_velocity().get_y()
        if "a" in self._input_service.get_inputs():
            dx = -1 * constants.PLAYER_SPEED
        elif "d" in self._input_service.get_inputs():
            dx = 1 * constants.PLAYER_SPEED
        else:
            dx = 0
        self._jump_player(player)
        if player.get_is_jumping():
            dy = -9
        elif player.get_is_on_ground():
            dy = 0
        else:
            dy = 9
        player.set_velocity(Point(dx, dy))  

    def _jump_player(self, player):
        if "w" in self._input_service.get_inputs() and player.get_is_on_ground():
            player.set_is_jumping(True)
            self._old_time = round(time(), 2)
        elif "w" in self._input_service.get_inputs() and round(time(), 2) - self._old_time  <= constants.JUMP_TIME:
            player.set_is_jumping(True)
        else:
            player.set_is_jumping(False)