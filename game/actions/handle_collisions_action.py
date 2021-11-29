from game import constants
from game.actions.action import Action
from game.point import Point

class HandleCollisionsAction(Action):

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._player_on_ground = False
        self._enemy_on_wall = False


    def execute(self, cast):
        self._handle_player_ground(cast)
        self._handle_bullet_wall(cast)
        self._handle_enemy_wall(cast)
        self._handle_bullet_enemy(cast)
        self._handle_enemy_player(cast)

    def _handle_enemy_wall(self, cast):
        enemies = cast["enemies"]
        walls = cast["walls"]
        
        for enemy in enemies:
            self._enemy_on_wall = False
            for wall in walls:
                self._handle_entity_wall(enemy, wall)
                enemy.set_is_on_wall(self._enemy_on_wall) 

    def _handle_player_ground(self, cast):
        player = cast["players"][0]
        walls = cast["walls"]
        self._player_on_ground = False 
        for wall in walls:
           self._handle_entity_wall(player, wall)
        player.set_is_on_ground(self._player_on_ground)   


    def _handle_entity_wall(self, entity, wall):
            x, y, px, py = self._update_entity_position(entity)
            wx = int(wall.get_position().get_x() + wall.get_width()/2)
            wy = int(wall.get_position().get_y() + wall.get_height()/2)

            if self._physics_service.is_collision(entity, wall):
                if entity.get_right_edge() in range(wall.get_left_edge(), wall.get_left_edge() + 10 + 1) and py in range(int(wall.get_top_edge() - entity.get_height()/2 + 1), int(wall.get_bottom_edge() + entity.get_height()/2)):
                    entity.set_position(Point(wall.get_left_edge() - entity.get_width(), y))
                    self._enemy_on_wall = True
                elif entity.get_left_edge() in range(wall.get_right_edge() - 10, wall.get_right_edge() + 1) and py in range(int(wall.get_top_edge() - entity.get_height()/2 + 1), int(wall.get_bottom_edge() + entity.get_height()/2)):
                    entity.set_position(Point(wall.get_right_edge(), y))
                    self._enemy_on_wall = True
                elif entity.get_top_edge() in range(wall.get_bottom_edge() - 10, wall.get_bottom_edge() + 1) and px in range(int(wall.get_left_edge() - entity.get_width()/2 + 1), int(wall.get_right_edge() + entity.get_width()/2)):
                    entity.set_position(Point(x, wall.get_bottom_edge()))
                elif entity.get_bottom_edge() in range(wall.get_top_edge(), wall.get_top_edge() + 11) and px in range(int(wall.get_left_edge() - entity.get_width()/2 + 1), int(wall.get_right_edge() + entity.get_width()/2)):
                    entity.set_position(Point(x, wall.get_top_edge() - entity.get_height()))
                    self._player_on_ground = True


    def _update_entity_position(self, entity):
        x = entity.get_position().get_x()
        y = entity.get_position().get_y()
        px = int(x + entity.get_width()/2)
        py = int(y + entity.get_height()/2)
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

    def _handle_bullet_enemy(self, cast):
        bullets_to_remove = []
        for bullet in cast["bullets"]:
            for enemy in cast ["enemies"]:
                if self._physics_service.is_collision(bullet, enemy):
                    enemy.take_damage()
                    bullets_to_remove.append(bullet)
        for bullet in bullets_to_remove:
            if bullet in cast["bullets"]:
                cast["bullets"].remove(bullet)

    def _handle_enemy_player(self, cast):
        player = cast["players"][0]
        enemies = cast["enemies"]
        for enemy in enemies:
            if self._physics_service.is_collision(player, enemy):
                player.take_damage()