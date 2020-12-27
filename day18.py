import os.path
from functools import reduce


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read().splitlines()
        return lines


def push(item, destination_list, depth):
    while depth != 0:
        destination_list = destination_list[-1]
        depth -= 1
    destination_list.append(item)


def parse_line(line):
    result = []
    depth = 0
    try:
        for c in line:
            if c == ' ':
                continue
            elif c == '(':
                push([], result, depth)
                depth += 1
            elif c == ')':
                depth -= 1
            else:
                push(int(c) if c.isdigit() else c, result, depth)
    except IndexError:
        raise ValueError('Parenthese mismatch')
    if depth > 0:
        raise ValueError('Parenthese mismatch')
    return result


def op(operator, a, b):
    if operator == '+':
        return a + b
    if operator == '*':
        return a * b


def get_expression_result(expression):
    curr_value = 0
    current_operation = None
    for item in expression:
        if isinstance(item, list):
            item = get_expression_result(item)
        if isinstance(item, int):
            # compute new value by consuming the operation
            if current_operation:
                curr_value = op(current_operation, curr_value, item)
                current_operation = None
            else:
                # First number in the line
                curr_value = item
        elif item in '+*':
            current_operation = item
    return curr_value


def part1(data):
    acc = 0
    for line in data:
        acc += get_expression_result(parse_line(line))
    return acc


def get_expression_result_addfirst(expression):
    new_expression = []

    loaded_num = 0
    has_loaded_add = False
    for item in expression:
        if isinstance(item, list):
            item = get_expression_result_addfirst(item)
        if isinstance(item, int):
            if loaded_num and has_loaded_add:
                loaded_num += item
                has_loaded_add = False
            else:
                loaded_num = item
        elif item == '*':
            new_expression.append(loaded_num)
            has_loaded_add = False
        elif item == '+':
            has_loaded_add = True
    if loaded_num:
        new_expression.append(loaded_num)
    return reduce((lambda a, b: a * b), new_expression)


def part2(data):
    acc = 0
    for line in data:
        acc += get_expression_result_addfirst(parse_line(line))
    return acc


if __name__ == '__main__':
    DAY = 18
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
