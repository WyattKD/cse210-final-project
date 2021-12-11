import os
os.environ['RAYLIB_BIN_PATH'] = '.'
import raylibpy
import random
from game import constants
from game.director import Director
from game.actors.actor import Actor
from game.point import Point
from game.actions.draw_actors_action import DrawActorsAction
from game.services.input_service import InputService
from game.services.output_service import OutputService
from game.services.physics_service import PhysicsService
from game.services.audio_service import AudioService

from game.actors.player import Player
from game.actors.player_legs import PlayerLegs
from game.actors.gun import Gun
from game.actors.wall import Wall
from game.actors.platform import Platform
from game.actors.enemies.enemy import Enemy
from game.actors.enemies.walker_enemy import Walker
from game.actors.enemies.flyer_enemy import Flyer
from game.actors.enemies.mover_enemy import Mover
from game.actors.background import Background
from game.actors.hp_bar import HpBar
from game.actors.text import Text
from game.actors.tutorial import Tutorial

from game.actions.control_actors_action import ControlActorsAction
from game.actions.handle_collisions_action import HandleCollisionsAction
from game.actions.move_actors_action import MoveActorsAction
from game.actions.handle_off_screen_action import HandleOffScreenAction
from game.actions.handle_entity_hp import HandleEntityHP
from game.actions.handle_enemy_movement import HandleEnemyMovement
from game.actions.handle_bullet_timeout_action import HandleBulletTimeoutAction
from game.actions.generate_room_action import GenerateRoomAction
from game.actions.prevent_enemy_overlap_action import PreventEnemyOverlapAction
from game.actions.handle_coins_action import HandleCoinsAction
from game.actions.handle_room_travelling_action import HandleRoomTravellingAction
from game.actions.handle_pickups import HandlePickups
from game.actions.handle_animations import HandleAnimations
from game.actions.update_ui import UpdateUI
from game.actions.handle_gameover import HandleGameover

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    background = Background()
    cast["background"] = [background]
    cast["tutorial"] = []
    player_legs = PlayerLegs()
    cast["player_parts"] = [player_legs]
    player = Player()
    cast["players"] = [player]
    
    gun = Gun()
    gun.set_gun_type(random.choice(["pistol", "rifle", "laser", "shotgun", "sniper", "burst rifle", "minigun", "machinegun", "dual pistol", "bubble"]))
    #gun.set_gun_type("minigun")
    cast["guns"] = [gun]
    cast["bullets"] = []
    cast["coins"] = []
    cast["walls"] = []
    cast["platforms"] = []
    cast["enemies"] = []
    cast["pickups"] = []
    cast["gameover_card"] = []
    hp_bar = HpBar()
    cast["UI"] = [hp_bar]
    hp_text = Text("HP", Point(0, 5), 60, raylibpy.RED)
    cast["UI"].append(hp_text)
    gold_text = Text("$", Point(800, 5), 60, raylibpy.GOLD)
    cast["UI"].append(gold_text)
    gold_count = Text("0", Point(840, 5), 60, raylibpy.GOLD)
    cast["UI"].append(gold_count)
    weapon_text = Text(f"{gun.get_gun_type().title()}", Point(5, 750), 40, raylibpy.WHITE)
    cast["UI"].append(weapon_text)
    rooms_cleared_text = Text("0", Point(0, 0), 40, raylibpy.BLANK)
    cast["UI"].append(rooms_cleared_text)
    enemies_defeated_text = Text("0", Point(0, 0), 40, raylibpy.BLANK)
    cast["UI"].append(enemies_defeated_text)
    total_score_text = Text("0", Point(0, 0), 60, raylibpy.BLANK)
    cast["UI"].append(total_score_text)

    generate_room_action = GenerateRoomAction()
    generate_room_action.generate_room_1(cast)
    
    
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)
    handle_off_screen_action = HandleOffScreenAction()
    handle_entity_hp = HandleEntityHP()
    handle_enemy_movement = HandleEnemyMovement()
    handle_bullet_timeout_action = HandleBulletTimeoutAction()
    prevent_enemy_overlap_action = PreventEnemyOverlapAction(physics_service)
    handle_coins_action = HandleCoinsAction()
    handle_room_travelling_action = HandleRoomTravellingAction()
    handle_pickups = HandlePickups(physics_service)
    handle_animations = HandleAnimations(input_service)
    update_ui = UpdateUI()
    handle_gameover = HandleGameover(input_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_off_screen_action, handle_entity_hp, handle_enemy_movement, handle_bullet_timeout_action, prevent_enemy_overlap_action, handle_coins_action, handle_room_travelling_action, handle_pickups]
    script["output"] = [update_ui, handle_gameover, handle_animations,  draw_actors_action]



    # Start the game
    output_service.open_window("Game")
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()