from game import constants
from game.action import Action
from game.point import Point
from time import time
from game.bullet import Bullet
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
        if " " in self._input_service.get_inputs():
            player.set_is_jumping(False)
        elif "w" in self._input_service.get_inputs() and player.get_is_on_ground():
            player.set_is_jumping(True)
            self._jump_time = round(time(), 2)
        elif "w" in self._input_service.get_inputs() and round(time(), 2) - self._jump_time  <= constants.JUMP_TIME:
            player.set_is_jumping(True)
        else:
            player.set_is_jumping(False)

    def _player_shoot(self, cast):
        if round(time(), 2) - self._shoot_time >= constants.SHOOT_TIME:
            bullets = cast["bullets"]
            player = cast["players"][0]
            x = player.get_position().get_x()
            y = player.get_position().get_y()
            if "13" in self._input_service.get_inputs():
                bullets.append(Bullet("leftup", x, y))
                self._shoot_time = round(time(), 2)
            elif "14" in self._input_service.get_inputs():
                bullets.append(Bullet("leftdown", x, y + constants.PLAYER_HEIGHT))
                self._shoot_time = round(time(), 2)
            elif "23" in self._input_service.get_inputs():
                bullets.append(Bullet("rightup", x + constants.PLAYER_WIDTH, y))
                self._shoot_time = round(time(), 2)
            elif "24" in self._input_service.get_inputs():
                bullets.append(Bullet("rightdown", x + constants.PLAYER_WIDTH, y + constants.PLAYER_HEIGHT))
                self._shoot_time = round(time(), 2)
            elif "1" in self._input_service.get_inputs():
                bullets.append(Bullet("left", x, y + constants.PLAYER_HEIGHT/2))
                self._shoot_time = round(time(), 2)
            elif "2" in self._input_service.get_inputs():
                bullets.append(Bullet("right", x + constants.PLAYER_WIDTH, y + constants.PLAYER_HEIGHT/2))
                self._shoot_time = round(time(), 2)
            elif "3" in self._input_service.get_inputs():
                bullets.append(Bullet("up", x + constants.PLAYER_WIDTH/2, y))
                self._shoot_time = round(time(), 2)
            elif "4" in self._input_service.get_inputs():
                bullets.append(Bullet("down", x + constants.PLAYER_WIDTH/2, y + constants.PLAYER_HEIGHT))
                self._shoot_time = round(time(), 2)