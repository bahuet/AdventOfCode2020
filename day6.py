import os.path


def get_input(day):
    input_path = os.path.join('inputs', str(day) +'.txt')
    f = open(input_path, 'r')
    data =[x.replace('\n', '') for x in f.read().split('\n\n')]
    return data



def part1(data):
    sum = 0
    for d in data:
        sum += len(set(d))
    return sum

def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input(6)
    print(part1(input_data))
    print(part2(input_data))
