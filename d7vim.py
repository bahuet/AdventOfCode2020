import re
from collections import defaultdict 
d = open('inputs/7.txt').read().splitlines()
inner_exp = re.compile(r'(\d+) ([\w ]+) bags?[,.]')
contained_by = defaultdict(list)
for line in d:
    outer, inners = line.split(' bags contain ')
    inners = inner_exp.findall(inners)
    for _, inner in inners:
        contained_by[inner].append(outer)
def count_can_contain(G, src, visited=set()):
    for color in G[src]:
        visited.add(color)
        count_can_contain(G, color, visited)
    return len(visited)
print(count_can_contain(contained_by, 'shiny gold'))
