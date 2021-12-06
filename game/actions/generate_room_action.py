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
        self._old_choice = -1
        

    def execute(self, cast, doors):
        rooms = [self._generate_room_2, self._generate_room_3]
        choice = randint(0, len(rooms) - 1)
        while choice == self._old_choice:
            choice = randint(0, len(rooms) - 1)
        rooms[choice](cast, doors)
        self._old_choice = choice

    def _generate_room_1(self, cast):

        self._default_walls(cast)

        self._block_bottom_door(cast)
        self._block_top_door(cast)
        self._block_left_door(cast)
        self._spawn_right_door(cast)

        self._full_platform(cast, self._two_jump_height)
        self._multi_medium(cast, "dual", self._one_jump_height)
        self._multi_long(cast, "center", self._four_jump_height - 60)    

    def _generate_room_2(self, cast, doors):
        
        self._default_walls(cast)

        left, right, up, down = doors[0], doors[1], doors[2], doors[3]
        self._generate_doors(cast, left, right, up, down)

        self._full_platform(cast, self._one_jump_height)
        self._full_platform(cast, self._two_jump_height)
        self._full_platform(cast, self._three_jump_height)
        self._full_platform(cast, self._four_jump_height)

        self._spawn_walkers(cast, 2, "bottom_right")
        self._spawn_flyers(cast, 3, "top_left")

        

        path = [Point(475,100), Point(275, 300), Point(475,500), Point(675, 300)]
        enemy5 = Mover(500,600, path, True)
        cast["enemies"].append(enemy5)

    def _generate_room_3(self, cast, doors):
        
        self._default_walls(cast)

        left, right, up, down = doors[0], doors[1], doors[2], doors[3]
        self._generate_doors(cast, left, right, up, down)

        if randint(1, 2) == 1:
            self._multi_long(cast, "center", self._one_jump_height)
            self._multi_long(cast, "center", self._four_jump_height)
        else:
            self._multi_short(cast, "dual_medium", self._one_jump_height)
            self._multi_short(cast, "dual_medium", self._four_jump_height)

        if randint(1, 2) == 1:
            self._multi_long(cast, "center", self._two_jump_height)
            self._multi_long(cast, "center", self._three_jump_height)
        else:
            self._multi_short(cast, "dual_medium", self._two_jump_height)
            self._multi_short(cast, "dual_medium", self._three_jump_height)

        if randint(1, 2) == 1:
            self._spawn_walkers(cast, 3, "center")
        else:
            self._spawn_flyers(cast, 4, "center")

        if randint(1, 2) == 1:
            path = [Point(50, 50), Point(50, 700), Point(900, 700), Point(900, 50)]
            enemy5 = Mover(500,600, path, True)
            cast["enemies"].append(enemy5)

        if randint(1, 2) == 1:
            path = [Point(900, 700), Point(900, 50), Point(50, 50), Point(50, 700)]
            enemy5 = Mover(500,200, path, True)
            cast["enemies"].append(enemy5)
            

        

    def _spawn_randomly(self, cast, area):
        distance = 0
        player = cast["players"][0]
        x = 0
        y = 0
        while distance <= 500:
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
            elif area == "center":
                x = randint(250, 750)
                y = randint(300, 600)
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
        cast["walls"].append(Wall(0, 0, 440, 40, "wall"))
        # Top right segmen
        cast["walls"].append(Wall(560, 0, 440, 40, "wall"))

        # Bottom left segment
        cast["walls"].append(Wall(0, 760, 440, 40, "wall"))
        # Bottom right segment
        cast["walls"].append(Wall(560, 760, 440, 40, "wall"))
    
        # Left top segment
        cast["walls"].append(Wall(0, 0, 40, 340, "wall"))
        # Left bottom segment
        cast["walls"].append(Wall(0, 460, 40, 340, "wall"))

        # Right top segment
        cast["walls"].append(Wall(960, 0, 40, 340, "wall"))
        # Right bottom segment
        cast["walls"].append(Wall(960, 460, 40, 340, "wall"))

    def _block_top_door(self, cast):
        cast["walls"].append(Wall(440, 0, 120, 40, "wall"))

    def _block_bottom_door(self, cast):
        cast["walls"].append(Wall(440, 760, 120, 40, "wall"))

    def _block_right_door(self, cast):
        cast["walls"].append(Wall(960, 340, 40, 120, "wall"))

    def _block_left_door(self, cast):
        cast["walls"].append(Wall(0, 340, 40, 120, "wall"))

    def _spawn_top_door(self, cast):
        cast["walls"].append(Wall(440, 0, 120, 40, "door"))

    def _spawn_bottom_door(self, cast):
        cast["walls"].append(Wall(440, 760, 120, 40, "door"))

    def _spawn_right_door(self, cast):
        cast["walls"].append(Wall(960, 340, 40, 120, "door"))

    def _spawn_left_door(self, cast):
        cast["walls"].append(Wall(0, 340, 40, 120, "door"))

    def _spawn_top_entrance(self, cast):
        cast["walls"].append(Wall(440, 0, 120, 40, "entrance"))

    def _spawn_bottom_entrance(self, cast):
        cast["walls"].append(Wall(440, 760, 120, 40, "entrance"))

    def _spawn_right_entrance(self, cast):
        cast["walls"].append(Wall(960, 340, 40, 120, "entrance"))

    def _spawn_left_entrance(self, cast):
        cast["walls"].append(Wall(0, 340, 40, 120, "entrance"))



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

    def _generate_doors(self, cast, left, right, up, down):
        if left == "door":
            self._spawn_left_door(cast)
        elif left == "open":
            pass
        else:
            self._block_left_door(cast)
        
        if right == "door":
            self._spawn_right_door(cast)
        elif right == "open":
            pass
        else:
            self._block_right_door(cast)

        if up == "door":
            self._spawn_top_door(cast)
        elif up == "open":
            pass
        else:
            self._block_top_door(cast)

        if down == "door":
            self._spawn_bottom_door(cast)
        elif down == "open":
            pass
        else:
            self._block_bottom_door(cast)