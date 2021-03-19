from map.table_map import Map
from setting_files import settings


def read_map(filename):
    field = open(filename, "r")
    table_map = []
    max_length = 0
    hero_pos = None
    monsters_pos = []
    i = 0
    for line in field:
        new_line = [9]
        max_length = max(max_length, len(line))
        j = 0
        for symbol in line:
            if symbol == "#":
                new_line.append(1)
            elif symbol == "h":
                new_line.append(0)
                hero_pos = [(j + 1) * settings.cell_size, (i + 1) * settings.cell_size]
            elif symbol == "m":
                new_line.append(2)
                monsters_pos.append(((j + 1) * settings.cell_size, (i + 1) * settings.cell_size))
            elif symbol == " ":
                new_line.append(9)
            elif symbol == "_":
                new_line.append(0)
            j += 1
        i += 1
        table_map.append(new_line)

    max_length += 1

    line1 = [9] * (max_length + 1)

    for line in table_map:
        while len(line) < max_length:
            line.append(9)
        line.append(9)

    table_map.insert(0, line1)
    table_map.append(line1)

    return Map(table_map, hero_pos, monsters_pos)


def generate_map():
    return read_map("map/map_example.txt")
