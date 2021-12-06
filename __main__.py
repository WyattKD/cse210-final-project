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
from game.actors.gun import Gun
from game.actors.wall import Wall
from game.actors.platform import Platform
from game.actors.enemies.enemy import Enemy
from game.actors.enemies.walker_enemy import Walker
from game.actors.enemies.flyer_enemy import Flyer
from game.actors.enemies.mover_enemy import Mover

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
def main():

    # create the cast {key: tag, value: list}
    cast = {}

    
    player = Player()
    cast["players"] = [player]
    gun = Gun()
    gun.set_gun_type(random.choice(["pistol", "rifle", "laser", "shotgun", "sniper", "burst_rifle", "minigun", "machinegun", "dual_pistol", "bubble"]))
    cast["guns"] = [gun]
    cast["bullets"] = []
    cast["coins"] = []
    cast["walls"] = []
    cast["platforms"] = []
    cast["enemies"] = []
    cast["pickups"] = []

    generate_room_action = GenerateRoomAction()
    generate_room_action.execute(cast)
    
    
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

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_off_screen_action, handle_entity_hp, handle_enemy_movement, handle_bullet_timeout_action, prevent_enemy_overlap_action, handle_coins_action, handle_room_travelling_action, handle_pickups]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Game")
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()