from game.actors.enemies.enemy import Enemy
from game.point import Point
from game import constants
from time import time

class Walker(Enemy):

    def __init__(self, x, y, extra_hp, extra_speed):
        super().__init__(x, y)
        self.set_width(constants.WALKER_WIDTH)
        self.set_height(constants.WALKER_HEIGHT)
        self.set_hp(5 + extra_hp)
        self._cooldown_time = round(time(), 2)
        self._jump_time = round(time(), 2)
        self._is_jumping = False
        self.set_animation(constants.WALKER_ANIMATION)
        self.set_image(constants.WALKER_ANIMATION_1)
        self.switch_animation()
        self._speed = constants.WALKER_SPEED
        self._extra_speed = extra_speed
        self.set_sound(constants.WALKER_DEATH_SOUND)
        self.set_volume(2.0)

    def switch_animation(self):
        
        if self.get_velocity().get_x() > 0:
            self.set_animation(constants.WALKER_ANIMATIONF)
        else:
            self.set_animation(constants.WALKER_ANIMATION)

    def move(self, player):
        player_x = player.get_position().get_x() + player.get_width()/2
        walker_x = self.get_position().get_x() + self.get_width()/2
        player_y = player.get_position().get_y() + player.get_height()/2
        walker_y = self.get_position().get_y() + self.get_height()/2
        dx = self.get_velocity().get_x()
        dy = self.get_velocity().get_y()
        

        if player_x > walker_x:
            self.set_velocity(Point((self._speed + self._extra_speed), dy))
        elif player_x < walker_x:
            self.set_velocity(Point(-1 * (self._speed + self._extra_speed), dy))
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
            if self.get_is_on_ground():
                dy = 0
                self.set_position(Point(self.get_position().get_x(), self.get_position().get_y() - 1))
            else:
                dy = 5
            self.set_velocity(Point(dx, dy))
            

            
            