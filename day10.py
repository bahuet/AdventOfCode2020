import os.path


def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
    with open(input_path) as f:
        data = [int(x) for x in f.read().splitlines()]
        return data


def count_differences(data):
    adapters_sorted = sorted(data)
    # add outlet and adapter
    adapters_sorted.insert(0, 0)
    adapters_sorted.append(adapters_sorted[-1]+3)
    counts = {}
    for i in range(1, len(adapters_sorted)):
        diff = adapters_sorted[i] - adapters_sorted[i-1]
        counts[diff] = counts[diff] + 1 if counts.get(diff) else 1
    return counts


def part1(data):
    counts = count_differences(data)
    return(counts[1] * counts[3])


def part2(data):
    pass


if __name__ == '__main__':
    input_data = get_input(10)
    print(part1(input_data))
    print(part2(input_data))
