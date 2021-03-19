from graphics.interface import interface
from setting_files import settings


def load_atlas(filename, width, height):
    image = interface.load_image(filename)
    image_width, image_height = image.get_size()
    return [
        [
            (image.subsurface((x * width, y * height, width, height))).scale((settings.cell_size, settings.cell_size))
            for x in range(image_width // width)
        ]
        for y in range(image_height // height)
    ]


def make_list_frames(frames, repeat):
    new_frames = []
    for frame in frames:
        new_frames.extend([frame] * repeat)

    return new_frames


class Resources(object):
    def __init__(self):
        self.wall_tiles = load_atlas("Wall.png", 16, 16)
        self.floor_tiles = load_atlas("Floor.png", 16, 16)
        self.player = [load_atlas("Player0.png", 16, 16), load_atlas("Player1.png", 16, 16),
                       load_atlas("Player0rev.png", 16, 16), load_atlas("Player1rev.png", 16, 16),]
        self.monsters = [load_atlas("Demon0.png", 16, 16), load_atlas("Demon1.png", 16, 16),]

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Resources, cls).__new__(cls)
        return cls.instance


resources = Resources()


class Design(object):
    def __init__(self, wall_set, floor_set, player_set, monster_set):
        x, y = floor_set
        self.floors = {
            "corner1": resources.floor_tiles[x][y],          # corner |'
            "corner2": resources.floor_tiles[x][y + 2],      # corner '|
            "corner3": resources.floor_tiles[x + 2][y + 2],  # corner _|
            "corner4": resources.floor_tiles[x + 2][y],      # corner |_
            "full": resources.floor_tiles[x + 1][y + 1],     # full cell
            "edge1": resources.floor_tiles[x + 1][y],        # |...
            "edge2": resources.floor_tiles[x][y + 1],        # '''
            "edge3": resources.floor_tiles[x + 1][y + 2],    # ...|
            "edge4": resources.floor_tiles[x + 2][y + 1],    # ___
            "hall1": resources.floor_tiles[x + 1][y + 5],    # up and down walls
            "hall2": resources.floor_tiles[x + 1][y + 3],    # left and right walls
            "end1": resources.floor_tiles[x + 1][y + 4],     # no wall ...|
            "end2": resources.floor_tiles[x][y + 3],         # no wall ___
            "end3": resources.floor_tiles[x + 1][y + 6],     # no wall |...
            "end4": resources.floor_tiles[x + 2][y + 3],     # no wall '''
            "zero": resources.floor_tiles[x][y + 5]          # only walls
        }

        x, y = wall_set
        self.walls = {
            "corner1": resources.wall_tiles[x][y],          # corner |'
            "corner2": resources.wall_tiles[x][y + 2],      # corner '|
            "corner3": resources.wall_tiles[x + 2][y + 2],  # corner _|
            "corner4": resources.wall_tiles[x + 2][y],      # corner |_
            "full": resources.wall_tiles[x + 1][y + 1],     # full cell
            "edge1": resources.wall_tiles[x + 1][y],        # |
            "edge3": resources.wall_tiles[x][y + 1],        # ___
        }

        x, y = player_set
        player_frames = [resources.player[0][x][y], resources.player[1][x][y]]
        player_rev_frames = [resources.player[2][x][7 - y], resources.player[3][x][7 - y]]
        self.player = {settings.left_key: make_list_frames(player_frames, settings.frame_tick),
                       settings.right_key: make_list_frames(player_rev_frames, settings.frame_tick)}

        self.monsters = {}
        for monster_type in monster_set:
            self.monsters[monster_type] = []
            for design in monster_set[monster_type]:
                x, y = design
                monster_frames = [resources.monsters[0][x][y], resources.monsters[1][x][y]]
                self.monsters[monster_type].append(make_list_frames(monster_frames, settings.frame_tick))

    def __new__(cls, wall_set, floor_set, player_set, monster_set):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Design, cls).__new__(cls)
        return cls.instance


monster_design = {
    "demon": ((3, 2), (1, 3), (1, 2), (1, 0))
}

data = Design((6, 0), (6, 0), (3, 3), monster_design)
