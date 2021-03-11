LEFT, RIGHT, FORWARD = 'LRF'
NORTH, SOUTH, EAST, WEST = 'NSEW'
with open('inputs/12.txt') as f:
    d = tuple(map(lambda x: (x[0], int(x[1:])), f.read().splitlines()))
ROTMAN = {
    (LEFT, 90): lambda x, y: (-y, x),
    (LEFT, 180): lambda x, y: (-x, -y),
    (LEFT, 270): lambda x, y: (y, -x),
    (RIGHT, 90): lambda x, y: (y, -x),
    (RIGHT, 180): lambda x, y: (-x, -y),
    (RIGHT, 270): lambda x, y: (-y, x)
    }
MOVEMAP = {
        NORTH: lambda x, y, n: (x, y + n),
        SOUTH: lambda x, y, n: (x, y - n),
        EAST: lambda x, y, n: (x + n, y),
        WEST: lambda x, y, n: (x - n, y)
    }
x, y = 0, 0
dx, dy = 1, 0
for cmd, n in d:
    if cmd == FORWARD:
        x += dx * n
        y += dy * n
    elif cmd == LEFT or cmd == RIGHT:
        dx, dy = ROTMAN[(cmd, n)](dx, dy)
    else:
        x, y = MOVEMAP[cmd](x, y, n)
print(abs(x) + abs(y))

x, y = 0, 0
dx, dy = 10, 1 
for cmd, n in d:
    if cmd == FORWARD:
        x += dx * n
        y += dy * n
    elif cmd == LEFT or cmd == RIGHT:
        dx, dy = ROTMAN[(cmd, n)](dx, dy)
    else:
        dx, dy = MOVEMAP[cmd](dx, dy, n)
print(abs(x) + abs(y))
