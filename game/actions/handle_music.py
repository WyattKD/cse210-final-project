from game import constants
from game.actions.action import Action
from time import time
class HandleMusic(Action):

    def __init__(self, audio_service):
        super().__init__()
        self._audio_service = audio_service
        self._music_time = 0
        self._music_stopped = False
        

    def execute(self, cast):
        if round(time(), 2) - self._music_time > 90 and not cast["players"][0].get_is_dead():
            self._audio_service.play_sound(constants.MUSIC, 0.5)
            self._music_time = round(time(), 2)
        elif cast["players"][0].get_is_dead():
            self._audio_service.stop_sound(constants.MUSIC)
            self._music_stopped = True
        elif self._music_stopped and not cast["players"][0].get_is_dead():
            self._music_stopped = False
            self._audio_service.play_sound(constants.MUSIC, 0.5)
            self._music_time = round(time(), 2)