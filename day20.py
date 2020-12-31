import os.path
import re


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


def part1(data):
    tiles = parse_input(data)
    return tiles


def part2(data):
    pass


if __name__ == '__main__':
    DAY = 20
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
