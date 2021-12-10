from game import constants
from game.point import Point
from time import time
import raylibpy

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
        _width (int): The actor's width
        _height (int): The actor's height
        _image (string): The file path of the image file (if present)
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = 0
        self._height = 0
        self._image = ""
        self._color = ""
        self._has_gravity = False
        self._is_on_ground = False
        self._collision = True
        self._frame_time = round(time(), 2)
        self._animation = ""
        self._frame_index = 0
        self._tint = raylibpy.WHITE

    def set_tint(self, tint):
        self._tint = tint

    def get_tint(self):
        return self._tint

    def set_frame_index(self, num):
        self._frame_index = num

    def get_frame_index(self):
        return self._frame_index

    def has_gravity(self):
        return self._has_gravity

    def set_gravity(self, status):
        self._has_gravity = status

    def get_is_on_ground(self):
        return self._is_on_ground

    def set_is_on_ground(self, status):
        self._is_on_ground = status

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
    
    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_image(self):
        return self._image
    
    def set_image(self, image):
        self._image = image

    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color

    def get_left_edge(self):
        return self._position.get_x()

    def get_right_edge(self):
        return self._position.get_x() + self._width

    def get_top_edge(self):
        return self._position.get_y()

    def get_bottom_edge(self):
        return self._position.get_y() + self._height

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def set_text(self, text):
        self._text = text

    def has_animation(self):
        return self._animation != ""

    def get_animation(self):
        return self._animation

    def set_animation(self, animation):
        self._animation = animation

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            self (Actor): An instance of Actor.
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given velocity.
        """
        self._velocity = velocity

    def set_frame_time(self):
        self._frame_time = round(time(), 2)

    def get_frame_time(self):
        return self._frame_time
    def has_text(self):
        return self._text != ""

    def has_image(self):
        return self._image != ""

    def has_color(self):
        return self._color != ""

    def has_collision(self):
        return self._collision

    def set_collision(self, status):
        self._collision = status

