import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_inputs(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
    
        inputs = ""

        if self.is_a_pressed():
            inputs += "a"
        
        if self.is_d_pressed():
            inputs += "d"
        
        if self.is_w_pressed():
            inputs += "w"
        
        if self.is_s_pressed():
            inputs += "s"
        
        return inputs

    def is_a_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_A)

    def is_d_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_D)

    def is_w_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_W)

    def is_s_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_S)

    def window_should_close(self):
        return raylibpy.window_should_close()
