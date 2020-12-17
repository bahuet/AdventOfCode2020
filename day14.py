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


def int_to_36bin(num):
    return f'{bin(num)[2:]:0>36}'


def apply_mask_to_value(value, mask):
    value_bin = int_to_36bin(value)
    new_value_bin_list = []
    for i, bit in enumerate(value_bin):
        if mask[i] in '01':
            current_bit = mask[i]
        else:
            current_bit = bit
        new_value_bin_list.append(current_bit)
    new_number_int = int(''.join(new_value_bin_list), 2)
    return new_number_int


def part1(data):
    memory = {}
    current_mask = ''
    for d in data:
        parsed_data = parse(d)
        if parsed_data['type'] == 'mem':
            new_value = apply_mask_to_value(parsed_data['value'], current_mask)
            memory[parsed_data['address']] = new_value
        else:
            current_mask = parsed_data['mask']
    return sum(memory.values())


def compute_floatings(address_bin, computed_list):  # ??
    X_index = address_bin.find('X')
    if X_index == -1:
        computed_list.append(address_bin)
    else:
        zero_address = address_bin[:X_index] + '0' + address_bin[X_index + 1:]
        one_address = address_bin[:X_index] + '1' + address_bin[X_index + 1:]
        compute_floatings(zero_address, computed_list)
        compute_floatings(one_address, computed_list)


def apply_mask_to_address(address_int, mask):
    adress_bin = int_to_36bin(address_int)
    new_address_bin_list = []
    for i, bit in enumerate(adress_bin):
        if mask[i] in '1X':
            current_bit = mask[i]
        else:
            current_bit = bit
        new_address_bin_list.append(current_bit)
    addresses_bin_list = []
    compute_floatings(''.join(new_address_bin_list), addresses_bin_list)
    return [int(address, 2) for address in addresses_bin_list]


def part2(data):
    memory = {}
    current_mask = ''
    for d in data:
        parsed_data = parse(d)
        if parsed_data['type'] == 'mem':
            addresses = apply_mask_to_address(parsed_data['address'], current_mask)
            for address in addresses:
                memory[address] = parsed_data['value']
        else:
            current_mask = parsed_data['mask']
    return sum(memory.values())


# 24754394106 too low
# 26668152560 too low
if __name__ == '__main__':
    input_data = get_input(14, False)
    print(part1(input_data))
    print(part2(input_data))
