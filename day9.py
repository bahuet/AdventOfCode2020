import os.path

def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
    with open(input_path) as f:
        data = [int(x) for x in f.read().splitlines()]
        return data


def check_validity(index, nb, data):
    pool = set(data[index - nb: index])
    target = data[index]
    for swimmer in pool:
        pool.remove(swimmer)
        candidate = target - swimmer
        if candidate in pool:
            return candidate
        else:
            pool.add(swimmer)
    return None


def part1(data):
    valid = True
    index = 24
    while valid:
        index += 1
        valid = check_validity(index, 25, data)
    return data[index]


def part2(data):
    target = part1(data)
    pool = []
    avant_garde = -1
    arriere_garde = -1
    sumpool = 0
    while sumpool != target:
        if sumpool < target:
            avant_garde += 1
            head = data[avant_garde]
            pool.append(head)
            sumpool += head
        elif sumpool > target:
            arriere_garde += 1
            tail = data[arriere_garde]
            pool.remove(tail)
            sumpool -= tail
    return max(pool) + min(pool)


if __name__ == '__main__':
    input_data = get_input(9)
    print(part1(input_data))
    print(part2(input_data))
