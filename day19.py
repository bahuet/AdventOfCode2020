import os.path
import re


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        rules, messages = f.read().split('\n\n')
        return rules.splitlines(), messages.splitlines()


def parse_rules(rules_raw):
    rules = {}
    rule_num_reg = r'^(\d+):\s(.+)'
    char_reg = '"([a-zA-Z])"'
    two_rules_reg = r'(\d+)\s(\d+)'
    rules_set = two_rules_reg + '(?:' + r'\s\|\s' + two_rules_reg + ')?'
    for rule_raw in rules_raw:
        match = re.search(rule_num_reg, rule_raw)
        num = int(match[1])
        rules[num] = {}
        letter_match = re.search(char_reg, match[2])
        value_match = re.search(rules_set, match[2])
        if letter_match:
            rules[num]['type'] = 'val'
            rules[num]['data'] = letter_match[1]
        elif value_match:
            rules[num]['type'] = 'ref'
            rules[num]['data'] = [[value_match[1], value_match[2]]]
            if value_match[3]:
                second_list = [value_match[3]]
                if value_match[4]:
                    second_list.append(value_match[4])
                rules[num]['data'].append(second_list)
    return rules


def part1(rules_data, messages):
    rules = parse_rules(rules_data)
    print('123')


def part2(rules_data, messages_data):
    pass


if __name__ == '__main__':
    DAY = 19
    rules_lines, messages_lines = get_input(DAY, False)
    print(part1(rules_lines, messages_lines))
    print(part2(rules_lines, messages_lines))
