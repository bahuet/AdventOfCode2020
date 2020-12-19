import os.path
import io
import re


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read()
        return lines


def parse_data(lines):
    block_one, block_two, block_three = lines.split('\n\n')
    rules = {}

    for rule_line in block_one.strip().split('\n'):
        reg = r'^([\w\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$'
        match = re.search(reg, rule_line)
        rules[match[1]] = [[int(match[2]), int(match[3])], [int(match[4]), int(match[5])]]

    my_ticket = [int(x) for x in block_two.split('\n')[1].split(',')]

    nearby_tickets_lines = block_three.strip().split('\n')[1:]
    nearby_tickets = [list(map(int, nearby_tickets_line.split(','))) for nearby_tickets_line in nearby_tickets_lines]

    return rules, my_ticket, nearby_tickets


def part1(data):
    pass


def part2(data):
    pass


if __name__ == '__main__':
    DAY = 16
    input_data = get_input(DAY, False)
    data = parse_data(input_data)
    print(part1(data))
    print(part2(data))
