from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):

    def __init__(self, input_service):
        super().__init__()
        self._input_service = input_service

    def execute(self, cast):
        pass