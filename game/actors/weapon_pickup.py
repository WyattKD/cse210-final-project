from game.actors.actor import Actor
from game import constants
from random import choice

class WeaponPickup(Actor):

    def __init__(self, position):
        super().__init__()
        self._gun_type = choice(["pistol", "rifle", "laser", "shotgun", "sniper", "burst rifle", "minigun", "machinegun", "dual pistol", "bubble"])
        self.set_gravity(True)
        self.set_width(constants.WEAPON_PICKUP_WIDTH)
        self.set_height(constants.WEAPON_PICKUP_HEIGHT)
        self.set_color(constants.WEAPON_PICKUP_COLOR)
        self.set_position(position)
        self.set_gun_image()
        self._type = "weapon"

    def get_type(self):
        return self._type

    def get_is_crouched(self):
        return False

    def set_gun_image(self):
        if self._gun_type == "pistol":
            self.set_image(constants.PISTOL_PICKUP)
        elif self._gun_type == "sniper":
            self.set_image(constants.SNIPER_PICKUP)
        elif self._gun_type == "shotgun":
            self.set_image(constants.SHOTGUN_PICKUP)
        elif self._gun_type == "machinegun":
            self.set_image(constants.MACHINE_GUN_PICKUP)
        elif self._gun_type == "dual pistol":
            self.set_image(constants.DUAL_PISTOL_PICKUP)
        elif self._gun_type == "minigun":
            self.set_image(constants.MINIGUN_PICKUP)
        elif self._gun_type == "rifle":
            self.set_image(constants.RIFLE_PICKUP)
        elif self._gun_type == "burst rifle":
            self.set_image(constants.BURST_RIFLE_PICKUP)
        elif self._gun_type == "bubble":
            self.set_image(constants.BUBBLE_PICKUP)
        elif self._gun_type == "laser":
            self.set_image(constants.LASER_PICKUP)

    def get_gun_type(self):
        return self._gun_type