from game.actors.enemies.enemy import Enemy
from game.point import Point
from game import constants
from time import time

class Walker(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_hp(5)
        self._cooldown_time = round(time(), 2)
        self._jump_time = round(time(), 2)
        self._is_jumping = False

    def move(self, player):
        player_x = player.get_position().get_x() + player.get_width()/2
        walker_x = self.get_position().get_x() + self.get_width()/2
        player_y = player.get_position().get_y() + player.get_height()/2
        walker_y = self.get_position().get_y() + self.get_height()/2
        dx = self.get_velocity().get_x()
        dy = self.get_velocity().get_y()
        

        if player_x > walker_x:
            self.set_velocity(Point(constants.WALKER_SPEED, dy))
        elif player_x < walker_x:
            self.set_velocity(Point(-1 * constants.WALKER_SPEED, dy))
        else:
            self.set_velocity(Point(0, dy))

        if -7 <= player_x - walker_x <= 7 and walker_y - player_y > 80 and round(time(), 2) - self._cooldown_time  >= constants.WALKER_JUMP_TIME:
            self._cooldown_time = round(time(), 2)
            self._jump_time = round(time(), 2)
            self._is_jumping = True
        elif self.get_is_on_wall() and round(time(), 2) - self._cooldown_time  >= constants.WALKER_JUMP_TIME and not -7 <= player_x - walker_x <= 7:
            self._cooldown_time = round(time(), 2)
            self._jump_time = round(time(), 2)
            self._is_jumping = True
        elif round(time(), 2) - self._jump_time  >= constants.WALKER_COOLDOWN:
            self._is_jumping = False
            self.set_gravity(True)
        elif self._is_jumping:
            self.set_gravity(False)
            dy = -7
            self.set_velocity(Point(dx, dy))

        if -7 <= player_x - walker_x <= 7 and player_y - walker_y > 20:
            
            self.set_is_crouched(True)
        else:
            self.set_is_crouched(False)

        if self.has_gravity():
            dx = self.get_velocity().get_x()
            dy = 5
            self.set_velocity(Point(dx, dy))

            
            