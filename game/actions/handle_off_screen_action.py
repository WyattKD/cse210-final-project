from game import constants
from game.actions.action import Action
from game.point import Point

class HandleOffScreenAction(Action):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        self._handle_bullet_offscreen(cast)

    def _handle_bullet_offscreen(self, cast):
        for bullet in cast["bullets"]:
            x = bullet.get_position().get_x()
            y = bullet.get_position().get_y()
            if x <= 0 or  x >= 1000 - constants.BULLET_WIDTH or y <= 0 or y >= 800 - constants.BULLET_HEIGHT:
                cast["bullets"].remove(bullet)