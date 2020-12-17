import os.path
import re


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read().splitlines()
        return lines


def parse(line):
    regex = r'(?:(mem)\[(\d+)\] = (\d+))|(?:mask = (\w+))'
    match = re.match(regex, line)
    result = None
    if match[1] == 'mem':
        result = {
            'type': 'mem',
            'address': int(match[2]),
            'value': int(match[3])
        }
    else:
        result = {
            'type': 'mask',
            'mask': match[4]
        }
    return result


def apply_mask(number, mask):
    number_bin = f'{bin(number)[2:]:0>36}'
    new_number_bin_list = []
    for i, bit in enumerate(number_bin):
        if mask[i] in '01':
            current_bit = mask[i]
        else:
            current_bit = bit
        new_number_bin_list.append(current_bit)
    new_number_int = int(''.join(new_number_bin_list), 2)
    return new_number_int


def part1(data):
    memory = {}
    current_mask = ''
    for d in data:
        parsed_data = parse(d)
        if parsed_data['type'] == 'mem':
            new_value = apply_mask(parsed_data['value'], current_mask)
            memory[parsed_data['address']] = new_value
        else:
            current_mask = parsed_data['mask']
    return sum(memory.values())


def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input(14, False)
    print(part1(input_data))
    print(part2(input_data))
