from random import choice
from setting_files import settings
from graphics.interface import interface
from resources.resources import data
from setting_files import block_names
from setting_files.utils import cartesian_coord, map_coord
from mobs.monsters import Demon
from mobs.hero import Hero


MONSTERS = [Demon]


class Map:
    def __init__(self, table_map, hero_coord, monster_coord):
        self.table = table_map
        self.table_size = (len(self.table), len(self.table[0]))
        self.hero_coord = hero_coord
        self.hero = None
        self.monster_coord = monster_coord
        self.mobs = {}
        self.rendered_map = None
        self.image = None
        self.current_animations = 0

    def get_position(self, coord):
        if coord[0] < 0 or coord[0] >= self.table_size[1] or coord[1] < 0 or coord[1] >= self.table_size[0]:
            return "nothing"
        return settings.map_symbols[self.table[coord[1]][coord[0]]]

    def is_empty(self, coord):
        object_coord = self.get_position(coord)
        if object_coord == "floor":
            return True
        return False

    def update(self, display):
        self.image.set_rect((-display.camera[0], -display.camera[1]))

    def find_neighbour_walls(self, pos):
        x, y = pos
        code = ""
        if self.table[x + 1][y] == 1:
            code += 'd'
        if self.table[x - 1][y] == 1:
            code += 'u'
        if self.table[x][y - 1] == 1:
            code += 'l'
        if self.table[x][y + 1] == 1:
            code += 'r'
        return code

    def type_floor(self, pos):
        return block_names.floors[self.find_neighbour_walls(pos)]

    def type_wall(self, pos):
        neighbours = self.find_neighbour_walls(pos)
        if neighbours in block_names.walls:
            return block_names.walls[neighbours]
        return "full"

    def render_map(self):
        map_size = cartesian_coord(self.table_size, True)
        self.rendered_map = interface.Image(image=None, size=map_size)
        for y in range(self.table_size[0]):
            for x in range(self.table_size[1]):
                cell_type = settings.map_symbols[self.table[y][x]]
                cell = interface.Image(image=None, size=(settings.cell_size, settings.cell_size))
                if cell_type in ["floor", "monster", "hero"]:
                    cell = data.floors[self.type_floor((y, x))]
                elif cell_type == "wall":
                    cell = data.walls[self.type_wall((y, x))]
                cell.set_rect(cartesian_coord((x, y)))
                self.rendered_map.merge(cell)
        self.image = self.rendered_map

    def draw(self, display):
        display.draw_image(self.image)

    def set_table(self, coord, value):
        x, y = map_coord(coord)
        self.table[y][x] = value

    def place_mob(self, mob, coord):
        if mob.coord:
            del self.mobs[(mob.coord[0], mob.coord[1])]
            self.set_table(mob.coord, 0)
        mob.set_coord(coord)
        self.mobs[coord] = mob

        mob_value = 3
        if self.hero == mob:
            mob_value = 2
        self.set_table(mob.coord, mob_value)

    def spawn_monsters(self):
        for monster_pos in self.monster_coord:
            current_monster = choice(MONSTERS)
            new_monster = current_monster()
            self.place_mob(new_monster, monster_pos)
            new_monster.move_image(monster_pos)

    def spawn_hero(self):
        self.hero = Hero()
        self.place_mob(self.hero, tuple(self.hero_coord))
        self.hero.move_image(self.hero.coord)
