import os.path
import re


def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
    f = open(input_path, 'r')
    data = [x for x in f.read().splitlines()]
    return data


def parse_bag_rules(bag_rules):
    ''' returns a dict with key = bag et value = list of bags it can contains'''

    main_bag_regex = r'^([\w\s]+) bags contain'
    sub_bags_regex = r'(\d) ([\w\s]+) bags?.|,'
    bag_rules_dict = {}

    for bag_rule in bag_rules:
        main_bag_match = re.match(main_bag_regex, bag_rule)
        if not main_bag_match:
            continue
        main_bag = main_bag_match.group(1)
        sub_bags = re.findall(sub_bags_regex, bag_rule)
        bag_rules_dict[main_bag] = sub_bags
    return bag_rules_dict


def get_bags_containers(bags_rules, bag):
    containers = set()
    for bag, subbags in bags_rules.items():
        subbags_set = set([subbag[1] for subbag in subbags])
        if bag in subbags_set:
            containers.add(bag)
    return containers


def part1(data):
    bags = parse_bag_rules(data)
    containers = set()
    queue = set(['shiny gold'])
    counter = 0
    while len(queue) > 0:
        newqueue = set()
        for bag, subbags in bags.items():
            # subbags_set is the set of bags that this bag can carry
            subbags_set = set([subbag[1] for subbag in subbags])
            # Some bags are in
            if len(queue & subbags_set) > 0:
                newqueue.add(bag)
        containers |= newqueue
        queue = newqueue
    return len(containers )



def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input(7)
    print(part1(input_data))
    print(part2(input_data))
