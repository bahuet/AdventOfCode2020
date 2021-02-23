import re
from functools import lru_cache
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
@lru_cache(maxsize=None)
def count_contained(src):
    t = 0
    for qty, color in contains[src]:
        t += qty * (1 +  count_contained(color))
    return t
print(count_contained('shiny gold'))

