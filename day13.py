import os.path


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

# 774995113 too high
def part2(data):
    pass


if __name__ == '__main__':
    input_data= get_input(13, False)
    print(part1(input_data))
    print(part2(input_data))
