import os.path
import re
from itertools import permutations


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
        self.will_flip = False

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

    def get_tile_if_exists(self, tile):
        key = self.get_tile_key(tile.x, tile.y, tile.z)
        if key not in self.hm:
            self.hm[key] = tile
        return self.hm[key]

    def get_black_count(self):
        return len([x for x in self.hm.values() if not x.white])

    def get_scope(self):
        x = [0, 0]
        y = [0, 0]
        z = [0, 0]
        for tile in self.hm.values():
            if tile.x < x[0]:
                x[0] = tile.x
            elif tile.x > x[1]:
                x[1] = tile.x
            if tile.y < y[0]:
                y[0] = tile.y
            elif tile.y > y[1]:
                y[1] = tile.y
            if tile.z < z[0]:
                z[0] = tile.z
            elif tile.z > z[1]:
                z[1] = tile.z

        return x, y, z

    def is_black(self, x, y, z):
        key = self.get_tile_key(x, y, z)
        if self.hm.get(key) and not self.hm.get(key).white:
            return True
        return False

    def get_adj_tiles_coords(self, x, y, z):
        ps = permutations(range(-1, 2), 3)
        return [[x + p[0], y + [1], z + p[2]] for p in ps]

    def get_adj_tiles_black_count(self, x, y, z):
        bcount = 0
        for x_probe, y_probe, z_probe in self.get_adj_tiles_coords(x,y,z):
            if self.is_black(x_probe, y_probe, z_probe):
                bcount += 1
        return bcount

    def should_flip(self, is_white, bcount):
        if is_white and bcount == 2:
            return True
        elif not is_white and (bcount == 0 or bcount > 2):
            return True
        return False

    def apply_flipping(self):
        count = 0
        for tile in self.hm.values():
            if tile.will_flip:
                tile.flip_color()
                count += 1

    def do_art(self):
        x_scope, y_scope, z_scope = self.get_scope()
        for x in range(x_scope[0] - 1, x_scope[1] + 2):
            for y in range(y_scope[0] - 1, y_scope[1] + 2):
                for z in range(z_scope[0] - 1, z_scope[1] + 2):
                    bcount = self.get_adj_tiles_black_count(x, y, z)
                    is_white = not self.is_black(x, y, z)
                    flip = self.should_flip(is_white, bcount)
                    if flip:
                        flip = self.get_tile_if_exists(Tile(x, y, z))
                        flip.will_flip = True

        self.apply_flipping()


def part1(data):
    dirs = parse_input(data)
    floor = Floor()
    for dir_line in dirs:
        tile = Tile(0, 0, 0)
        tile.consume_serie_of_moves(dir_line)
        tile = floor.get_tile_if_exists(tile)
        tile.flip_color()
    return floor


def part2(floor):
    for _ in range(10):
        floor.do_art()
    return floor.get_black_count()

# 12412 too high.


if __name__ == '__main__':
    DAY = 24
    input_data = get_input(DAY, False)
    p1_floor = part1(input_data)
    print(p1_floor.get_black_count())
    print(part2(p1_floor))
