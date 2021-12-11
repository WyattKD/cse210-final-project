import os
import raylibpy
MAX_X = 1000
MAX_Y = 800
FRAME_RATE = 60

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

PLAYER_WIDTH = 48
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
WALKER_WIDTH = 52
WALKER_HEIGHT = 80

FLYER_SPEED = 2
FLYER_WIDTH = 60
FLYER_HEIGHT = 51

MOVER_SPEED = 4
MOVER_WIDTH = 100
MOVER_HEIGHT = 100

COIN_WIDTH = 20
COIN_HEIGHT = 20
COIN_COLOR = raylibpy.GOLD
COIN_SPEED = 10
COIN_AIR_TIME = 0.1

DOOR_COLOR = raylibpy.DARKGREEN

HEALTH_PICKUP_COLOR = raylibpy.GREEN
HEALTH_PICKUP_WIDTH = 41
HEALTH_PICKUP_HEIGHT = 50

WEAPON_PICKUP_COLOR = raylibpy.ORANGE
WEAPON_PICKUP_WIDTH = 50
WEAPON_PICKUP_HEIGHT = 50

WALL_IMAGE = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/Wall.png")
WALL_IMAGE_LONG = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/long_wall.png")
WALL_IMAGE_TALL = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tall_wall.png")
WALL_IMAGE_LONG_BLOCK = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/long_block.png")
WALL_IMAGE_TALL_BLOCK = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tall_block.png")
WALL_IMAGE_11 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_11.png")
WALL_IMAGE_12 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_12.png")
WALL_IMAGE_13 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_13.png")
WALL_IMAGE_14 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/wall_14.png")

WALL_IMAGE_LONG_DOOR = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/long_door.png")
WALL_IMAGE_TALL_DOOR = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tall_door.png")

PLATFORM_IMAGE_SHORT = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/short_platform.png")
PLATFORM_IMAGE_MEDIUM = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/medium_platform.png")
PLATFORM_IMAGE_LONG = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/long_platform.png")
PLATFORM_IMAGE_FULL = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/full_platform.png")

BACKGROUND_IMAGE = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/background.png")

PLAYER_IMAGE = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player.png")

PLAYER_LEFT = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_left.png")
PLAYER_RIGHT = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_right.png")
PLAYER_UP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_up.png")
PLAYER_DOWN = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_down.png")
PLAYER_LEFTUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_leftup.png")
PLAYER_LEFTDOWN = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_leftdown.png")
PLAYER_RIGHTUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_rightup.png")
PLAYER_RIGHTDOWN = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_rightdown.png")
PLAYER_IDLE_LEFT = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_idle_left.png")
PLAYER_IDLE_RIGHT = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_idle_right.png")

HP_BAR_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/hp_bar_3.png")
HP_BAR_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/hp_bar_2.png")
HP_BAR_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/hp_bar_1.png")
HP_BAR_0 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/hp_bar_0.png")

WALK_ANIMATION = [os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation1.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation2.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation3.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animation4.png")]
WALK_ANIMATION2 = [os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf1.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf2.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf3.png"), os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walk_animationf4.png")]

COIN_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/coin_animation1.png")
COIN_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/coin_animation2.png")
COIN_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/coin_animation3.png")
COIN_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/coin_animation4.png")
COIN_ANIMATION = [COIN_ANIMATION_1, COIN_ANIMATION_2, COIN_ANIMATION_3, COIN_ANIMATION_4]

HEALTH_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation1.png")
HEALTH_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation2.png")
HEALTH_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation3.png")
HEALTH_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation4.png")
HEALTH_ANIMATION_5 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation5.png")
HEALTH_ANIMATION_6 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation6.png")
HEALTH_ANIMATION_7 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation7.png")
HEALTH_ANIMATION_8 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/health_animation8.png")
HEALTH_ANIMATION = [HEALTH_ANIMATION_1, HEALTH_ANIMATION_2, HEALTH_ANIMATION_3, HEALTH_ANIMATION_4, HEALTH_ANIMATION_5, HEALTH_ANIMATION_6, HEALTH_ANIMATION_7, HEALTH_ANIMATION_8]

FLYER_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyer1.png")
FLYER_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyer2.png")
FLYER_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyer3.png")
FLYER_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyer4.png")
FLYER_ANIMATION = [FLYER_ANIMATION_1, FLYER_ANIMATION_2, FLYER_ANIMATION_3, FLYER_ANIMATION_4]

FLYER_ANIMATIONF_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyerf1.png")
FLYER_ANIMATIONF_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyerf2.png")
FLYER_ANIMATIONF_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyerf3.png")
FLYER_ANIMATIONF_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/flyerf4.png")
FLYER_ANIMATIONF = [FLYER_ANIMATIONF_1, FLYER_ANIMATIONF_2, FLYER_ANIMATIONF_3, FLYER_ANIMATIONF_4]

MOVER_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover1.png")
MOVER_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover2.png")
MOVER_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover3.png")
MOVER_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover4.png")
MOVER_ANIMATION_5 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover5.png")
MOVER_ANIMATION_6 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover6.png")
MOVER_ANIMATION_7 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover7.png")
MOVER_ANIMATION_8 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover8.png")
MOVER_ANIMATION_9 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover9.png")
MOVER_ANIMATION_10 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover10.png")
MOVER_ANIMATION_11 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover11.png")
MOVER_ANIMATION_12 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/mover12.png")
MOVER_ANIMATION = [MOVER_ANIMATION_1, MOVER_ANIMATION_2, MOVER_ANIMATION_3, MOVER_ANIMATION_4, MOVER_ANIMATION_5, MOVER_ANIMATION_6, MOVER_ANIMATION_7, MOVER_ANIMATION_8, MOVER_ANIMATION_9, MOVER_ANIMATION_10, MOVER_ANIMATION_11, MOVER_ANIMATION_12]

WALKER_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walker1.png")
WALKER_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walker2.png")
WALKER_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walker3.png")
WALKER_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walker4.png")
WALKER_ANIMATION = [WALKER_ANIMATION_1, WALKER_ANIMATION_2, WALKER_ANIMATION_3, WALKER_ANIMATION_4]

WALKER_ANIMATIONF_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walkerf1.png")
WALKER_ANIMATIONF_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walkerf2.png")
WALKER_ANIMATIONF_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walkerf3.png")
WALKER_ANIMATIONF_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/walkerf4.png")
WALKER_ANIMATIONF = [WALKER_ANIMATIONF_1, WALKER_ANIMATIONF_2, WALKER_ANIMATIONF_3, WALKER_ANIMATIONF_4]

PISTOL_BULLET = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/pistol_bullet.png")
SNIPER_BULLET = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/sniper_bullet.png")
SHOTGUN_BULLET = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/shotgun_bullet.png")
RIFLE_BULLET = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/rifle_bullet.png")
BURST_RIFLE_BULLET = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/burst_rifle_bullet.png")
BUBBLE_BULLET = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/bubble_bullet.png")
LASER_BULLET = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/laser_bullet.png")

PISTOL_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/pistol_pickup.png")
DUAL_PISTOL_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/dual_pistol_pickup.png")
MACHINE_GUN_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/machinegun_pickup.png")
SNIPER_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/sniper_pickup.png")
SHOTGUN_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/shotgun_pickup.png")
MINIGUN_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/minigun_pickup.png")
RIFLE_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/rifle_pickup.png")
BURST_RIFLE_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/burst_rifle_pickup.png")
BUBBLE_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/bubble_pickup.png")
LASER_PICKUP = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/laser_pickup.png")

LEFT_DEATH_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left1.png")
LEFT_DEATH_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left2.png")
LEFT_DEATH_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left3.png")
LEFT_DEATH_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left4.png")
LEFT_DEATH_ANIMATION_5 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left5.png")
LEFT_DEATH_ANIMATION_6 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left6.png")
LEFT_DEATH_ANIMATION_7 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left7.png")
LEFT_DEATH_ANIMATION_8 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left8.png")
LEFT_DEATH_ANIMATION_9 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_left9.png")
LEFT_DEATH_ANIMATION = [LEFT_DEATH_ANIMATION_1, LEFT_DEATH_ANIMATION_2, LEFT_DEATH_ANIMATION_3, LEFT_DEATH_ANIMATION_4, LEFT_DEATH_ANIMATION_5, LEFT_DEATH_ANIMATION_6, LEFT_DEATH_ANIMATION_7, LEFT_DEATH_ANIMATION_8, LEFT_DEATH_ANIMATION_9]

RIGHT_DEATH_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right1.png")
RIGHT_DEATH_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right2.png")
RIGHT_DEATH_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right3.png")
RIGHT_DEATH_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right4.png")
RIGHT_DEATH_ANIMATION_5 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right5.png")
RIGHT_DEATH_ANIMATION_6 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right6.png")
RIGHT_DEATH_ANIMATION_7 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right7.png")
RIGHT_DEATH_ANIMATION_8 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right8.png")
RIGHT_DEATH_ANIMATION_9 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/player_death_right9.png")
RIGHT_DEATH_ANIMATION = [RIGHT_DEATH_ANIMATION_1, RIGHT_DEATH_ANIMATION_2, RIGHT_DEATH_ANIMATION_3, RIGHT_DEATH_ANIMATION_4, RIGHT_DEATH_ANIMATION_5, RIGHT_DEATH_ANIMATION_6, RIGHT_DEATH_ANIMATION_7, RIGHT_DEATH_ANIMATION_8, RIGHT_DEATH_ANIMATION_9]

TUTORIAL_ANIMATION_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial1.png")
TUTORIAL_ANIMATION_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial2.png")
TUTORIAL_ANIMATION_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial3.png")
TUTORIAL_ANIMATION_4 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial4.png")
TUTORIAL_ANIMATION_5 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial5.png")
TUTORIAL_ANIMATION_6 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial6.png")
TUTORIAL_ANIMATION_7 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial7.png")
TUTORIAL_ANIMATION_8 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/tutorial8.png")
TUTORIAL_ANIMATION = [TUTORIAL_ANIMATION_1, TUTORIAL_ANIMATION_2, TUTORIAL_ANIMATION_3, TUTORIAL_ANIMATION_4, TUTORIAL_ANIMATION_5, TUTORIAL_ANIMATION_6, TUTORIAL_ANIMATION_7, TUTORIAL_ANIMATION_8]
TUTORIAL_WIDTH = 360
TUTORIAL_HEIGHT = 240

GAMEOVER_1 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/gameover1.png")
GAMEOVER_2 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/gameover2.png")
GAMEOVER_3 = os.path.join(os.getcwd(), "cse210-programs/cse210-final-project//assets/gameover3.png")