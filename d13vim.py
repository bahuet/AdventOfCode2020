with open('inputs/13.txt') as f:
    d = (int(f.readline()), tuple(map(lambda x: int(x) if x.isdigit() else x, f.readline().strip().split(','))))
buses = tuple(b for b in d[1] if isinstance(b,int))
best = float('inf') 
bestid = None
for bid in buses:
    mod = bid - d[0]%bid
    if  mod < best:
        best, bestid = mod, bid
print(best*bestid)
