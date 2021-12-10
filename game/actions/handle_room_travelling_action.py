import raylibpy
from game import constants
from game.actions.action import Action
from game.point import Point
from game.actions.generate_room_action import GenerateRoomAction
from random import randint, choice

class HandleRoomTravellingAction(Action):

    def __init__(self):
        super().__init__()
        self._generate_room_action = GenerateRoomAction()
        self._doors = ["wall", "door", "wall", "wall"]
        self._door_closed = True
        self._theme = raylibpy.WHITE

    def execute(self, cast):
        self._traverse_room(cast)
        self._handle_doors(cast)

    def _traverse_room(self, cast):
        
        player = cast["players"][0]
        x = player.get_position().get_x()
        y = player.get_position().get_y()
        
        if (x < 20 or x > 960 or y < 20 or y > 760) and self._door_closed:
            cast["walls"] = []
            cast["platforms"] = []
            cast["coins"] = []
            cast["pickups"] = []
            cast["bullets"] = []
            cast["enemies"] = []
            self._doors = ["wall", "wall", "wall", "wall"]
            if x < 20:
                x = 954
                self._doors[1] = "open"
            elif x > 960:
                x = 7
                self._doors[0] = "open"
            elif y < 20:
                y = 720
                self._doors[3] = "open"
            elif y > 760:
                y = 10
                self._doors[2] = "open"
            for i in range(randint(1,3)):
                door = randint(1, 3)
                while self._doors[door] == "open":
                    door = randint(1, 3)
                self._doors[door] = "door"
            self._generate_room_action.execute(cast, self._doors)
            self._randomize_colors(cast)
            self._door_closed = False
            player.set_position(Point(x, y))
        elif not self._door_closed:
            if x < 7:
                player.set_position(Point(6, y))
            elif x > 953:
                player.set_position(Point(954, y))
            elif y < 10:
                player.set_position(Point(x, 9))
            elif y > 750:
                player.set_position(Point(x, 951))
            
            if self._doors[0] == "open" and x > 40:
                self._generate_room_action._spawn_left_entrance(cast)
                self._door_closed = True
            elif self._doors[1] == "open" and x < 960:
                self._generate_room_action._spawn_right_entrance(cast)
                self._door_closed = True
            elif self._doors[2] == "open" and y > 40:
                self._generate_room_action._spawn_top_entrance(cast)
                self._door_closed = True
            elif self._doors[3] == "open" and y < 760:
                self._generate_room_action._spawn_bottom_entrance(cast)
                self._door_closed = True
            for wall in cast["walls"]:
                wall.set_tint(self._theme)

    
    def _handle_doors(self, cast):
        walls = cast["walls"]
        doors_to_remove = []
        if cast["enemies"] == [] and self._door_closed:
            for wall in walls:
                if wall.get_type() == "door":
                    doors_to_remove.append(wall)
            for door in doors_to_remove:
                walls.remove(door)

    def _randomize_colors(self, cast):
        walls = cast["walls"]
        platforms = cast["platforms"]
        background = cast["background"][0]
        self._theme = choice([raylibpy.LIGHTGRAY, raylibpy.GRAY, raylibpy.YELLOW, raylibpy.GOLD, raylibpy.ORANGE, raylibpy.PINK, raylibpy.RED, raylibpy.MAROON, raylibpy.GREEN, raylibpy.LIME, raylibpy.SKYBLUE, raylibpy.BLUE, raylibpy.PURPLE, raylibpy.VIOLET, raylibpy.BEIGE, raylibpy.BROWN, raylibpy.WHITE, raylibpy.MAGENTA])
        for wall in walls:
            wall.set_tint(self._theme)
        for platform in platforms:
            platform.set_tint(self._theme)
        background.set_tint(self._theme)
                    