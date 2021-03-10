LEFT, RIGHT, FORWARD = 'LRF'
NORTH, SOUTH, EAST, WEST = 'NSEW'
with open('inputs/12.txt') as f:
    d = tuple(map(lambda x: (x[0], int(x[1:])), f.read().splitlines()))

print(d)
