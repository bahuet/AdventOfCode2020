import re

import os.path


def get_input():
    input_path = os.path.join('inputs', 'day2-input.txt')
    f = open(input_path, 'r')
    data = f.read().split('\n')
    data.pop()
    return data


def part1():
    data = get_input()
    regex = r'^(\d+)-(\d+)\s(\w):\s(\w+)$'
    valid_count = 0
    for word in data:
        match = re.search(regex, word)
        lower_bound = int(match.group(1))
        upper_bound = int(match.group(2))
        char = match.group(3)
        passwd = match.group(4)
        char_count = passwd.count(char)
        if char_count >= lower_bound and char_count <= upper_bound:
            valid_count += 1
    return valid_count


def part2():
    data = get_input()
    valid_count = 0
    for word in data:
        regex = r'^(\d+)-(\d+)\s(\w):\s(\w+)$'
        match = re.search(regex, word)
        first_index = int(match.group(1)) - 1
        second_index = int(match.group(2)) - 1
        char = match.group(3)
        passwd = match.group(4)
        flag = False
        if len(passwd) > first_index and passwd[first_index] == char:
            flag = True
        if len(passwd) > second_index and passwd[second_index] == char:
            flag = not flag
        if flag:
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    print(part1())
    print(part2())
