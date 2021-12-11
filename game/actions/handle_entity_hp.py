from game import constants
from game.actions.action import Action
from game.point import Point
from random import randint
from game.actors.coin import Coin
from game.actors.health_pickup import HealthPickup
from game.actors.weapon_pickup import WeaponPickup
class HandleEntityHP(Action):

    def __init__(self):
        super().__init__()

    def execute(self, cast):
        self._handle_enemy_hp(cast)
        self._handle_player_hp(cast)

    def _handle_enemy_hp(self, cast):
        enemies_to_remove = []
        enemies = cast["enemies"]
        coins = cast["coins"]
        enemies_defeated_text = cast["UI"][6]
        for enemy in enemies:
            if enemy.get_hp() <= 0:
                enemies_to_remove.append(enemy)

        for enemy in enemies_to_remove:
            amount = randint(3, 7)
            for _ in range(amount):
                coins.append(Coin(enemy.get_position()))
            random = randint(1,14)
            if random == 1:
                cast["pickups"].append(HealthPickup(enemy.get_position()))
            elif random == 2:
                cast["pickups"].append(WeaponPickup(enemy.get_position()))
            enemies.remove(enemy)
            enemies_defeated = int(enemies_defeated_text.get_text())
            enemies_defeated += 1
            enemies_defeated_text.set_text(str(enemies_defeated))

    def _handle_player_hp(self, cast):
        player = cast["players"][0]
        player.determine_damage_status()
        

