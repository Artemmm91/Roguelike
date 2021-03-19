from setting_files import settings
from graphics.interface import interface
from resources.resources import data
from setting_files import block_names


def keys_in_dict(keys, dictionary):
    for k in keys:
        if k not in dictionary:
            return False
    return True


class Map:
    def __init__(self, map_coord, hero_coord):
        self.table = map_coord
        self.table_size = (len(self.table), len(self.table[0]))
        self.hero_coord = hero_coord
        self.rendered_map = None
        self.image = None

    def get_position(self, coord):
        if coord[0] < 0 or coord[0] >= self.table_size[1] or coord[1] < 0 or coord[1] >= self.table_size[0]:
            return "nothing"
        return settings.map_symbols[self.table[coord[1]][coord[0]]]

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
        map_size = (self.table_size[1] * settings.cell_size, self.table_size[0] * settings.cell_size)
        self.rendered_map = interface.Image(image=None, size=map_size)
        for y in range(self.table_size[0]):
            for x in range(self.table_size[1]):
                cell_type = settings.map_symbols[self.table[y][x]]
                cell = interface.Image(image=None, size=(settings.cell_size, settings.cell_size))
                if cell_type == "floor":
                    cell = data.floors[self.type_floor((y, x))]
                elif cell_type == "wall":
                    cell = data.walls[self.type_wall((y, x))]
                cell.set_rect((x * settings.cell_size, y * settings.cell_size))
                self.rendered_map.merge(cell)
        self.image = self.rendered_map

    def draw(self, display):
        display.draw_image(self.image)
