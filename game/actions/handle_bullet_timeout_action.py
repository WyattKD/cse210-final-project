from game import constants
from game.actions.action import Action
from game.point import Point
from time import time

class HandleBulletTimeoutAction(Action):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        self._handle_bullet_timeout(cast["bullets"])

    def _handle_bullet_timeout(self, bullets):
        bullets_to_remove = []
        
        for bullet in bullets:
            if round(time(), 2) - bullet.get_spawn_time() >= constants.BULLET_TIME:
                bullets_to_remove.append(bullet)
        for bullet in bullets_to_remove:
            bullets.remove(bullet)

