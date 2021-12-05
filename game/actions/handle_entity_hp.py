from game import constants
from game.actions.action import Action
from game.point import Point
from random import randint
from game.actors.coin import Coin

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
        for enemy in enemies:
            if enemy.get_hp() <= 0:
                enemies_to_remove.append(enemy)

        for enemy in enemies_to_remove:
            amount = randint(5, 10)
            for _ in range(amount):
                coins.append(Coin(enemy.get_position()))
            enemies.remove(enemy)

    def _handle_player_hp(self, cast):
        player = cast["players"][0]
        player.determine_damage_status()
        

