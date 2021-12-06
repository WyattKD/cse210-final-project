from game import constants
from game.actions.action import Action
from game.point import Point


class HandleCollisionsAction(Action):

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._player_on_ground = False
        self._enemy_on_wall = False
        self._player_on_ceiling = False


    def execute(self, cast):
        self._handle_bullet_wall(cast)
        self._handle_enemy_wall(cast)
        self._handle_bullet_enemy(cast)
        self._handle_enemy_player(cast)
        self._player_on_ground = False
        self._player_on_ceiling = False
        self._handle_platforms(cast)
        self._handle_player_ground(cast)
        self._handle_player_coin(cast)
        self._handle_coin_ground(cast)
        self._handle_pickups_ground(cast)

    def _handle_enemy_wall(self, cast):
        enemies = cast["enemies"]
        walls = cast["walls"]
        platforms = cast["platforms"]
        for enemy in enemies:
            self._enemy_on_wall = False
            self._enemy_on_ground = False
            for wall in walls:
                self._handle_entity_wall(enemy, wall)
                enemy.set_is_on_wall(self._enemy_on_wall) 
                enemy.set_is_on_ground(self._enemy_on_ground) 
            for platform in platforms:
                self._handle_entity_platform(enemy, platform)
                enemy.set_is_on_ground(self._enemy_on_ground)

    def _handle_player_ground(self, cast):
        player = cast["players"][0]
        walls = cast["walls"]
        if player.get_velocity().get_y() >= 0:
            walls.sort(key=lambda wall: wall.get_shortest_distance(player))
        else:
            walls.sort(reverse=True, key=lambda wall: wall.get_shortest_distance(player))
        for wall in walls:
            self._handle_entity_wall(player, wall)
        player.set_is_on_ground(self._player_on_ground)   
        player.set_is_on_ceiling(self._player_on_ceiling) 

    def _handle_platforms(self, cast):
        player = cast["players"][0]
        platforms = cast["platforms"]
        coins = cast["coins"]
        pickups = cast["pickups"]
        for platform in platforms:
            self._handle_entity_platform(player, platform)
        player.set_is_on_ground(self._player_on_ground)  
        for coin in coins:
            for platform in platforms:
                self._handle_entity_platform(coin, platform)
        for pickup in pickups:
            for platform in platforms:
                self._handle_entity_platform(pickup, platform)


    def _handle_entity_wall(self, entity, wall):
            x, y, px, py = self._update_entity_position(entity)
            if self._physics_service.is_collision(entity, wall) and entity.has_collision():
                if  wall.get_left_edge() <= entity.get_right_edge() <= wall.get_left_edge() + 10 and wall.get_top_edge() - entity.get_height()/2 + 1<= py <= wall.get_bottom_edge() + entity.get_height()/2 - 1:
                    entity.set_position(Point(wall.get_left_edge() - entity.get_width(), y))
                    self._enemy_on_wall = True
                elif wall.get_right_edge() - 10 <= entity.get_left_edge() <= wall.get_right_edge() and wall.get_top_edge() - entity.get_height()/2 + 1 <= py <= wall.get_bottom_edge() + entity.get_height()/2 - 1:
                    entity.set_position(Point(wall.get_right_edge(), y))
                    self._enemy_on_wall = True
                elif wall.get_bottom_edge() - 10 <= entity.get_top_edge() <= wall.get_bottom_edge() and wall.get_left_edge() - entity.get_width()/2 + 1 <= px <= wall.get_right_edge() + entity.get_width()/2 - 1:
                    entity.set_position(Point(x, wall.get_bottom_edge()))
                    if entity.get_color() == constants.PLAYER_COLOR or entity.get_color() == constants.PLAYER_INV_COLOR:
                        self._player_on_ceiling = True
                elif wall.get_top_edge() <= entity.get_bottom_edge() <= wall.get_top_edge() + 10 and wall.get_left_edge() - entity.get_width()/2 + 1 <= px <= wall.get_right_edge() + entity.get_width()/2 - 1:
                    entity.set_position(Point(x, wall.get_top_edge() - entity.get_height()))
                    if (entity.get_color() == constants.PLAYER_COLOR or entity.get_color() == constants.PLAYER_INV_COLOR) and entity.get_velocity().get_y() >= 0:
                        self._player_on_ground = True
                    elif entity.get_color() == constants.ENEMY_COLOR:
                        self._enemy_on_ground = True

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
        gun = cast["guns"][0]
        stats = gun.get_gun_stats()
        damage = stats[8]
        bullets_to_remove = []
        for bullet in cast["bullets"]:
            for enemy in cast ["enemies"]:
                if self._physics_service.is_collision(bullet, enemy):
                    enemy.take_damage(damage)
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

    def _handle_entity_platform(self, entity, platform):
            x, y, px, py = self._update_entity_position(entity)
            wx = int(platform.get_position().get_x() + platform.get_width()/2)
            wy = int(platform.get_position().get_y() + platform.get_height()/2)

            if self._physics_service.is_collision(entity, platform) and not entity.get_is_crouched() and entity.has_gravity():
                if platform.get_top_edge() <= entity.get_bottom_edge() <= platform.get_top_edge() + 10 and platform.get_left_edge() - entity.get_width()/2 <= px <= platform.get_right_edge() + entity.get_width()/2:
                    entity.set_position(Point(x, platform.get_top_edge() - entity.get_height()))
                    if (entity.get_color() == constants.PLAYER_COLOR or entity.get_color() == constants.PLAYER_INV_COLOR) and entity.get_velocity().get_y() >= 0:
                        self._player_on_ground = True
                    elif entity.get_color() == constants.ENEMY_COLOR:
                        self._enemy_on_ground = True

    def _handle_player_coin(self, cast):
        coins = cast["coins"]
        player = cast["players"][0]
        coins_to_remove = []
        for coin in coins:
            if self._physics_service.is_collision(player, coin):
                coins_to_remove.append(coin)
        for coin in coins_to_remove:
            coins.remove(coin)

    def _handle_coin_ground(self, cast):
        coins = cast["coins"]
        walls = cast["walls"]
        for coin in coins:
            for wall in walls:
                self._handle_entity_wall(coin, wall)

    def _handle_pickups_ground(self, cast):
        pickups = cast["pickups"]
        walls = cast["walls"]
        for pickup in pickups:
            for wall in walls:
                self._handle_entity_wall(pickup, wall)