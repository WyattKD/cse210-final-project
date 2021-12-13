from game import constants
import raylibpy

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        None
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        self._textures = {}

    def open_window(self, title):
        """
        Opens a new window with the provided title.
        """
        raylibpy.init_window(constants.MAX_X, constants.MAX_Y, title)
        raylibpy.set_target_fps(constants.FRAME_RATE)
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.begin_drawing()
        raylibpy.clear_background(raylibpy.BLACK)

    def draw_box(self, x, y, width, height, color):
        """
        Draws at rectangular box with the provided specifications.
        """
        raylibpy.draw_rectangle(x, y, width, height, color)

    def draw_text(self, x, y, text, font_size, color):
        """
        Outputs the provided text at the desired location.
        """

        raylibpy.draw_text(text, x + 5, y + 5, font_size, color)

    def draw_image(self, x, y, image, tint):
        """
        Outputs the provided image on the screen.
        """
        if image not in self._textures.keys():

            loaded = raylibpy.load_texture(image)
            self._textures[image] = loaded

        texture = self._textures[image]
        raylibpy.draw_texture(texture, x, y, tint)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()

        if actor.has_image():
            image = actor.get_image()
            if (actor.get_color() == constants.PLAYER_COLOR or actor.get_color() == constants.PLAYER_INV_COLOR):
                self.draw_image(x - width / 2, y, image, actor.get_tint())
            else:
                self.draw_image(x, y, image, actor.get_tint())

            
        elif actor.has_text():
            text = actor.get_text()
            if not actor.has_color():
                color = raylibpy.WHITE
            self.draw_text(x, y, actor.get_text(), actor.get_font_size(), actor.get_color())
        elif actor.has_color():
            color = actor.get_color()
            self.draw_box(x, y, width, height, color)
        elif width > 0 and height > 0:
            self.draw_box(x, y, width, height, raylibpy.BLUE)
        
    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.end_drawing()
