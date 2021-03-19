from setting_files import settings
from mobs.mob import Mob
from resources.resources import data
from random import choice


class Monster(Mob):
    def __init__(self, frames):
        super().__init__(frames)
        self.hp = settings.monster_hp
        self.direct_coord = None

    def update(self, display):
        super(Monster, self).update(display)
        if self.animation:
            try:
                next(self.animation)
            except StopIteration:
                self.animation = None
                self.coord = self.direct_coord
        else:
            self.set_image()


class Demon(Monster):
    def __init__(self):
        super(Demon, self).__init__(choice(data.monsters["demon"]))
