frame_wait = 24
SCREEN_SIZE = (WIDTH, HEIGHT) = (1280, 720)
FULLSCREEN_DEFAULT = False
quit_flag = "QUIT"
keydown_flag = "KEYDOWN"
hero_hp = 100
monster_hp = 20
map_width_default = 6
map_height_default = 6
map_rooms_default = 1
cell_size = 64

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

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
}
