from setting_files import settings
from mobs.mob import Mob


class Monster(Mob):
    def __init__(self):
        super().__init__()
        self.hp = settings.monster_hp

    def draw(self):
        pass
