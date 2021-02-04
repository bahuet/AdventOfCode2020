from itertools import count
with open('inputs/3.txt') as f:
    d = f.read().splitlines()
height = len(d)
width = len(d[0])
trees = 0
for row, col in zip(range(height), count(0,3)):
    if d[row][col % width] == '#':
        trees += 1
print(trees)
slopes = ((1, 1), (1, 5), (1, 7), (2, 1))
total = trees
for down, right in slopes:
    trees = 0
    for row, col in zip(range(0, height, down), count(0,right)):
        if d[row][col%width] == '#':
            trees +=1
    total *= trees
print(total)
