import os.path


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        return [int(x) for x in f.read().split(',')]




def get_nth_number(n, data):
    # create and populate the hashmap used to store the indexes
    last_index_bank = {}
    for i, d in enumerate(data):
        if i != len(data) - 1:
            last_index_bank[d] = i
    previous_number = d
    for current_index in range(i+1, n):
        previous_number_last_index = last_index_bank.get(previous_number)

        last_index_bank[previous_number] = current_index - 1
        current_number = current_index - 1 - previous_number_last_index if previous_number_last_index is not None else 0

        previous_number = current_number
    return current_number



def part1(data):
    return get_nth_number(2020, data)


def part2(data):
    return get_nth_number(30000000, data)


if __name__ == '__main__':
    DAY = 15
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
