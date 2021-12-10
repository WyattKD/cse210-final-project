from game.actors.actor import Actor
from game.point import Point
from game import constants

class Text(Actor):

    def __init__(self, text, position, font_size, color):
        super().__init__()
        self.set_color(color)
        self.set_font_size(font_size)
        self.set_text(text)
        self.set_position(position)

    def set_font_size(self, font_size):
        self._font_size = font_size

    def get_font_size(self):
        return self._font_size