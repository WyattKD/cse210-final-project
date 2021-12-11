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
        self._bullet_time = round(time(), 2)
        self._inputs = ["", "", ""]
        

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
                if player.get_is_on_ceiling():
                    dy = 0
                elif dy > 0:
                    dy = 0
                elif dy <= -9:
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
            player.set_velocity(Point(0, 9))

    def _player_jump(self, player):
        if "w" in self._input_service.get_inputs() and player.get_is_on_ground():
            player.set_is_jumping(True)
            self._jump_time = round(time(), 2)
        if "w" in self._input_service.get_inputs() and round(time(), 2) - self._jump_time  <= constants.JUMP_TIME:
            player.set_is_jumping(True)
        else:
            player.set_is_jumping(False)

    def _player_shoot(self, cast):
        player = cast["players"][0]
        if not player.get_is_dead():
            gun = cast["guns"][0]
            stats = gun.get_gun_stats()
            time_between_shots = stats[4]
            num_bullets = stats[5]
            time_between_bullets = stats[9]
            self._inputs.append(self._input_service.get_inputs())
            self._inputs.pop(0)
            if any(char.isdigit() for char in self._inputs[0]) and any(char.isdigit() for char in self._inputs[1]) and any(char.isdigit() for char in self._inputs[2]):
                if round(time(), 2) - self._shoot_time >= time_between_shots:
                    bullets = cast["bullets"]
                    player = cast["players"][0]
                    x = player.get_position().get_x()
                    y = player.get_position().get_y()
                    if "13" in self._inputs[0] or "13" in self._inputs[1] or "13" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("leftup", x - 10, y + 20, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)
                    elif "14" in self._inputs[0] or  "14" in self._inputs[1] or "14" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("leftdown", x - 16, y - 20 + constants.PLAYER_HEIGHT, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)
                    elif "23" in self._inputs[0] or "23" in self._inputs[1] or "23" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("rightup", x + constants.PLAYER_WIDTH + 10, y + 20, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)
                    elif "24" in self._inputs[0] or "24" in self._inputs[1] or "24" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("rightdown", x + constants.PLAYER_WIDTH + 16, y + constants.PLAYER_HEIGHT - 20, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)
                    elif "1" in self._inputs[0] or "1" in self._inputs[1] or "1" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("left", x - 10, y + constants.PLAYER_HEIGHT/2 - 7, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)
                    elif "2" in self._inputs[0] or "2" in self._inputs[1] or "2" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("right", x + constants.PLAYER_WIDTH + 5, y + constants.PLAYER_HEIGHT/2 - 7, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)
                    elif "3" in self._inputs[0] or "3" in self._inputs[1] or "3" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("up", x + constants.PLAYER_WIDTH/2 - 3, y + 10, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)
                    elif "4" in self._inputs[0] or "4" in self._inputs[1] or "4" in self._inputs[2]:
                        for shots in range(num_bullets):
                            bullets.append(Bullet("down", x + constants.PLAYER_WIDTH/2, y - 13 + constants.PLAYER_HEIGHT, stats))
                            bullets[-1].bullet_step((num_bullets - (shots + 1)) * time_between_bullets)
                        self._shoot_time = round(time(), 2)