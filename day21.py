import os.path
import re


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read().splitlines()
        return lines


def parse_input(data):
    output = []
    regex = r'^(.+) \(contains (.+)\)$'
    for line in data:
        match = re.match(regex, line)
        output.append({'ingredients': match[1].split(' '),
                       'allergens': match[2].split(', ')})
    return output


def get_possible_matches(data):
    matches = {}
    for entry in data:
        for allergen_name in entry['allergens']:
            matches[allergen_name] = matches[allergen_name] & set(
                entry['ingredients']) if matches.get(allergen_name) else set(
                entry['ingredients'])
    return matches


def part1(data):
    m = get_possible_matches(data)
    all_allergens_ing = set()
    for d in m.values():
        all_allergens_ing = all_allergens_ing | d
    counter = 0
    for entry in data:
        counter += len([ing for ing in entry['ingredients'] if ing not in all_allergens_ing])
    return counter


def remove_ing_from_matches(ing, m):
    for k, v in m.items():
        if ing in v:
            v.remove(ing)


def part2(data):
    m = get_possible_matches(data)
    all_to_ing = {}
    while len(m) > 0:
        for k, v in m.items():
            if len(v) == 1:
                ing = v.pop()
                all_to_ing[k] = ing
                if ing:
                    remove_ing_from_matches(ing, m)
        m = {k: v for k, v in m.items() if len(v) > 0}
    als = sorted(list(all_to_ing.keys()))
    return ','.join([all_to_ing[al] for al in als])


if __name__ == '__main__':
    DAY = 21
    input_data = get_input(DAY, False)
    parsed_data = parse_input(input_data)
    print(part1(parsed_data))
    print(part2(parsed_data))
