from game.actions.action import Action
from game.point import Point
from math import sqrt

class PreventEnemyOverlapAction(Action):
    
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        
    def execute(self, cast):
        self.push_enemies_apart(cast["enemies"])


    def push_enemies_apart(self, enemies):
        for enemy1 in enemies:
            for enemy2 in enemies:
                dx2 = enemy2.get_velocity().get_x()
                dy2 = enemy2.get_velocity().get_y()
                dx = enemy1.get_position().get_x() - enemy2.get_position().get_x()
                dy = enemy1.get_position().get_y() - enemy2.get_position().get_y()

                distance = sqrt(dx*dx + dy*dy)
                if distance != 0 and distance <= 30:
                    dx /= distance
                    dy /= distance
                    ndx = (dx2 - dx)/2
                    ndy = (dy2 - dy)/2
                    enemy2.set_velocity(Point(ndx, dy2))
