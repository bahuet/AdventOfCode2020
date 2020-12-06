import os.path
from functools import reduce


def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
    f = open(input_path, 'r')
    data = [x.splitlines() for x in f.read().split('\n\n')]
    return data


def part1(data):
    agg_sum = 0
    for d in data:
        sets = [set(x) for x in d]
        union = reduce(lambda x, y: x | y, sets)
        agg_sum += len(union)
    return agg_sum


def part2(data):
    agg_sum = 0
    for d in data:
        sets = [set(x) for x in d]
        intersection = reduce(lambda x, y: x & y, sets)
        agg_sum += len(intersection)
    return agg_sum


if __name__ == '__main__':
    input_data = get_input(6)
    print(part1(input_data))
    print(part2(input_data))
