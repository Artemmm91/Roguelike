from setting_files import settings
from mobs.mob import Mob
from resources.resources import data


def shift_coord(coord, shift):
    return coord[0] + shift[0], coord[1] + shift[1]


def center(window_size):
    center_screen = (window_size[0] // 2, window_size[1] // 2)
    half_side = settings.cell_size // 2
    return center_screen[0] - half_side, center_screen[1] - half_side


class Hero(Mob):
    def __init__(self):
        super().__init__(data.player[settings.left_key])
        self.hp = settings.hero_hp
        self.direction_image = settings.left_key
        self.shift = (0, 0)
        self.direct_coord = None

    def walk_animation(self, direction=None):
        for frame in range(settings.animation_frames):
            for step in range(settings.animation_wait):
                yield
            if direction is not None:
                coefficient = settings.cell_size // settings.animation_frames
                self.shift = (coefficient * direction[0], coefficient * direction[1])
                self.shift_coord(self.shift)
            self.set_image()  # need to be walking animation frame

    def act(self, key, level):
        if key not in settings.move_keys:
            return False
        direction = settings.move_keys[key]
        new_coord = shift_coord(self.coord, (direction[0] * settings.cell_size, direction[1] * settings.cell_size))
        new_map_coord = (new_coord[0] // settings.cell_size, new_coord[1] // settings.cell_size)
        object_coord = level.get_position(new_map_coord)
        if object_coord == "floor":
            self.direct_coord = [new_coord[0], new_coord[1]]
            level.hero_coord = new_map_coord
            if key in [settings.left_key, settings.right_key]:
                self.direction_image = key
            self.animation = self.walk_animation(direction)
            return True
        return False

    def update(self, display):
        super(Hero, self).update(display)
        self.frames = data.player[self.direction_image]
        if self.animation:
            try:
                next(self.animation)
                display.shift_camera(self.shift)
                self.shift = (0, 0)
            except StopIteration:
                self.animation = None
                self.coord = self.direct_coord
                self.set_image()
        else:
            self.set_image()
        display_coord = center(display.screen.get_size())
        display.camera = [self.coord[0] - display_coord[0], self.coord[1] - display_coord[1]]
