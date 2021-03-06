import os.path

def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read().splitlines()
        return lines


def part1(data):
    pass


def part2(data):
    pass


if __name__ == '__main__':
    DAY = 0
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
