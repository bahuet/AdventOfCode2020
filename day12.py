import os.path
from time import sleep

enums = {'N': 0, 'E': 1, 'S': 2, 'W': 3}


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        data = [[x[0], int(x[1:])] for x in f.read().splitlines()]
        return data


def get_next_position(ins, coords):
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
    coords = [0, 0, 0, 0, enums['E']]  # N E S W direction
    for ins in data:
        get_next_position(ins, coords)
    return abs(coords[0]-coords[2]) + abs(coords[1]-coords[3])


def move_ship(dist, ship, wp):
    for i, n in enumerate(ship):
        ship[i] += dist*wp[i]


def rotate_waypoint(direction, angle, wp):
    rotations = int(angle / 90)
    # Sometimes My Genius... It's Almost Frightening
    for _ in range(rotations):
        if direction == 'L':
            a = wp.pop(0)
            wp.append(a)
        elif direction == 'R':
            a = wp.pop()
            wp.insert(0, a)


def consume_p2_instruction(ins, ship, wp):
    command = ins[0]
    value = ins[1]
    if command in 'LR':
        rotate_waypoint(command, value, wp)
    elif command == 'F':
        move_ship(value, ship, wp)
    else:
        wp[enums[command]] += value


def part2(data):
    waypoint_pos = [1, 10, 0, 0]  # N E S W
    ship_coords = [0, 0, 0, 0]
    for ins in data:
        consume_p2_instruction(ins, ship_coords, waypoint_pos)
    return abs(ship_coords[0]-ship_coords[2]) + abs(ship_coords[1]-ship_coords[3])


if __name__ == '__main__':
    input_data = get_input(12, False)
    print(part1(input_data))
    print(part2(input_data))
