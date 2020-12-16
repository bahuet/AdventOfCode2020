import os.path
from math import gcd
from itertools import count


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        lines = f.read().splitlines()
        data = {
            "ts": int(lines[0]),
            "ids": []
        }
        for x in lines[1].split(','):
            v = None
            try:
                v = int(x)
            except:
                v = x
            data["ids"].append(v)
        return data


def part1(data):
    ids = [x for x in data['ids'] if isinstance(x, int)]
    lowest_id = float('inf')
    lowest_depart_ts = float('inf')
    for idn in ids:
        count_until_ts = data['ts'] % idn
        depart_ts = data['ts'] - count_until_ts + idn
        if depart_ts < lowest_depart_ts:
            lowest_id = idn
            lowest_depart_ts = depart_ts
    return lowest_id * (lowest_depart_ts - data['ts'])


def lcm(a, b):
    return a * b // gcd(a, b)


def part2(data):
    # 0 == t%id1 == (t+1)%id2 == (t+3)%id3...
    ids = [(i, x) for i, x in enumerate(data['ids']) if x != 'x']
    t = 0
    step = 1
    for delta, idn in ids:
        for t in count(t, step):
            if (t+delta) % idn == 0:
                break
        step = lcm(step, idn)

    return t


if __name__ == '__main__':
    input_data = get_input(13, False)
    print(part1(input_data))
    print(part2(input_data))
