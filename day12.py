import os.path
from time import sleep


def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
    with open(input_path) as f:
        data = [[x[0], int(x[1:])] for x in f.read().splitlines()]
        return data


def get_next_position(ins, coords, enums):
    command = ins[0]
    value = ins[1]
    if command in 'LR':
        sign = -1 if command == 'L' else 1
        coords[4] = int((coords[4] + (value * sign) / 90) % 4)
    elif command == 'F':
        coords[coords[4]] += value
    else:
        coords[enums[command]] += value


def part1(data):
    enums = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    coords = [0, 0, 0, 0, enums['E']]  # N E S W direction
    for ins in data:
        get_next_position(ins, coords, enums)
    return abs(coords[0]-coords[2]) + abs(coords[1]-coords[3])


def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input(12)
    print(part1(input_data))
    print(part2(input_data))
