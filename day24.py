import os.path
import re


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read().splitlines()
        return lines


def parse_input(data):
    out = []
    regex = '[ns]?[ew]'
    for line in data:
        m = re.findall(regex, line)
        out.append(m)
    return out


class Tile:
    """A tile represented with cube coordinates"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.white = True

    def flip_color(self):
        self.white = not self.white

    def consume_serie_of_moves(self, moves):
        for move in moves:
            self.move(move)

    def move(self, direction):
        if direction == 'e':
            self.x += 1
            self.y -= 1
        elif direction == 'w':
            self.x -= 1
            self.y += 1
        elif direction == 'ne':
            self.x += 1
            self.z -= 1
        elif direction == 'sw':
            self.x -= 1
            self.z += 1
        elif direction == 'nw':
            self.y += 1
            self.z -= 1
        elif direction == 'se':
            self.y -= 1
            self.z += 1


class Floor:
    def __init__(self):
        self.hm = {}

    def get_tile_key(self, x, y, z):
        return str(x) + '#' + str(y) + '#' + str(z)

    def get_existing_tile(self, tile):
        key = self.get_tile_key(tile.x, tile.y, tile.z)
        if key not in self.hm:
            self.hm[key] = tile
        return self.hm[key]

    def get_black_count(self):
        return len([x for x in self.hm.values() if not x.white])


def part1(data):
    dirs = parse_input(data)
    floor = Floor()
    for dir_line in dirs:
        tile = Tile(0, 0, 0)
        tile.consume_serie_of_moves(dir_line)
        tile = floor.get_existing_tile(tile)
        tile.flip_color()
    return floor.get_black_count()
# 385 too high
# 337 too low


def part2(data):
    pass


if __name__ == '__main__':
    DAY = 24
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
