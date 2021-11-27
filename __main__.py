import os
os.environ['RAYLIB_BIN_PATH'] = '.'
import raylibpy
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

from game.player import Player
from game.wall import Wall

from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.handle_off_screen_action import HandleOffScreenAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bullets"] = []

    player = Player()
    cast["players"] = [player]
    
    cast["walls"] = []
    wall = Wall(0, 720, 1000, 40)
    cast["walls"].append(wall)

    wall = Wall(500, 620, 40, 80)
    cast["walls"].append(wall)
    

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


    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_off_screen_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Game")
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()