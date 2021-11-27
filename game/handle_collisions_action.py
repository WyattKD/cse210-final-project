from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._player_on_ground = False

    def execute(self, cast):
        self._handle_player_ground(cast)
        self._handle_bullet_wall(cast)

    def _handle_player_ground(self, cast):
        player = cast["players"][0]
        walls = cast["walls"]
        self._player_on_ground = False
        for wall in walls:
            self._handle_player_wall(player, wall)
        player.set_is_on_ground(self._player_on_ground)   

    def _handle_player_wall(self, player, wall):
            x, y, px, py = self._update_player_position(player)
            wx = int(wall.get_position().get_x() + wall.get_width()/2)
            wy = int(wall.get_position().get_y() + wall.get_height()/2)

            if self._physics_service.is_collision(player, wall):
                if player.get_right_edge() in range(wall.get_left_edge(), wall.get_left_edge() + 10 + 1) and py in range(int(wall.get_top_edge() - constants.PLAYER_HEIGHT/2 + 1), int(wall.get_bottom_edge() + constants.PLAYER_HEIGHT/2)):
                    player.set_position(Point(wall.get_left_edge() - constants.PLAYER_WIDTH, y))
                elif player.get_left_edge() in range(wall.get_right_edge() - 10, wall.get_right_edge() + 1) and py in range(int(wall.get_top_edge() - constants.PLAYER_HEIGHT/2 + 1), int(wall.get_bottom_edge() + constants.PLAYER_HEIGHT/2)):
                    player.set_position(Point(wall.get_right_edge(), y))
                elif player.get_top_edge() in range(wall.get_bottom_edge() - 10, wall.get_bottom_edge() + 1) and px in range(int(wall.get_left_edge() - constants.PLAYER_WIDTH/2 + 1), int(wall.get_right_edge() + constants.PLAYER_WIDTH/2)):
                    player.set_position(Point(x, wall.get_bottom_edge()))
                elif player.get_bottom_edge() in range(wall.get_top_edge(), wall.get_top_edge() + 11) and px in range(int(wall.get_left_edge() - constants.PLAYER_WIDTH/2 + 1), int(wall.get_right_edge() + constants.PLAYER_WIDTH/2)):
                    player.set_position(Point(x, wall.get_top_edge() - constants.PLAYER_HEIGHT))
                    self._player_on_ground = True

    def _update_player_position(self, player):
        x = player.get_position().get_x()
        y = player.get_position().get_y()
        px = int(x + constants.PLAYER_WIDTH/2)
        py = int(y + constants.PLAYER_HEIGHT/2)
        return x, y, px ,py

    def _handle_bullet_wall(self, cast):
        bullets_to_remove = []
        for bullet in cast["bullets"]:
            for wall in cast["walls"]:
                if self._physics_service.is_collision(bullet, wall):
                    bullets_to_remove.append(bullet)
        for bullet in bullets_to_remove:
            if bullet in cast["bullets"]:
                cast["bullets"].remove(bullet)