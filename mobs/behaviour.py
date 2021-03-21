from setting_files import settings
from setting_files.utils import direct_coord, map_coord
from random import choice


class Behaviour:
    priority = 0

    @staticmethod
    def act(mob, level):
        pass


class Wander(Behaviour):
    @staticmethod
    def act(mob, level):
        positions = [d for d in settings.move_keys.values()
                     if level.is_empty(map_coord(direct_coord(mob.coord, d)))]
        if positions:
            direction = choice(positions)
            mob.move(level, direction)
