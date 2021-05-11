from itertools import product
with open('inputs/17.txt') as f:
    d = set()
    for y, row in enumerate(f.readlines()):
        for x, cell in enumerate(row.rstrip()):
            if cell == '#':
                d.add((x,y,0))

def neighbors(x,y,z):
    yield from product(range(x-1,x+2), range(y-1,y+2), range(z-1,z+2))

def alive_neighbors(cube, coords):
    alive = sum(p in cube for p in neighbors(*coords)) 
    alive -= coords in cube
    return alive

def all_neighbors(cube):
    return set(n for p in cube for n in neighbors(*p))

def mutate(initial_cube):
    new_cube = set()
    for n in all_neighbors(initial_cube):
        alive_n = alive_neighbors(initial_cube, n)
        if (alive_n == 2 and n in initial_cube) or alive_n == 3:
            new_cube.add(n)
    return new_cube

cube = d
for _ in range(6):
    cube = mutate(cube)
print(len(cube))


        


