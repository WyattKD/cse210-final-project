from game.actors.actor import Actor
from game import constants
import raylibpy

class Gun(Actor):

    def __init__(self):
        super().__init__()
        self.set_gun_type("minigun")

    def get_gun_type(self):
        return self._gun_type

    def set_gun_type(self, gun):
        self._gun_type = gun
        if gun == "pistol":
            stats = [20, 20, raylibpy.YELLOW, 10, 0.4, 1, 1, 350, 1, 0, constants.PISTOL_BULLET, constants.SHOOT_SOUND, 0.7]
        elif gun == "sniper":
            stats = [30, 30, raylibpy.YELLOW, 40, 1.9, 1, 0, 1000, 9, 0, constants.SNIPER_BULLET, constants.SNIPER_SOUND, 3.0]
        elif gun == "shotgun":
            stats = [10, 10, raylibpy.YELLOW, 10, 0.8, 7, 3, 200, 1, 0.7, constants.SHOTGUN_BULLET, constants.SHOTGUN_SOUND, 3.0]
        elif gun == "machinegun":
            stats = [20, 20, raylibpy.YELLOW, 15, 0.1, 1, 3, 500, 0.6, 0, constants.PISTOL_BULLET, constants.SHOOT_SOUND, 0.7]
        elif gun == "dual pistol":
            stats = [20, 20, raylibpy.YELLOW, 10, 0.4, 2, 1, 350, 1, 3, constants.PISTOL_BULLET, constants.SHOOT_SOUND, 0.7]
        elif gun == "minigun":
            stats = [10, 10, raylibpy.YELLOW, 15, 0.01, 1, 3, 600, 0.2, 0, constants.SHOTGUN_BULLET, constants.MINIGUN_SOUND, 1.0]
        elif gun == "rifle":
            stats = [25, 25, raylibpy.YELLOW, 17, 0.3, 1, 0.5, 600, 2, 0, constants.RIFLE_BULLET, constants.RIFLE_SOUND, 0.5]
        elif gun == "burst rifle":
            stats = [15, 15, raylibpy.YELLOW, 17, 0.8, 3, 1, 600, 1.4, 2, constants.BURST_RIFLE_BULLET, constants.RIFLE_SOUND, 0.5]
        elif gun == "bubble":
            stats = [15, 15, raylibpy.BLUE, 5, 0.02, 1, 1, 800, 0.2, 0, constants.BUBBLE_BULLET, constants.BUBBLE_SOUND, 0.7]
        elif gun == "laser":
            stats = [15, 15, raylibpy.RED, 20, 0.001, 3, 0, 500, 0.03, 0.6, constants.LASER_BULLET, constants.LASER_SOUND, 0.7]

        # [width, height, color, bullet speed, shot speed, bullets, spread, range, damage, bullet delay, image, sound, volume]
        self._bullet_width = stats[0]
        self._bullet_height = stats[1]
        self._bullet_color = stats[2]
        self._bullet_speed = stats[3]
        self._time_between_shots = stats[4]
        self._bullets = stats[5]
        self._bullet_spread = stats[6]
        self._bullet_life = stats[7]
        self._bullet_damage = stats[8]
        self._time_between_bullets = stats[9]
        self._bullet_image = stats[10]
        self._bullet_sound = stats[11]
        self._bullet_volume = stats[12]

    def get_gun_stats(self):
        stats = [self._bullet_width, self._bullet_height, self._bullet_color, self._bullet_speed, self._time_between_shots, self._bullets, self._bullet_spread, self._bullet_life, self._bullet_damage, self._time_between_bullets, self._bullet_image, self._bullet_sound, self._bullet_volume]
        return stats


    