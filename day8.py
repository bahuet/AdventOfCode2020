import os.path
import re


def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
    f = open(input_path, 'r')
    data = [x for x in f.read().splitlines()]
    return data


def parse_data(data):
    # could have been parsed in get_input so we only scan once
    ins_list = []
    for entry in data:
        match = re.search(r'^(\w\w\w)\s([+-]\d+)$', entry)
        topush = {
            "com": match.group(1),
            "val": int(match.group(2))
        }
        ins_list.append(topush)
    return ins_list


def consume_instruction(ins, index, acc):
    if ins['com'] == 'nop':
        index += 1
    elif ins['com'] == 'acc':
        index += 1
        acc += ins['val']
    elif ins['com'] == 'jmp':
        index += ins['val']
    return index, acc


def part1(data):
    ins_list = parse_data(data)
    visited = set()
    index = 0
    acc = 0
    ins = ins_list[0]
    while True:
        visited.add(index)
        index, newacc = consume_instruction(ins, index, acc)
        if index in visited:
            break
        acc = newacc
        ins = ins_list[index]
    return acc


def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input(8)
    print(part1(input_data))
    print(part2(input_data))
