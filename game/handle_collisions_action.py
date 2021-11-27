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

    def is_on_wall(self, player, wall):
        player_left = player.get_left_edge()
        player_right = player.get_right_edge()
        wall_left = wall.get_left_edge()
        wall_right = wall.get_right_edge()
        if (player_left < wall_right and player_left > wall_left) or (player_right > wall_left and player_right < wall_right):
            return True
        else:
            return False

    def is_next_to_wall(self, player, wall):
        player_top = player.get_top_edge()
        player_bottom = player.get_bottom_edge()
        wall_top = wall.get_top_edge()
        wall_bottom = wall.get_bottom_edge()
        if (player_top < wall_bottom and player_top > wall_top) or (player_bottom > wall_bottom and player_bottom < wall_top):
            return True
        else:
            return False

    def _handle_player_wall(self, player, wall):

            x = player.get_position().get_x()

            y = player.get_position().get_y()

            if (player.get_right_edge() >= wall.get_left_edge() and player.get_right_edge() <= wall.get_right_edge()) and self.is_next_to_wall(player, wall):
                
                player.set_position(Point(wall.get_left_edge() - player.get_width(), y))

            if (player.get_left_edge() <= wall.get_right_edge() and player.get_left_edge() >= wall.get_left_edge()) and self.is_next_to_wall(player, wall):
                
                player.set_position(Point(wall.get_right_edge(), y))

            if (player.get_bottom_edge() >= wall.get_top_edge() and player.get_bottom_edge() <= wall.get_bottom_edge()) and self.is_on_wall(player, wall):
                
                player.set_position(Point(x, wall.get_top_edge() - player.get_height()))
                self._player_on_ground = True

            if (player.get_top_edge() <= wall.get_bottom_edge() and player.get_top_edge() >= wall.get_top_edge()) and self.is_on_wall(player, wall):

                player.set_position(Point(x, wall.get_bottom_edge()))

    def _handle_bullet_wall(self, cast):
        bullets_to_remove = []
        for bullet in cast["bullets"]:
            for wall in cast["walls"]:
                if self._physics_service.is_collision(bullet, wall):
                    bullets_to_remove.append(bullet)
        for bullet in bullets_to_remove:
            if bullet in cast["bullets"]:
                cast["bullets"].remove(bullet)