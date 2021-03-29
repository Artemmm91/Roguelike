from mobs.mob import Mob
from resources.resources import data
from mobs.behaviour import *


class Monster(Mob):
    def __init__(self, frames):
        super().__init__(frames)
        self.hp = settings.monster_hp
        self.behaviours = []

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
