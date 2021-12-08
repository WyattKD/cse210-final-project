from game import constants
from game.actions.action import Action
from game.point import Point
from time import time
import raylibpy

class HandleAnimations(Action):

    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service
        self._player_iteration = 0
        self._player_frame_time = round(time(), 2)

    def execute(self, cast):
        self.handle_player_animation(cast)

    def handle_player_animation(self, cast):
        player = cast["players"][0]
        if round(time(), 2) - self._player_frame_time > 0.2 and "a" in self._input_service.get_inputs():
            player.set_image(constants.WALK_ANIMATION[self._player_iteration])
            self._player_frame_time = round(time(), 2)
            self._player_iteration += 1
            if self._player_iteration >= len(constants.WALK_ANIMATION):
                self._player_iteration = 0
        elif round(time(), 2) - self._player_frame_time > 0.2 and "d" in self._input_service.get_inputs():
            player.set_image(constants.WALK_ANIMATION2[self._player_iteration])
            self._player_frame_time = round(time(), 2)
            self._player_iteration += 1
            if self._player_iteration >= len(constants.WALK_ANIMATION):
                self._player_iteration = 0
        
        

