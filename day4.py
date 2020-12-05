import re
import os.path
#REQ_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
REQ_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
FIELDS_REGEX_RULES = {
    "byr": '19[2-9][0-9]|200[0-2]',
    "iyr": r'201\d|2020',
    "eyr": r'202\d|2030',
    "hgt": '^(?:(?:1[5-8][0-9]|19[0-3])cm)$|^(?:(?:59|6[0-9]|7[0-6])in)$',
    "hcl": '^#[a-f0-9]{6}$',
    "ecl": 'amb|blu|brn|gry|grn|hzl|oth',
    "pid": r'^\d{9}$'
}


def get_input():
    input_path = os.path.join('inputs', '4.txt')
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
            fields_dict[field] = None
    return fields_dict


def check_passport_info_complete(passport_values):
    for field in REQ_FIELDS:
        if passport_values[field] is None:
            return False
    return True


def check_passport_info_valid(passport_values):
    for field in REQ_FIELDS:
        regex = FIELDS_REGEX_RULES[field]
        if not re.search(regex, passport_values[field]):
            return False
    return True


def part1(passports):
    complete_passport_count = 0
    for passport in passports:
        passport_values = extract_passport_values(passport)
        if check_passport_info_complete(passport_values):
            complete_passport_count += 1
    return complete_passport_count

def part2(passports):
    valid_passport_count = 0
    for passport in passports:
        passport_values = extract_passport_values(passport)
        if check_passport_info_complete(passport_values) and check_passport_info_valid(passport_values):
            valid_passport_count += 1
    return valid_passport_count


if __name__ == '__main__':
    input_data = get_input()
    print(part1(input_data))
    print(part2(input_data))
