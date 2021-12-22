from game.actors.actor import Actor
from game.point import Point
from game import constants

class Enemy(Actor):

    def __init__(self, x, y):
        super().__init__()
        self.set_width(constants.ENEMY_WIDTH)
        self.set_height(constants.ENEMY_HEIGHT)
        self.set_position(Point(x, y))
        self.set_color(constants.ENEMY_COLOR)
        self.set_gravity(True)
        self._hp = 3
        self._is_on_wall = False
        self._is_on_ground = False
        self._is_crouched = False
        self._type = "enemy"
        self._sound = constants.ENEMY_DEATH_SOUND
        self._volume = 1.0
        self._pitch = 1.0
        self._shot_sound = ""
        self._speed = 0

    def set_shot_sound(self, sound):
        self._shot_sound = sound

    def get_shot_sound(self):
        return self._shot_sound

    def has_shot_sound(self):
        return self._shot_sound != ""

    def set_volume(self, volume):
        self._volume = volume

    def get_volume(self):
        return self._volume

    def set_pitch(self, pitch):
        self._pitch = pitch

    def get_pitch(self):
        return self._pitch

    def set_sound(self, sound):
        self._sound = sound

    def get_sound(self):
        return self._sound

    def switch_animation(self):
        pass

    def set_is_crouched(self, status):
        self._is_crouched = status

    def get_is_crouched(self):
        return self._is_crouched
        
    def set_hp(self, amount):
        self._hp = amount

    def get_hp(self):
        return self._hp

    def set_speed(self, amount):
        self._speed = amount

    def get_speed(self):
        return self._speed

    def set_is_on_wall(self, status):
        self._is_on_wall = status
    
    def get_is_on_wall(self):
        return self._is_on_wall

    def set_is_on_ground(self, status):
        self._is_on_ground = status
    
    def get_is_on_ground(self):
        return self._is_on_ground

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)

    def move(self, player):
        raise NotImplementedError("execute not implemented in superclass")

    def shoot(self, cast):
        pass


            