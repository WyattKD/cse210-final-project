from game import constants
from game.actions.action import Action
from game.point import Point
from game.actions.generate_room_action import GenerateRoomAction

class HandleRoomTravellingAction(Action):

    def __init__(self):
        super().__init__()
        self._generate_room_action = GenerateRoomAction()

    def execute(self, cast):
        self._traverse_room(cast)
        self._handle_doors(cast)

    def _traverse_room(self, cast):
        player = cast["players"][0]
        x = player.get_position().get_x()
        y = player.get_position().get_y()
        if x < 10 or x > 961 or y < 10 or y > 761:
            cast["walls"] = []
            cast["platforms"] = []
            cast["coins"] = []
            self._generate_room_action.execute(cast)
            if x < 10:
                x = 919
            elif x > 961:
                x = 41
            elif y < 10:
                y = 719
            elif y > 761:
                y = 41
            player.set_position(Point(x, y))
    
    def _handle_doors(self, cast):
        walls = cast["walls"]
        doors_to_remove = []
        if cast["enemies"] == []:
            for wall in walls:
                if wall.get_is_door():
                    doors_to_remove.append(wall)
            for door in doors_to_remove:
                walls.remove(door)
                    