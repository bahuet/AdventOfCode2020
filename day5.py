import os.path


def get_input():
    input_path = os.path.join('inputs', 'day5-input.txt')
    f = open(input_path, 'r')
    data = f.read().split('\n')
    data.pop()
    return data


def extract_row_col(boarding_pass):
    row_str = boarding_pass[:7]
    col_str = boarding_pass[-3:]
    row_str_bin = row_str.replace('F', '0').replace('B', '1')
    col_str_bin = col_str.replace('L', '0').replace('R', '1')
    row = int(row_str_bin, 2)
    col = int(col_str_bin, 2)
    return row, col


def part1(boarding_passes):
    seatid_max = -1
    for bp in boarding_passes:
        row, col = extract_row_col(bp)
        seatid = row * 8 + col
        if seatid > seatid_max:
            seatid_max = seatid
    return seatid_max


def part2(boarding_passes):
    # we could compute all the seatids, sort them, and scan them linearly, but is there a bit operation trick we could use?
    # do scan first
    get_seatid = lambda x: x[0] * 8 + x[1]
    sorted_seatid_list = sorted([get_seatid(extract_row_col(bp)) for bp in boarding_passes])
    for i in range(1, len(sorted_seatid_list)):
        if sorted_seatid_list[i - 1] + 1 != sorted_seatid_list[i]:
            return sorted_seatid_list[i - 1] + 1
    return None

#740 too high

if __name__ == '__main__':
    input_data = get_input()
    print(part1(input_data))
    print(part2(input_data))
