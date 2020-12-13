import os.path
from time import sleep


def get_input(day):
    input_path = os.path.join('inputs', str(day)+'.txt')
    with open(input_path) as f:
        data = [list(x) for x in f.read().splitlines()]
        return data


def get_adjacents(x, y, seats):
    adj = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i < 0 or j < 0 or (i == y and j == x):
                continue
            try:
                adj.append(seats[i][j])
            except:
                pass
    return ''.join(adj)


def apply_rules(seats):
    newseats = []
    for y in range(len(seats)):
        newseats.append([])
        for x in range(len(seats[y])):
            adjacents = get_adjacents(x, y, seats)
            if seats[y][x] == 'L' and adjacents.count('#') == 0:
                elt = '#'
            elif seats[y][x] == '#' and adjacents.count('#') >= 4:
                elt = 'L'
            else:
                elt = seats[y][x]
            newseats[y].append(elt)
    return newseats


def part1(data):
    counter = 0
    seats = data
    ogstring = ''
    newstring = ''.join([s for substr in seats for s in substr])

    while ogstring != newstring and counter < 100:
        ogstring = newstring
        newseats = apply_rules(seats)
        newstring = ''.join([s for substr in newseats for s in substr])
        counter += 1
        seats = newseats
    print(f'It took {counter} operations to reach stable position')
    return newstring.count('#')



def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input(11)
    print(part1(input_data))
    print(part2(input_data))
