
import os.path


def get_input():
    input_path = os.path.join('inputs', 'day3-input.txt')
    f = open(input_path, 'r')
    data = f.read().split('\n')
    data.pop()
    return data


def part1():
    data = get_input()
    tree_count = 0
    x = 0
    for line in data:
        if line[x] == '#':
            tree_count += 1
        x = (x + 3) % len(line)
    return tree_count

def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
