import re
import os.path
#REQ_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
REQ_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def get_input():
    input_path = os.path.join('inputs', 'day4-input.txt')
    f = open(input_path, 'r')
    data = f.read().split('\n\n')
    return data


def extract_passport_values(string):
    fields_dict = {field: None for field in REQ_FIELDS}
    for field in fields_dict:
        regex = field + r':([#\w\d]+)'
        match = re.search(regex, string)
        try:
            fields_dict[field] = match.group(1)
        except (IndexError, AttributeError):
            pass
    return fields_dict


def check_passport_validity(passport_values):
    for field in REQ_FIELDS:
        if passport_values[field] is None:
            return False
    return True


def part1(passports):
    valid_passports_count = 0
    for passport in passports:
        passport_values = extract_passport_values(passport)
        if check_passport_validity(passport_values):
            valid_passports_count += 1
    return valid_passports_count


def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input()
    print(part1(input_data))
    print(part2(input_data))
