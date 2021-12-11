from game import constants
from game.actions.action import Action
from game.point import Point
from time import time
import raylibpy

class HandleAnimations(Action):

    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service
        self._player_iteration = 0
        self._player_frame_time = round(time(), 2)
        self._inputs = []
        self._facing = "right"
        self._player_inv_frame_time = round(time(), 2)

    def execute(self, cast):
        self._handle_player_animation(cast)
        self._handle_coin_animation(cast)
        self._handle_enemy_animation(cast)
        self._handle_pickup_animation(cast)
        self._handle_death_animation(cast)
        self._handle_tutorial_animation(cast)

    def _handle_player_animation(self, cast):
        player = cast["players"][0]
        player_legs = cast["player_parts"][0]
        player_legs.set_position(player.get_position())
        if not player.get_is_dead():
            if round(time(), 2) - self._player_frame_time > 0.2 and "a" in self._input_service.get_inputs():
                player_legs.set_image(constants.WALK_ANIMATION[self._player_iteration])
                self._player_frame_time = round(time(), 2)
                self._player_iteration += 1
                if self._player_iteration >= len(constants.WALK_ANIMATION):
                    self._player_iteration = 0
                self._facing = "left"
                player.set_direction("left")
            elif round(time(), 2) - self._player_frame_time > 0.2 and "d" in self._input_service.get_inputs():
                player_legs.set_image(constants.WALK_ANIMATION2[self._player_iteration])
                self._player_frame_time = round(time(), 2)
                self._player_iteration += 1
                if self._player_iteration >= len(constants.WALK_ANIMATION):
                    self._player_iteration = 0
                self._facing = "right"
                player.set_direction("right")
            
            if "1" not in self._input_service.get_inputs() and "2" not in self._input_service.get_inputs() and "3" not in self._input_service.get_inputs() and "4" not in self._input_service.get_inputs():
                if self._facing == "left":
                    player.set_image(constants.PLAYER_IDLE_LEFT)
                elif self._facing == "right":
                    player.set_image(constants.PLAYER_IDLE_RIGHT)

            if "13" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_LEFTUP)
            elif "14" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_LEFTDOWN)
            elif "23" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_RIGHTUP)
            elif "24" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_RIGHTDOWN)
            elif "1" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_LEFT)
            elif "2" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_RIGHT)
            elif "3" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_UP)
            elif "4" in self._input_service.get_inputs():
                player.set_image(constants.PLAYER_DOWN)

            if player.get_color() == constants.PLAYER_INV_COLOR:
                if round(time(), 2) - self._player_inv_frame_time > 0.05:
                    self._player_inv_frame_time = round(time(), 2)
                    if player.get_tint() == raylibpy.GRAY:
                        player.set_tint(raylibpy.BLANK)
                        player_legs.set_tint(raylibpy.BLANK)
                    else:
                        player.set_tint(raylibpy.GRAY)
                        player_legs.set_tint(raylibpy.GRAY)
            else:
                player.set_tint(raylibpy.WHITE)
                player_legs.set_tint(raylibpy.WHITE)
        else:
            player.set_tint(raylibpy.BLANK)
            player_legs.set_tint(raylibpy.BLANK)

            

    def _handle_enemy_animation(self, cast):
        enemies = cast["enemies"]
        for enemy in enemies:
            if enemy.has_animation():
                enemy.switch_animation()
                if round(time(), 2) - enemy.get_frame_time() > 0.1:
                    animation = enemy.get_animation()
                    image = enemy.get_image()
                    index = enemy.get_frame_index()
                    index += 1
                    if index >= len(animation):
                        index = 0
                    enemy.set_image(animation[index]) 
                    enemy.set_frame_time()
                    enemy.set_frame_index(index)

    def _handle_death_animation(self, cast):
        if len(cast["player_parts"]) > 1:
            dead_player = cast["player_parts"][1]
            if round(time(), 2) - dead_player.get_frame_time() > 0.2:
                animation = dead_player.get_animation()
                index = dead_player.get_frame_index()
                index += 1
                if index >= len(animation):
                    index = 8
                dead_player.set_image(animation[index]) 
                dead_player.set_frame_time()
                dead_player.set_frame_index(index)

    def _handle_coin_animation(self, cast):
        coins = cast["coins"]
        for coin in coins:
            if round(time(), 2) - coin.get_frame_time() > 0.2:
                animation = coin.get_animation()
                image = coin.get_image()
                index = animation.index(image)
                index += 1
                if index >= len(animation):
                    index = 0
                coin.set_image(animation[index]) 
                coin.set_frame_time()

    def _handle_pickup_animation(self, cast):
        pickups = cast["pickups"]
        for pickup in pickups:
            if pickup.get_type() == "health":
                if round(time(), 2) - pickup.get_frame_time() > 0.2:
                    animation = pickup.get_animation()
                    image = pickup.get_image()
                    index = animation.index(image)
                    index += 1
                    if index >= len(animation):
                        index = 0
                    pickup.set_image(animation[index]) 
                    pickup.set_frame_time()

    def _handle_tutorial_animation(self, cast):
        if len(cast["tutorial"]) > 0:
            tutorial = cast["tutorial"][0]
            if round(time(), 2) - tutorial.get_frame_time() > 0.2:
                animation = tutorial.get_animation()
                image = tutorial.get_image()
                index = animation.index(image)
                index += 1
                if index >= len(animation):
                    index = 0
                tutorial.set_image(animation[index]) 
                tutorial.set_frame_time()
               
        
        

