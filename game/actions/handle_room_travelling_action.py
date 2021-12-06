from game import constants
from game.actions.action import Action
from game.point import Point
from game.actions.generate_room_action import GenerateRoomAction
from random import randint

class HandleRoomTravellingAction(Action):

    def __init__(self):
        super().__init__()
        self._generate_room_action = GenerateRoomAction()
        self._doors = ["wall", "door", "wall", "wall"]
        self._door_closed = True

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

    
    def _handle_doors(self, cast):
        walls = cast["walls"]
        doors_to_remove = []
        if cast["enemies"] == [] and self._door_closed:
            for wall in walls:
                if wall.get_type() == "door":
                    doors_to_remove.append(wall)
            for door in doors_to_remove:
                walls.remove(door)
                    