from game import constants
from game.actions.action import Action
from game.point import Point
from random import choice
class HandlePickups(Action):

    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        self._handle_health_pickup(cast)
        self._handle_weapon_pickup(cast)

    def _handle_health_pickup(self, cast):
        player = cast["players"][0]
        pickups = cast["pickups"]
        pickups_to_remove = []
        for pickup in pickups:
            if pickup.get_type() == "health" and self._physics_service.is_collision(player, pickup) and player.get_hp() < 3:
                player.set_hp(player.get_hp() + 1)
                pickups_to_remove.append(pickup)
        for pickup in pickups_to_remove:
            pickups.remove(pickup)
            self._audio_service.play_sound(constants.HEALTH_SOUND)

                

    def _handle_weapon_pickup(self, cast):
        player = cast["players"][0]
        pickups = cast["pickups"]
        gun = cast["guns"][0]
        weapon_text = cast["UI"][4]
        pickups_to_remove = []
        for pickup in pickups:
            if pickup.get_type() == "weapon" and self._physics_service.is_collision(player, pickup):
                gun.set_gun_type(pickup.get_gun_type())
                pickups_to_remove.append(pickup)
        for pickup in pickups_to_remove:
            pickups.remove(pickup)
            self._audio_service.play_sound(constants.WEAPON_SOUND)
        weapon_text.set_text(f"{gun.get_gun_type().title()}")

