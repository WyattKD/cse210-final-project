from game import constants
from game.actions.action import Action
from game.point import Point
from game.actors.wall import Wall
from game.actors.platform import Platform
from game.actors.enemies.enemy import Enemy
from game.actors.enemies.walker_enemy import Walker
from game.actors.enemies.flyer_enemy import Flyer
from game.actors.enemies.mover_enemy import Mover
from random import randint
from math import sqrt

class GenerateRoomAction(Action):

    def __init__(self):
        super().__init__()
        self._one_jump_height = 600
        self._two_jump_height = 460
        self._three_jump_height = 320
        self._four_jump_height = 180

    def execute(self, cast):
        self._generate_room_2(cast)

    def _generate_room_1(self, cast):

        self._default_walls(cast)

        self._block_bottom_door(cast)
        self._block_top_door(cast)
        self._block_left_door(cast)

        self._full_platform(cast, self._two_jump_height)
        self._multi_medium(cast, "dual", self._one_jump_height)
        self._multi_long(cast, "center", self._four_jump_height - 60)    

    def _generate_room_2(self, cast):
        self._default_walls(cast)

        self._full_platform(cast, self._one_jump_height)
        self._full_platform(cast, self._two_jump_height)
        self._full_platform(cast, self._three_jump_height)
        self._full_platform(cast, self._four_jump_height)

        self._spawn_walkers(cast, 4, "bottom_right")
        self._spawn_flyers(cast, 5, "top_left")

        

        path = [Point(475,100), Point(275, 300), Point(475,500), Point(675, 300)]
        enemy5 = Mover(475,99, path, True)
        cast["enemies"].append(enemy5)

    def _spawn_randomly(self, cast, area):
        distance = 0
        player = cast["players"][0]
        x = 0
        y = 0
        while distance <= 300:
            if area == "top_left":
                x = randint(40, 500)
                y = randint(40, 400)
            elif area == "top_right":
                x = randint(500, 960)
                y = randint(40, 400)
            elif area == "bottom_left":
                x = randint(40, 500)
                y = randint(400, 760)
            elif area == "bottom_right":
                x = randint(500, 960)
                y = randint(400, 760)
            dx = player.get_position().get_x() - x
            dy = player.get_position().get_y() - y
            distance = sqrt(dx*dx + dy*dy)
        return x, y

    def _spawn_walkers(self, cast, amount, area):
        for _ in range(amount):
            x, y = self._spawn_randomly(cast, area)
            cast["enemies"].append(Walker(x, y))

    def _spawn_flyers(self, cast, amount, area):
        for _ in range(amount):
            x, y = self._spawn_randomly(cast, area)
            cast["enemies"].append(Flyer(x, y))

    def _default_walls(self, cast):
        # Top left segment
        cast["walls"].append(Wall(0, 0, 440, 40))
        # Top right segmen
        cast["walls"].append(Wall(560, 0, 440, 40))

        # Bottom left segment
        cast["walls"].append(Wall(0, 760, 440, 40))
        # Bottom right segment
        cast["walls"].append(Wall(560, 760, 440, 40))
    
        # Left top segment
        cast["walls"].append(Wall(0, 0, 40, 340))
        # Left bottom segment
        cast["walls"].append(Wall(0, 460, 40, 340))

        # Right top segment
        cast["walls"].append(Wall(960, 0, 40, 340))
        # Right bottom segment
        cast["walls"].append(Wall(960, 460, 40, 340))

    def _block_top_door(self, cast):
        cast["walls"].append(Wall(440, 0, 120, 40))

    def _block_bottom_door(self, cast):
        cast["walls"].append(Wall(440, 760, 120, 40))

    def _block_right_door(self, cast):
        cast["walls"].append(Wall(960, 340, 40, 120))

    def _block_left_door(self, cast):
        cast["walls"].append(Wall(0, 340, 40, 120))

    def _full_platform(self, cast, y):
        cast["platforms"].append(Platform(40, y, 920, 20))

    def _long_platform(self, cast, x, y):
        cast["platforms"].append(Platform(x, y, 480, 20))

    def _medium_platform(self, cast, x, y):
        cast["platforms"].append(Platform(x, y, 240, 20))

    def _short_platform(self, cast, x, y):
        cast["platforms"].append(Platform(x, y, 120, 20))

    def _multi_short(self, cast, type, y):
        if type == "dual_far":
            self._short_platform(cast, 120, y)
            self._short_platform(cast, 760, y)
        elif type == "dual_medium":
            self._short_platform(cast, 240, y)
            self._short_platform(cast, 640, y)
        elif type == "dual_short":
            self._short_platform(cast, 360, y)
            self._short_platform(cast, 520, y)
        elif type == "triple_standard":
            self._short_platform(cast, 120, y)
            self._short_platform(cast, 440, y)
            self._short_platform(cast, 760, y)
        elif type == "triple_medium":
            self._short_platform(cast, 120, y)
            self._medium_platform(cast, 380, y)
            self._short_platform(cast, 760, y)
        elif type == "left_wall":
            self._short_platform(cast, 40, y)
        elif type == "right_wall":
            self._short_platform(cast, 840, y)
        elif type == "center":
            self._short_platform(cast, 440, y)
        elif type == "quintuple":
            self._short_platform(cast, 40, y)
            self._short_platform(cast, 240, y)
            self._short_platform(cast, 440, y)
            self._short_platform(cast, 640, y)
            self._short_platform(cast, 840, y)

    def _multi_medium(self, cast, type, y):
        if type == "dual":
            self._medium_platform(cast, 180, y)
            self._medium_platform(cast, 580, y)
        elif type == "left_wall":
            self._medium_platform(cast, 40, y)
        elif type == "right_wall":
            self._medium_platform(cast, 720, y)
        elif type == "center":
            self._medium_platform(cast, 380, y)
        elif type == "left":
            self._medium_platform(cast, 180, y)
        elif type == "right":
            self._medium_platform(cast, 580, y)

    def _multi_long(self, cast, type, y):
        if type == "left_wall":
            self._long_platform(cast, 40, y)
        elif type == "right_wall":
            self._long_platform(cast, 480, y)
        elif type == "center":
            self._long_platform(cast, 260, y)
