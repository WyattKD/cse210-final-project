from game import constants
from game.actions.action import Action
from game.point import Point
from game.actors.bullet import Bullet
from time import time
from random import randint

class ControlActorsAction(Action):

    def __init__(self, input_service):
        super().__init__()
        self._input_service = input_service
        self._jump_time = round(time(), 2)
        self._shoot_time = round(time(), 2)
        

    def execute(self, cast):
        self._player_move(cast)
        self._player_shoot(cast)

    def _player_move(self, cast):
        player = cast["players"][0] 
        dx = player.get_velocity().get_x()
        dy = player.get_velocity().get_y()
        if not player.get_is_dead():
            if "s" in self._input_service.get_inputs():
                player.set_is_crouched(True)
            else:
                player.set_is_crouched(False)
            if "a" in self._input_service.get_inputs():
                dx = -1 * constants.PLAYER_SPEED
            elif "d" in self._input_service.get_inputs():
                dx = 1 * constants.PLAYER_SPEED
            else:
                dx = 0
            self._player_jump(player)
            if player.get_is_jumping():
                player.set_gravity(False)
                if dy > 0:
                    dy = 0
                if dy <= -9:
                    dy = -9
                else:
                    dy -= constants.JUMP_SPEED
            elif player.get_is_on_ground():
                player.set_gravity(False)
                dy = 0
            else:
                player.set_gravity(True)
            player.set_velocity(Point(dx, dy))  
        else:
            player.set_velocity(Point(0, 0))

    def _player_jump(self, player):
        if "w" in self._input_service.get_inputs() and player.get_is_on_ground():
            player.set_is_jumping(True)
            self._jump_time = round(time(), 2)
        if "w" in self._input_service.get_inputs() and round(time(), 2) - self._jump_time  <= constants.JUMP_TIME:
            player.set_is_jumping(True)
        else:
            player.set_is_jumping(False)

    def _player_shoot(self, cast):
        gun = cast["guns"][0]
        stats = gun.get_gun_stats()
        time_between_shots = stats[4]
        num_bullets = stats[5]
        if round(time(), 2) - self._shoot_time >= time_between_shots:
            bullets = cast["bullets"]
            player = cast["players"][0]
            x = player.get_position().get_x()
            y = player.get_position().get_y()
            if "13" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("leftup", x, y, stats))
                self._shoot_time = round(time(), 2)
            elif "14" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("leftdown", x, y + constants.PLAYER_HEIGHT, stats))
                self._shoot_time = round(time(), 2)
            elif "23" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("rightup", x + constants.PLAYER_WIDTH, y, stats))
                self._shoot_time = round(time(), 2)
            elif "24" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("rightdown", x + constants.PLAYER_WIDTH, y + constants.PLAYER_HEIGHT, stats))
                self._shoot_time = round(time(), 2)
            elif "1" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("left", x, y + constants.PLAYER_HEIGHT/2, stats))
                self._shoot_time = round(time(), 2)
            elif "2" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("right", x + constants.PLAYER_WIDTH, y + constants.PLAYER_HEIGHT/2, stats))
                self._shoot_time = round(time(), 2)
            elif "3" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("up", x + constants.PLAYER_WIDTH/2, y, stats))
                self._shoot_time = round(time(), 2)
            elif "4" in self._input_service.get_inputs():
                for shots in range(num_bullets):
                    bullets.append(Bullet("down", x + constants.PLAYER_WIDTH/2, y + constants.PLAYER_HEIGHT, stats))
                self._shoot_time = round(time(), 2)