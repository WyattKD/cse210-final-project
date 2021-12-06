from game import constants
from game.actions.action import Action
from game.point import Point

class HandleOffScreenAction(Action):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        self._handle_bullet_offscreen(cast)
        self._handle_coin_offscreen(cast)
        self._handle_pickup_offscreen(cast)

    def _handle_bullet_offscreen(self, cast):
        bullets_to_remove = []
        for bullet in cast["bullets"]:
            x = bullet.get_position().get_x()
            y = bullet.get_position().get_y()
            if x <= 30 or  x >= 970 - bullet.get_width() or y <= 30 or y >= 770 - bullet.get_height():
                bullets_to_remove.append(bullet)
        for bullet in bullets_to_remove:
            cast["bullets"].remove(bullet)
            
    def _handle_coin_offscreen(self, cast):
        coins_to_remove = []
        for coin in cast["coins"]:
            x = coin.get_position().get_x()
            y = coin.get_position().get_y()
            if x <= 30 or  x >= 970 - coin.get_width() or y <= 30 or y >= 770 - coin.get_height():
                coins_to_remove.append(coin)
        for coin in coins_to_remove:
            cast["coins"].remove(coin)

    def _handle_pickup_offscreen(self, cast):
        pickups_to_remove = []
        for pickup in cast["pickups"]:
            x = pickup.get_position().get_x()
            y = pickup.get_position().get_y()
            if x <= 30 or  x >= 970 - pickup.get_width() or y <= 30 or y >= 770 - pickup.get_height():
                pickups_to_remove.append(pickup)
        for pickup in pickups_to_remove:
            cast["pickups"].remove(pickup)