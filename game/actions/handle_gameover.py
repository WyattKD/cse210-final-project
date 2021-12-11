from game import constants
from game.actions.action import Action
from game.point import Point
from game.actors.text import Text
from game.actors.dead_player import DeadPlayer
from game.actors.gameover_card import GameoverCard
from game.actions.generate_room_action import GenerateRoomAction
from random import choice
from time import time
import raylibpy

class HandleGameover(Action):

    def __init__(self, input_service):
        super().__init__()
        self._input_service = input_service
        self._selection = ""
        self._generate_room = GenerateRoomAction()
        self._time = round(time(), 2)
        self._player_quit = False

    def execute(self, cast):
        self.spawn_death_animation(cast)
        self.display_stats(cast)
        self.handle_retry_or_quit(cast)

    def spawn_death_animation(self, cast):
        player = cast["players"][0]
        if player.get_is_dead():
            if player.get_direction() == "right" and len(cast["player_parts"]) <= 1:
                dead_player = DeadPlayer(Point(player.get_position().get_x() - 30, player.get_position().get_y()), constants.RIGHT_DEATH_ANIMATION)
                cast["player_parts"].append(dead_player)
            elif player.get_direction() == "left" and len(cast["player_parts"]) <= 1:
                dead_player = DeadPlayer(Point(player.get_position().get_x()- 30, player.get_position().get_y()), constants.LEFT_DEATH_ANIMATION)
                cast["player_parts"].append(dead_player)
            else:
                dead_player = cast["player_parts"][1]
                dead_player.set_position(Point(player.get_position().get_x()- 30, player.get_position().get_y()))

    def display_stats(self, cast):
        player = cast["players"][0]
        if len(cast["player_parts"]) > 1:
            if player.get_is_dead() and len(cast["gameover_card"]) <= 0 and round(time(), 2) - self._time > 3:
                gameover_card = GameoverCard()
                cast["gameover_card"].append(gameover_card)
                ui = cast["UI"]
                rooms_cleared_text = ui[5]
                enemies_defeated_text = ui[6]
                total_score_text = ui[7]
                gold_count = ui[3]
                rooms_cleared = int(rooms_cleared_text.get_text())
                enemies_defeated = int(enemies_defeated_text.get_text())
                gold_collected = int(gold_count.get_text())
                rooms_cleared_text.set_color(raylibpy.WHITE)
                enemies_defeated_text.set_color(raylibpy.WHITE)
                total_score_text.set_color(raylibpy.WHITE)
                rooms_cleared_text.set_position(Point(250, 300))
                enemies_defeated_text.set_position(Point(250, 350))
                total_score_text.set_position(Point(250, 470))
                total_score_text.set_text(f"Total score: {(rooms_cleared * 50) + (enemies_defeated * 5) + gold_collected}")
                rooms_cleared_text.set_text(f"Rooms cleared: {rooms_cleared_text.get_text()}")
                enemies_defeated_text.set_text(f"Enemies defeated: {enemies_defeated_text.get_text()}")
                gold_text = Text(f"Gold collected: {gold_count.get_text()}", Point(250, 400), 40, raylibpy.WHITE)
                ui.append(gold_text)
        else:
            self._time = round(time(), 2)

    def handle_retry_or_quit(self, cast):
        player = cast["players"][0]
        if player.get_is_dead() and len(cast["gameover_card"]) > 0:
            gameover_card = cast["gameover_card"][0]
            if "1" in self._input_service.get_inputs():
                gameover_card.set_image(constants.GAMEOVER_2)
                self._selection = "retry"
            elif "2" in self._input_service.get_inputs():
                gameover_card.set_image(constants.GAMEOVER_3)
                self._selection = "quit"
            if "e" in self._input_service.get_inputs() and self._selection == "retry":
                self.reset_game(cast)
            elif "e" in self._input_service.get_inputs() and self._selection == "quit":
                self._player_quit = True

    def reset_game(self, cast):
        cast["walls"] = []
        cast["platforms"] = []
        cast["coins"] = []
        cast["pickups"] = []
        cast["bullets"] = []
        cast["enemies"] = []
        cast["tutorial"] = []
        cast["gameover_card"] = []
        background = cast["background"][0]
        background.set_tint(raylibpy.WHITE)
        ui = cast["UI"]
        rooms_cleared_text = ui[5]
        enemies_defeated_text = ui[6]
        total_score_text = ui[7]
        gold_count = ui[3]
        ui.pop(8)
        cast["player_parts"].pop(1)
        rooms_cleared_text.set_color(raylibpy.BLANK)
        enemies_defeated_text.set_color(raylibpy.BLANK)
        total_score_text.set_color(raylibpy.BLANK)
        total_score_text.set_text("0")
        rooms_cleared_text.set_text("0")
        enemies_defeated_text.set_text("0")
        gold_count.set_text("0")
        player = cast["players"][0]
        self._generate_room.generate_room_1(cast)
        player.set_is_dead(False)
        player.set_color(constants.PLAYER_COLOR)
        player.set_position(Point(constants.MAX_X/2 - constants.PLAYER_WIDTH/2, constants.MAX_Y/2 - constants.PLAYER_HEIGHT/2))
        player.set_hp(3)
        gun = cast["guns"][0]
        gun.set_gun_type(choice(["pistol", "rifle", "laser", "shotgun", "sniper", "burst rifle", "minigun", "machinegun", "dual pistol", "bubble"]))

    def get_player_quit(self):
        return self._player_quit