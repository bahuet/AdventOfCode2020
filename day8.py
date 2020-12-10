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


def backwards_travel(index, index_paths, branch, visited):
    visited.add(index)
    source_ins_list = index_paths.get(index)
    if not source_ins_list:
        return
    for i, source_ins in enumerate(source_ins_list):
        backwards_travel(source_ins['index'], index_paths, branch + i, visited)


def part2(data):
    ins_list = parse_data(data)
    index_paths = {}
    alt_index_paths = {}
    for i, ins in enumerate(ins_list):
        if ins['com'] == 'nop':
            next_index = i + 1
            alt_next_index = i + ins['val']
        elif ins['com'] == 'acc':
            next_index = i + 1
            alt_next_index = i + 1
        elif ins['com'] == 'jmp':
            next_index = i + ins['val']
            alt_next_index = i + 1

        ins['index'] = i
        index_paths[next_index] = index_paths.get(next_index) + [ins] if index_paths.get(next_index) else [ins]
        alt_index_paths[alt_next_index] = alt_index_paths.get(
            alt_next_index) + [ins] if alt_index_paths.get(alt_next_index) else [ins]

    dead_ends = set()
    backwards_travel(656, index_paths, 0, dead_ends)
    possible_solutions = []
    for d in dead_ends:
        if alt_index_paths.get(d):
            # print(len(alt_index_paths.get(d)))
            indexes = [ins['index'] for ins in alt_index_paths[d]]
            possible_solutions.extend(indexes)
    visited = set()
    index = 0
    acc = 0
    ins = ins_list[0]
    flipped = False
    while True:
        visited.add(index)
        if index == len(ins_list) - 1:
            print(f'final acc at index:{index}: {acc}')
            return acc
        if index in possible_solutions and not flipped:
            print(f'{ins["com"]} instruction flipped at {index}')
            if ins['com'] == 'nop':
                index += ins['val']
            elif ins['com'] == 'jmp':
                index += 1
            flipped = True
        else:
            index, newacc = consume_instruction(ins, index, acc)
        if index in visited:
            print('breaking out of loop')
            break
        acc = newacc
        ins = ins_list[index]

if __name__ == '__main__':
    input_data = get_input(8)
    # print(part1(input_data))
    print(part2(input_data))
