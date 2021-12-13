from game.actors.actor import Actor
from game.point import Point
from game import constants
from random import uniform

class Bullet(Actor):

    def __init__(self, direction, x, y, stats):
        super().__init__()
        bullet_width = stats[0]
        bullet_height = stats[1]
        bullet_color = stats[2]
        bullet_speed = stats[3]
        bullet_spread = stats[6]
        bullet_image = stats[10]
        self.set_width(bullet_width)
        self.set_height(bullet_height)
        self.set_color(bullet_color)
        self.set_position(Point(x - bullet_width/2, y - bullet_height/2))
        self.set_image(bullet_image)
        self._spawn_point = self.get_position() 
        if direction == "left":
            spread = uniform(-1 * bullet_spread, bullet_spread)
            self.set_velocity(Point(-1 * bullet_speed, spread))
        elif direction == "right":
            spread = uniform(-1 * bullet_spread, bullet_spread)
            self.set_velocity(Point(bullet_speed, spread))
        elif direction == "up":
            spread = uniform(-1 * bullet_spread, bullet_spread)
            self.set_velocity(Point(spread, -1 * bullet_speed))
        elif direction == "down":
            spread = uniform(-1 * bullet_spread, bullet_spread)
            self.set_velocity(Point(spread, bullet_speed))
        elif direction == "leftup":
            spread = uniform(-1 * bullet_spread, bullet_spread)/2
            self.set_velocity(Point(-1 * bullet_speed/2 - spread, -1 * bullet_speed/2 + spread))
        elif direction == "rightup":
            spread = uniform(-1 * bullet_spread, bullet_spread)/2
            self.set_velocity(Point(bullet_speed/2 + spread, -1 * bullet_speed/2 + spread))
        elif direction == "leftdown":
            spread = uniform(-1 * bullet_spread, bullet_spread)/2
            self.set_velocity(Point(-1 * bullet_speed/2 + spread, bullet_speed/2 + spread))
        elif direction == "rightdown":
            spread = uniform(-1 * bullet_spread, bullet_spread)/2
            self.set_velocity(Point(bullet_speed/2 - spread, bullet_speed/2 + spread))

    def get_spawn_point(self):
        return self._spawn_point

    def bullet_step(self, steps):
        dx = self.get_velocity().get_x() * steps
        dy = self.get_velocity().get_y() * steps
        bx = self.get_position().get_x()
        by = self.get_position().get_y()  
        self.set_position(Point((bx + dx) % constants.MAX_X, (by + dy) % constants.MAX_Y))