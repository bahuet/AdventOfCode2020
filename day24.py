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


DIRECTIONS = [
    (+1, -1, 0), (+1, 0, -1), (0, +1, -1),
    (-1, +1, 0), (-1, 0, +1), (0, -1, +1),
]


class Tile:
    """A tile represented with cube coordinates"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.white = True
        self.will_flip = False

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
        for cardinal_move in moves:
            self.cardinal_move(cardinal_move)

    def cardinal_move(self, cardinal_dir):
        self.move(self.translate_table[cardinal_dir])

    def move(self, index):
        move_values = DIRECTIONS[index]
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

    def get_tile_neighbor(self, tile_coords, direction):
        move_vals = DIRECTIONS[direction]
        return tuple(tile_coords[i]+move_vals[i] for i in range(3))

    def get_tiles_ring(self, radius):
        if radius == 0:
            return [(0, 0, 0)]
        tiles_ring = []
        tile_coords = (-radius, 0, radius)  # this is the starting position that works with the order of directions
        for i in range(6):
            for j in range(radius):
                tiles_ring.append(tile_coords)
                tile_coords = self.get_tile_neighbor(tile_coords, i)
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
        for tile in self.hm.values():
            if tile.will_flip:
                tile.flip_color()

    def do_art(self):
        max_r = self.get_max_radius()
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
    for i in range(10):
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
