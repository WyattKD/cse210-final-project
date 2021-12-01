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

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bullets"] = []

    player = Player()
    cast["players"] = [player]

    gun = Gun()
    cast["guns"] = [gun]
    
    cast["walls"] = []
    wall = Wall(0, 720, 1000, 40)
    cast["walls"].append(wall)
    wall = Wall(500, 620, 40, 80)
    cast["walls"].append(wall)

    cast["platforms"] = []
    platform1 = Platform(240, 560, 120, 20)
    cast["platforms"].append(platform1)
    platform2 = Platform(660, 560, 120, 20)
    cast["platforms"].append(platform2)

    cast["enemies"] = []
    
    enemy1 = Walker(50,600)
    cast["enemies"].append(enemy1)
    enemy2 = Walker(100,600)
    cast["enemies"].append(enemy2)

    enemy3 = Flyer(50,50)
    cast["enemies"].append(enemy3)
    enemy4 = Flyer(950,50)
    cast["enemies"].append(enemy4)

    path = [Point(475,100), Point(275, 300), Point(475,500), Point(675, 300)]
    enemy5 = Mover(475,99, path, True)
    cast["enemies"].append(enemy5)
    
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


    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_off_screen_action, handle_entity_hp, handle_enemy_movement, handle_bullet_timeout_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Game")
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
