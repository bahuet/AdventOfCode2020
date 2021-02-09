with open('inputs/5.txt') as f:
    table = str.maketrans('BFRL', '1010')
    d = f.read().translate(table).splitlines()
ids = tuple(map(lambda x: int(x,2), d))
maxid = max(ids)
print(maxid)
minid = min(ids)
expected = maxid * (maxid + 1) // 2 - minid * (minid -  1) // 2
missing = expected - sum(ids)  
print(missing)

