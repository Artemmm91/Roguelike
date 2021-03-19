SCREEN_SIZE = (WIDTH, HEIGHT) = (1280, 720)
FULLSCREEN_DEFAULT = False

hero_hp = 100
monster_hp = 20

cell_size = 64

frame_tick = 8
frame_wait = 24
animation_wait = 2
animation_frames = 2

colors = {
    "BLACK": (0, 0, 0),
    "GREEN": (0, 255, 0)
}

quit_flag = "QUIT"
keydown_flag = "KEYDOWN"

escape_key = "ESCAPE"
down_key = "DOWN"
up_key = "UP"
left_key = "LEFT"
right_key = "RIGHT"

move_keys = {
    down_key: (0, 1),
    up_key: (0, -1),
    left_key: (-1, 0),
    right_key: (1, 0)
}

map_symbols = {
    9: "empty",
    0: "floor",
    1: "wall",
    2: "monster",
}
