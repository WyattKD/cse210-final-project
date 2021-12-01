from game.actors.actor import Actor
from game.point import Point
from game import constants
import raylibpy

class Gun(Actor):

    def __init__(self):
        super().__init__()
        self.set_gun_type("machinegun")

    def get_gun_type(self):
        return self._gun_type

    def set_gun_type(self, gun):
        self._gun_type = gun
        if gun == "pistol":
            stats = [20, 20, raylibpy.YELLOW, 10, 0.3, 1, 1, 200, 1]
        elif gun == "sniper":
            stats = [25, 25, raylibpy.YELLOW, 30, 1, 1, 0, 1000, 3]
        elif gun == "shotgun":
            stats = [10, 10, raylibpy.YELLOW, 10, 0.5, 5, 1, 200, 0.5]
        elif gun == "machinegun":
            stats = [15, 15, raylibpy.YELLOW, 15, 0.1, 1, 3, 400, 0.3]
        self._bullet_width = stats[0]
        self._bullet_height = stats[1]
        self._bullet_color = stats[2]
        self._bullet_speed = stats[3]
        self._time_between_shots = stats[4]
        self._bullets = stats[5]
        self._bullet_spread = stats[6]
        self._bullet_life = stats[7]
        self._bullet_damage = stats[8]

    def get_gun_stats(self):
        stats = [self._bullet_width, self._bullet_height, self._bullet_color, self._bullet_speed, self._time_between_shots, self._bullets, self._bullet_spread, self._bullet_life, self._bullet_damage]
        return stats


    