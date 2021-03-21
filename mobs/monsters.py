from setting_files.utils import shift_coord
from mobs.mob import Mob
from resources.resources import data
from mobs.behaviour import *


class Monster(Mob):
    def __init__(self, frames):
        super().__init__(frames)
        self.hp = settings.monster_hp
        self.behaviours = []

    def update(self, display):
        super(Monster, self).update(display)
        if self.animation:
            try:
                next(self.animation)
            except StopIteration:
                self.set_animation(None)
        else:
            self.set_image()

    def walk_animation(self, direction):
        for frame in range(settings.animation_frames):
            for step in range(settings.animation_wait):
                yield
            if direction is not None:
                coefficient = settings.cell_size // settings.animation_frames
                shift = (coefficient * direction[0], coefficient * direction[1])
                self.move_image(shift_coord(self.image_coord, shift))
            self.set_image("walk")  # need to be walking animation frame

    def move(self, level, direction):
        level.place_mob(self, direct_coord(self.coord, direction))
        self.set_animation(self.walk_animation(direction))

    def act(self, level):
        for behaviour in self.behaviours:
            behaviour.act(self, level)

    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)
        self.behaviours.sort(key=lambda b: -b.priority)


class Demon(Monster):
    def __init__(self):
        super(Demon, self).__init__(choice(data.monsters["demon"]))
        self.add_behaviour(Wander)
