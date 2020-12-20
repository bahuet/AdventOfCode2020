import os.path
import re
from functools import reduce

def get_input(day, test=False, num=1):
    filename = str(day) + ('test' + str(num) if test else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read()
        return lines


def parse_data(lines):
    block_one, block_two, block_three = lines.split('\n\n')
    rules = {}

    for rule_line in block_one.strip().split('\n'):
        reg = r'^([\w\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$'
        match = re.search(reg, rule_line)
        rules[match[1]] = [[int(match[2]), int(match[3])], [int(match[4]), int(match[5])]]

    my_ticket = [int(x) for x in block_two.split('\n')[1].split(',')]

    nearby_tickets_lines = block_three.strip().split('\n')[1:]
    nearby_tickets = [list(map(int, nearby_tickets_line.split(','))) for nearby_tickets_line in nearby_tickets_lines]

    return rules, my_ticket, nearby_tickets


def value_is_within_scope(value, scope):
    if scope[0] <= value <= scope[1]:
        return True
    return False


def value_valid_for_rule(value, rulename, rules):
    return any([value_is_within_scope(value, scope) for scope in rules[rulename]])


def value_valid_for_atleast_one_rule(value, rules):
    return any([value_valid_for_rule(value, rulename, rules) for rulename in rules.keys()])


def get_tickets_invalid_values(ticket, rules):
    invalid_values = []
    for value in ticket:
        if not value_valid_for_atleast_one_rule(value, rules):
            invalid_values.append(value)
    return invalid_values


def part1(data):
    rules, _, all_tickets = data
    ticket_scanning_error_rate = 0

    for ticket in all_tickets:
        ticket_scanning_error_rate += sum(get_tickets_invalid_values(ticket, rules))
    return ticket_scanning_error_rate


def get_invalid_rules_for_value(value, rules):
    invalid_rules = []
    for rulename in rules.keys():
        if not value_valid_for_rule(value, rulename, rules):
            invalid_rules.append(rulename)
    return invalid_rules


def apply_hashmap_filter(colindex, invalid_rules, hm):
    columns_found = set()
    for invalid_rule in invalid_rules:
        try:
            hm[invalid_rule].remove(colindex)
            if len(hm[invalid_rule]) == 1:
                columns_found.add(list(hm[invalid_rule])[0])
        except:
            pass

    return columns_found



def clean_hm(columns_found_set, rules, hm):
    new_columns_found_set = set()
    for rule in rules:
        if len(hm[rule]) > 1:
            try:
                hm[rule] = hm[rule] - columns_found_set
                if len(hm[rule]) == 1:
                    new_columns_found_set.add(list(hm[rule])[0])
            except:
                pass
    if new_columns_found_set:
        clean_hm(new_columns_found_set, rules, hm)


def part2(data):
    rules, my_ticket, all_tickets = data
    rules_possible_col_indexes = {}
    for rulename in rules.keys():
        rules_possible_col_indexes[rulename] = set(range(len(my_ticket)))
    for ticket in all_tickets:
        if get_tickets_invalid_values(ticket, rules):
            continue
        for colindex, value in enumerate(ticket):
            invalid_rules = get_invalid_rules_for_value(value, rules)
            if invalid_rules:
                columns_found = apply_hashmap_filter(colindex, invalid_rules, rules_possible_col_indexes)
                if columns_found:
                    clean_hm(columns_found, rules, rules_possible_col_indexes)
        # stop when all rules found their columns
        if sum([len(colset) for colset in rules_possible_col_indexes.values()]) == len(my_ticket):
            break
    vals_to_multiply = [my_ticket[col.pop()] for (rulename, col) in rules_possible_col_indexes.items() if 'departure' in rulename]
    return reduce(lambda a,b: a *b, vals_to_multiply)

if __name__ == '__main__':
    DAY = 16
    input_data = get_input(DAY, False, 2)
    parsed_data = parse_data(input_data)
    # print(part1(parsed_data))
    print(part2(parsed_data))
