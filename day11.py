import os.path
from time import sleep


def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
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


def count_visible_occupied_seats(x, y, seats):
    truth_dict = {11: False}
    offset = 1
    while len(truth_dict) < 9:
        for oy_i, offsetted_y in enumerate([y-offset, y, y+offset]):
            for ox_i, offsetted_x in enumerate([x-offset, x, x+offset]):
                out_of_bounds = offsetted_y < 0 or offsetted_x < 0 or offsetted_y > len(
                    seats) - 1 or offsetted_x > len(seats[0]) - 1
                if truth_dict.get(oy_i*10+ox_i) is not None:
                    continue
                elif out_of_bounds or seats[offsetted_y][offsetted_x] == 'L':
                    truth_dict[oy_i*10+ox_i] = False
                elif seats[offsetted_y][offsetted_x] == '#':
                    truth_dict[oy_i*10+ox_i] = True
        offset += 1
    return sum(v == True for v in truth_dict.values())


def apply_new_rules(seats):
    # lots of repeated reads here, but in O(1).
    newseats = []
    for y in range(len(seats)):
        newseats.append([])
        for x in range(len(seats[y])):
            occupied_count = count_visible_occupied_seats(x, y, seats)
            if seats[y][x] == 'L' and occupied_count == 0:
                elt = '#'
            elif seats[y][x] == '#' and occupied_count >= 5:
                elt = 'L'
            else:
                elt = seats[y][x]
            newseats[y].append(elt)
    return newseats


def part2(data):
    counter = 0
    seats = data
    ogstring = ''
    newstring = ''.join([s for substr in seats for s in substr])

    while ogstring != newstring and counter < 100:
        ogstring = newstring
        newseats = apply_new_rules(seats)
        newstring = ''.join([s for substr in newseats for s in substr])
        counter += 1
        seats = newseats
    print(f'It took {counter} operations to reach stable position')
    return newstring.count('#')
# 7417 too high


if __name__ == '__main__':
    input_data = get_input(11)
    # print(part1(input_data))
    print(part2(input_data))
