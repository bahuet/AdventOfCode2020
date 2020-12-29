import os.path
import re


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        rules, messages = f.read().split('\n\n')
        return rules.splitlines(), messages.splitlines()


def parse_rules(rules_data):
    rules = {}
    for line in rules_data:
        ruleid, options = line.split(': ')
        ruleid = int(ruleid)

        if '"' in options:
            rule = options[1: -1]
        else:
            rule = []
            for option in options.split(' | '):
                rule.append(tuple(map(int, option.split())))
        rules[ruleid] = rule
    return rules


def build_regexep(rules, rulenum=0):
    rule = rules[rulenum]
    if isinstance(rule, str):
        return rule
    options = []
    for opt_tuble in rule:
        opt_str = ''
        for sub_rule in opt_tuble:
            opt_str += build_regexep(rules, sub_rule)
        options.append(opt_str)
    return '(' + '|'.join(options) + ')'


def part1(rules_data, messages):
    rules = parse_rules(rules_data)
    reg = re.compile('^' + build_regexep(rules) + '$')
    valid = 0
    for msg in messages:
        if reg.match(msg):
            valid += 1
    return valid


def part2(rules_data, messages_data):
    pass


if __name__ == '__main__':
    DAY = 19
    rules_lines, messages_lines = get_input(DAY, False)
    print(part1(rules_lines, messages_lines))
    print(part2(rules_lines, messages_lines))
