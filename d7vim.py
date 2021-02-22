import re
from collections import defaultdict 
d = open('inputs/7.txt').read().splitlines()
inner_exp = re.compile(r'(\d+) ([\w ]+) bags?[,.]')
contained_by = defaultdict(list)
contains = defaultdict(list)
for line in d:
    outer, inners = line.split(' bags contain ')
    inners = inner_exp.findall(inners)
    for qty, inner in inners:
        contained_by[inner].append(outer)
        contains[outer].append((int(qty), inner))
def count_can_contain(G, src, visited=set()):
    for color in G[src]:
        visited.add(color)
        count_can_contain(G, color, visited)
    return len(visited)
print(count_can_contain(contained_by, 'shiny gold'))
def count_contained(G, src):
    t = 0
    for qty, color in G[src]:
        t += qty
        t += qty * count_contained(G, color)
    return t
print(count_contained(contains, 'shiny gold'))

