with open('inputs/1.txt') as f:
    d = tuple(map(int, f.read().splitlines()))
#p1
comps = set()
for x in d:
    y = 2020 - x
    if x in comps:
        print(x*y)
        break
    else:
        comps.add(y)
#p2
for xi, x in enumerate(d):
    comps2 = set()
    target = 2020 - x
    for yi in range(xi+1, len(d)):
        y = d[yi]
        z = target - y
        if z in comps2:
            print(x * y * z)
            break
        comps2.add(y)
