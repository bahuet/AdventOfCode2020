import os.path


def get_input():
    input_path = os.path.join('inputs', 'day5-input.txt')
    f = open(input_path, 'r')
    data = f.read().split('\n')
    data.pop()
    return data


def part1(data):
    pass


def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input()
    print(part1(input_data))
    print(part2(input_data))
