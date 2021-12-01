from game.actors.enemies.enemy import Enemy
from game.point import Point
from game import constants
from math import sqrt

class Mover(Enemy):

    def __init__(self, x, y, path, circular):
        super().__init__(x, y)
        self.set_hp(7)
        self.set_gravity(False)
        self.set_width(constants.MOVER_WIDTH)
        self.set_height(constants.MOVER_HEIGHT)
        self._circular = circular
        self._path = path
        self._current_point = self._path[0]
        self._iteration = 0
        self._going_down = False

    def move(self, player):
        self._current_point = self._path[self._iteration]
        dx = self._current_point.get_x() - self.get_position().get_x()
        dy = self._current_point.get_y() - self.get_position().get_y()

        distance = sqrt(dx*dx + dy*dy)
        dx /= distance
        dy /= distance

        dx *= constants.MOVER_SPEED
        dy *= constants.MOVER_SPEED

        self.set_velocity(Point(dx, dy))

        if -5 <= self.get_position().get_x() - self._current_point.get_x() <= 5 and -5 <= self.get_position().get_y() - self._current_point.get_y() <= 5:
            if self._circular:
                if self._iteration >= len(self._path) - 1:
                    self._iteration = 0
                else:
                    self._iteration += 1
            else:
                if self._going_down:
                    if self._iteration <= 0:
                        self._going_down = not self._going_down
                    else:
                        self._iteration -= 1
                else:
                    if self._iteration >= len(self._path) - 1:
                        self._going_down = not self._going_down
                    else:
                        self._iteration += 1