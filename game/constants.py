import os
import raylibpy
MAX_X = 1000
MAX_Y = 800
FRAME_RATE = 60

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

PLAYER_WIDTH = 70
PLAYER_HEIGHT = 89
PLAYER_SPEED = 6
PLAYER_COLOR = raylibpy.BLUE
PLAYER_INV_COLOR = raylibpy.WHITE
PLAYER_DEAD_COLOR = raylibpy.DARKGRAY

WALL_COLOR = raylibpy.GRAY
PLATFORM_COLOR = raylibpy.LIGHTGRAY

BULLET_WIDTH = 20
BULLET_HEIGHT = 20
BULLET_COLOR = raylibpy.YELLOW
BULLET_SPEED = 10
BULLET_TIME = 0.4

JUMP_SPEED = 1
GRAVITY = 1
JUMP_TIME = 0.3
SHOOT_TIME = 0.3
INVINCIBLE_TIME = 2

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40
ENEMY_COLOR = raylibpy.RED

WALKER_SPEED = 2
WALKER_JUMP_SPEED = 1
WALKER_JUMP_TIME = 1
WALKER_COOLDOWN = 0.4

FLYER_SPEED = 2
FLYER_WIDTH = 30
FLYER_HEIGHT = 30

MOVER_SPEED = 4
MOVER_WIDTH = 50
MOVER_HEIGHT = 50

COIN_WIDTH = 20
COIN_HEIGHT = 20
COIN_COLOR = raylibpy.GOLD
COIN_SPEED = 9
COIN_AIR_TIME = 0.1

DOOR_COLOR = raylibpy.DARKGREEN

HEALTH_PICKUP_COLOR = raylibpy.GREEN
HEALTH_PICKUP_WIDTH = 30
HEALTH_PICKUP_HEIGHT = 30

WEAPON_PICKUP_COLOR = raylibpy.ORANGE
WEAPON_PICKUP_WIDTH = 30
WEAPON_PICKUP_HEIGHT = 30

WALL_IMAGE = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/Wall.png")
WALL_IMAGE_LONG = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/long_wall.png")
WALL_IMAGE_TALL = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tall_wall.png")
WALL_IMAGE_LONG_BLOCK = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/long_block.png")
WALL_IMAGE_TALL_BLOCK = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tall_block.png")
WALL_IMAGE_11 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_11.png")
WALL_IMAGE_12 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_12.png")
WALL_IMAGE_13 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_13.png")
WALL_IMAGE_14 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_14.png")

PLATFORM_IMAGE_SHORT = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/short_platform.png")
PLATFORM_IMAGE_MEDIUM = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/medium_platform.png")
PLATFORM_IMAGE_LONG = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/long_platform.png")
PLATFORM_IMAGE_FULL = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/full_platform.png")

BACKGROUND_IMAGE = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/background.png")

PLAYER_IMAGE = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player.png")
HP_BAR_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/hp_bar_3.png")

WALK_ANIMATION = [os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation1.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation2.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation3.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation4.png")]
WALK_ANIMATION2 = [os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf1.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf2.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf3.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf4.png")]