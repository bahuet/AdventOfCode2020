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
