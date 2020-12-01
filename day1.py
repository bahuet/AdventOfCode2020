import os.path


def get_input():
    input_path = os.path.join('inputs', 'day1-input.txt')

    f = open(input_path, 'r')
    data = f.read().split('\n')
    data.pop()
    return [int(val) for val in data]

def part1():
    data = get_input()
    data_set = set(data)

    for curr_num in data:
        goal = 2020 - curr_num
        if goal in data_set:
            return curr_num * goal


def part2():
    data = get_input()
    data_set = set(data)
    for numi in data:
        for numj in data[1:]:
            goal =  2020 - (numi + numj)
            if goal in data_set:
                return numi * numj * goal



if __name__ == '__main__':
    print(part1())
    print(part2())
    
