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

