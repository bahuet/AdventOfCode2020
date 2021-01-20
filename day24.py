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
        self.directions = [
            (+1, -1, 0), (+1, 0, -1), (0, +1, -1),
            (-1, +1, 0), (-1, 0, +1), (0, -1, +1),
        ]
        self.translate_table = {
            'e': 0,
            'w': 3,
            'ne': 1,
            'sw': 4,
            'nw': 2,
            'se': 5
        }

    def flip_color(self):
        self.white = not self.white

    def consume_serie_of_moves(self, moves):
        for move in moves:
            self.move(move)

    def move(self, cardinal_dir):
        move_values = self.directions[self.translate_table[cardinal_dir]]
        self.x += move_values[0]
        self.y += move_values[1]
        self.z += move_values[2]


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

    def get_max_radius(self):
        return max([max(tile.x, tile.y, tile.z) for tile in self.hm.values()])

    def is_black(self, x, y, z):
        key = self.get_tile_key(x, y, z)
        if self.hm.get(key) and not self.hm.get(key).white:
            return True
        return False

    def get_tiles_ring(self, radius):
        if radius == 0:
            return [[0, 0, 0]]
        ps = permutations(range(-radius, radius+1), 3)
        tiles_ring = [[p[0], p[1], p[2]] for p in ps if sum(p) == 0 and sum(abs(x) for x in p) == radius*2]

        return tiles_ring

    def get_adj_tiles_coords(self, x, y, z):
        return [[x + p[0], y + p[1], z + p[2]] for p in self.get_tiles_ring(1)]

    def get_adj_tiles_black_count(self, x, y, z):
        bcount = 0
        for x_probe, y_probe, z_probe in self.get_adj_tiles_coords(x, y, z):
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
        # print(count)

    def do_art(self):
        max_r = self.get_max_radius()
        print('max_r: ', max_r)
        check_count = 0
        for r in range(max_r + 2):
            ring_tiles = self.get_tiles_ring(r)
            for x, y, z in ring_tiles:
                check_count += 1
                bcount = self.get_adj_tiles_black_count(x, y, z)
                is_white = not self.is_black(x, y, z)
                flip = self.should_flip(is_white, bcount)
                if flip:
                    flip = self.get_tile_if_exists(Tile(x, y, z))
                    flip.will_flip = True
        print('check_count:', check_count)
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
    for i in range(100):
        floor.do_art()
        print('Day ', i+1, ': ', floor.get_black_count())
    return floor.get_black_count()

# 464 too low.
# 12412 too high.


if __name__ == '__main__':
    DAY = 24
    input_data = get_input(DAY, True)
    p1_floor = part1(input_data)
    print(p1_floor.get_black_count())
    print(part2(p1_floor))
