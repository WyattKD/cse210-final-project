from game.actors.actor import Actor
from game.point import Point
from game import constants

class Bullet(Actor):

    def __init__(self, direction, x, y):
        super().__init__()
        self.set_width(constants.BULLET_WIDTH)
        self.set_height(constants.BULLET_HEIGHT)
        self.set_color(constants.BULLET_COLOR)
        self.set_position(Point(x - constants.BULLET_WIDTH/2, y - constants.BULLET_HEIGHT/2))
        if direction == "left":
            self.set_velocity(Point(-1 * constants.BULLET_SPEED, 0))
        elif direction == "right":
            self.set_velocity(Point(constants.BULLET_SPEED, 0))
        elif direction == "up":
            self.set_velocity(Point(0, -1 * constants.BULLET_SPEED))
        elif direction == "down":
            self.set_velocity(Point(0, constants.BULLET_SPEED))
        elif direction == "leftup":
            self.set_velocity(Point(-1 * constants.BULLET_SPEED/2, -1 * constants.BULLET_SPEED/2))
        elif direction == "rightup":
            self.set_velocity(Point(constants.BULLET_SPEED/2, -1 * constants.BULLET_SPEED/2))
        elif direction == "leftdown":
            self.set_velocity(Point(-1 * constants.BULLET_SPEED/2, constants.BULLET_SPEED/2))
        elif direction == "rightdown":
            self.set_velocity(Point(constants.BULLET_SPEED/2, constants.BULLET_SPEED/2))