with open('inputs/6.txt') as f:
    raw_groups = tuple(x.splitlines() for x in f.read().strip().split('\n\n'))
groups = tuple(map(lambda g:tuple(map(set,g)),raw_groups))
print(sum(len(set.union(*g)) for g in groups))
print(sum(len(set.intersection(*g)) for g in groups))
