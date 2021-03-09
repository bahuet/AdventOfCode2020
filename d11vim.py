from copy import deepcopy
OCCUPIED, EMPTY, FLOOR = '#L.'
with open('inputs/11.txt') as f:
    og = list(map(list, (map(str.rstrip, f.readlines()))))
MAXROW, MAXCOL = len(og) - 1, len(og[0]) - 1
def occupied_neighbors(grid, r, c, sight ):
    total = 0
    for y in range(-1,2):
        for x in range(-1,2):
            if y == x == 0:
                continue
            rr, cc = r+y, c+x

            if sight:
                while 0 <= rr <= MAXROW and 0 <= cc <= MAXCOL:
                    if grid[rr][cc] != FLOOR:
                        if grid[rr][cc] == OCCUPIED:
                            total += 1
                        break
                    rr += y
                    cc += x
            else:
                if 0 <= rr <= MAXROW and 0 <= cc <= MAXCOL:
                    total += grid[rr][cc] == OCCUPIED
    return total
def evolve(grid, occ_counter, occ_threshold):
    while 1:        
        previous = deepcopy(grid)
        for r, row in enumerate(previous):
            for c, cell in enumerate(row):
                if cell == FLOOR:
                    continue
                occ = occ_counter(previous, r, c)
                if cell == EMPTY and occ == 0:
                    grid[r][c] = OCCUPIED
                elif cell == OCCUPIED and occ >= occ_threshold:
                    grid[r][c] = EMPTY
        if grid == previous:
            return sum(row.count(OCCUPIED) for row in grid)
def counter1(a,b,c):
    return occupied_neighbors(a,b,c,False)
def counter2(a,b,c):
    return occupied_neighbors(a,b,c,True)
print(evolve(deepcopy(og), counter1, 4))
print(evolve(deepcopy(og), counter2, 5))
