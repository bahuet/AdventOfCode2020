import os.path


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        return [list(line) for line in f.read().splitlines()]


def get_next_state():
    pass


def part1(data):
    print(data)


def part2(data):
    pass


if __name__ == '__main__':
    DAY = 17
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
