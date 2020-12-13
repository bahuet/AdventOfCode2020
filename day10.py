import os.path


def get_input(day):
    input_path = os.path.join('inputs', str(day) + '.txt')
    with open(input_path) as f:
        data = [int(x) for x in f.read().splitlines()]
        return data


def get_sorted_adapters(data):
    adapters_sorted = sorted(data)
    # add outlet and adapter
    adapters_sorted.insert(0, 0)
    adapters_sorted.append(adapters_sorted[-1]+3)
    return adapters_sorted


def count_differences(data):
    adapters_sorted = get_sorted_adapters(data)
    counts = {}
    for i in range(1, len(adapters_sorted)):
        diff = adapters_sorted[i] - adapters_sorted[i-1]
        counts[diff] = counts[diff] + 1 if counts.get(diff) else 1
    return counts


def part1(data):
    counts = count_differences(data)
    return(counts[1] * counts[3])


def nb_of_paths(i, lst, hm):
    if i == len(lst) - 1:
        return 1
    if i in hm:
        return hm[i]
    x = 0
    for j in range(i+1, min(i+4, len(lst))):
        if lst[j] - lst[i] <= 3:
            x += nb_of_paths(j, lst, hm)
    hm[i] = x
    return x

def part2(data):
    adapters = get_sorted_adapters(data)
    hashmapu = {}
    return nb_of_paths(0, adapters, hashmapu)



if __name__ == '__main__':
    input_data = get_input(10)
    print(part1(input_data))
    print(part2(input_data))
