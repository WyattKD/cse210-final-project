from game.actions.action import Action
from math import sqrt

class HandleBulletTimeoutAction(Action):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        self._handle_bullet_timeout(cast)

    def _handle_bullet_timeout(self, cast):
        gun = cast["guns"][0]
        bullets = cast["bullets"]
        stats = gun.get_gun_stats()
        bullet_life = stats[7]
        bullets_to_remove = []
        
        for bullet in bullets:
            spawnpoint = bullet.get_spawn_point()
            x = bullet.get_position().get_x() - spawnpoint.get_x()
            y = bullet.get_position().get_y() - spawnpoint.get_y()
            distance = sqrt(x*x + y*y)
            if  abs(distance) >= bullet_life:
                bullets_to_remove.append(bullet)
        for bullet in bullets_to_remove:
            bullets.remove(bullet)

