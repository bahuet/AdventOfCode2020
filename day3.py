
import os.path
from functools import reduce


def get_input():
    input_path = os.path.join('inputs', 'day3-input.txt')
    f = open(input_path, 'r')
    data = f.read().split('\n')
    data.pop()
    return data


def part1(data):
    tree_count = 0
    x = 0
    for line in data:
        if line[x] == '#':
            tree_count += 1
        x = (x + 3) % len(line)
    return tree_count


def part2(data):
    # lets do it in one scan for fun
    slopes_data = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    slopes = [{"right": s[0], "down": s[1], 'x': 0, 'tree_count': 0} for s in slopes_data]
    y = 0

    for line in data:
        for slope in slopes:
            if y % slope["down"] == 0:
                if line[slope['x']] == '#':
                    slope['tree_count'] += 1
                slope['x'] = (slope['x'] + slope['right']) % len(line)
        y += 1
    return reduce((lambda x, y: x * y), [slope['tree_count'] for slope in slopes])

if __name__ == '__main__':
    input_data = get_input()
    print(part1(input_data))
    print(part2(input_data))
