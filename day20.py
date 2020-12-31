import os.path
import re
from functools import reduce


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        return f.read()


def parse_input(inputdata):
    tiles = {}
    for rawtile in inputdata.strip().split('\n\n'):
        tile_line = rawtile.split('\n')
        tileid = int(re.match('Tile (\d+):', tile_line[0])[1])
        tiles[tileid] = [list(line) for line in tile_line[1:]]
    return tiles


def build_tiles_sides_patterns(tiles):
    tiles_sides_patterns = {}
    for tileid, tile in tiles.items():
        top_pattern = right_pattern = left_pattern = bot_pattern = ''
        for i in range(len(tile)):
            top_pattern += tile[0][i]
            bot_pattern += tile[-1][-i-1]
            left_pattern += tile[-i-1][0]
            right_pattern += tile[i][-1]
        tiles_sides_patterns[tileid] = [top_pattern, bot_pattern, left_pattern, right_pattern]
    return tiles_sides_patterns


def get_pattern_numeric_value(pattern):
    num = 0
    for i, c in enumerate(pattern):
        if c == '#':
            num += 10**i
    return num


def get_pattern_universal_num_value(pattern):
    return min(get_pattern_numeric_value(pattern), get_pattern_numeric_value(pattern[::-1]))


def get_patterns_counter(tiles_sides_patterns):
    patterns_counter = {}
    for tile_patterns in tiles_sides_patterns.values():
        for pattern in tile_patterns:
            num_to_use = get_pattern_universal_num_value(pattern)
            patterns_counter[num_to_use] = patterns_counter[num_to_use] + 1 if patterns_counter.get(num_to_use) else 1
    return patterns_counter


def part1(data):
    tiles = parse_input(data)
    tiles_sides_patterns = build_tiles_sides_patterns(tiles)
    patterns_counter = get_patterns_counter(tiles_sides_patterns)
    tiles_with_2_unique_tiles = []
    for tileid, patterns in tiles_sides_patterns.items():
        counter = 0
        for pattern in patterns:
            if patterns_counter[get_pattern_universal_num_value(pattern)] == 1:
                counter += 1
        if counter == 2:
            tiles_with_2_unique_tiles.append(tileid)
    return reduce(lambda x, y: x*y, tiles_with_2_unique_tiles)


def part2(data):
    pass


if __name__ == '__main__':
    DAY = 20
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
