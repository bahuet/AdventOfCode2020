with open('inputs/1.txt') as f:
    d = tuple(map(int, f.read().splitlines()))
#p1
comps = set()
for x in d:
    y = 2020 -x
    if x in comps:
        print(x*y)
        break
    else:
        comps.add(y)
