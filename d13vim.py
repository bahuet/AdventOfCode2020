with open('inputs/13.txt') as f:
    d = (int(f.readline()), tuple(map(lambda x: int(x) if x.isdigit() else x, f.readline().strip().split(','))))
buses = tuple(b for b in d[1] if isinstance(b,int))
best = float('inf') 
bestid = None
for bid in buses:
    mod = bid - d[0]%bid
    if mod < best:
        best, bestid = mod, bid
print(best*bestid)
from itertools import count
from math import gcd
buses2 = tuple((i,b) for (i,b) in enumerate(d[1]) if isinstance(b,int))
t, step = buses2[0]
for delta, period in buses2[1:]:
    for t in count(t, step):
        if (t+delta) % period == 0:
            break
    step = step * period // gcd(step, period)
print(t)
