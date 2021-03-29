from setting_files.utils import *
from mobs.mob import Mob
from resources.resources import data


def jump_function(dist):
    c = settings.cell_size
    return round(dist * (c - dist) * 2 / c)


def get_jump_shift(direction, dist):
    return dist * direction[0], dist * direction[1] - jump_function(dist)


class Hero(Mob):
    def __init__(self):
        super().__init__(data.player[settings.left_key])
        self.hp = settings.hero_hp
        self.direction_image = settings.left_key
        self.camera_shift = (0, 0)

    def act(self, key, level):
        if key in settings.move_keys:
            direction = settings.move_keys[key]
            new_coord = direct_coord(self.coord, direction)
            if level.is_empty(map_coord(new_coord)):
                level.place_mob(self, new_coord)
                if key in [settings.left_key, settings.right_key]:
                    self.direction_image = key
                self.set_animation(self.walk_animation(direction))
                return True
        return False

    def walk_animation(self, direction):
        shift_list = make_splitting(settings.cell_size, settings.animation_frames, direction)
        init_image_coord = self.image_coord
        distance = 0
        for shift in shift_list:
            self.camera_shift = shift
            yield
            distance += abs(shift[0] + shift[1])
            hero_shift = get_jump_shift(direction, distance)
            self.move_image(shift_coord(init_image_coord, hero_shift))
            self.set_image("walk")

    def update(self, display):
        self.frames = data.player[self.direction_image]
        super().update(display)
        display.shift_camera(self.camera_shift)
        self.camera_shift = (0, 0)

    def center_camera(self, display):
        display_coord = center(display.screen.get_size())
        display.camera = list(shift_coord(self.image_coord, display_coord, -1))
