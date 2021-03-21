from setting_files.utils import *
from mobs.mob import Mob
from resources.resources import data


class Hero(Mob):
    def __init__(self):
        super().__init__(data.player[settings.left_key])
        self.hp = settings.hero_hp
        self.direction_image = settings.left_key
        self.shift = (0, 0)

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

    def update(self, display):
        super(Hero, self).update(display)
        self.frames = data.player[self.direction_image]
        if self.animation:
            try:
                next(self.animation)
                display.shift_camera(self.last_image_shift)
                self.last_image_shift = (0, 0)
            except StopIteration:
                self.set_animation(None)
        else:
            self.set_image()
        display_coord = center(display.screen.get_size())
        display.camera = list(shift_coord(self.image_coord, display_coord, -1))
