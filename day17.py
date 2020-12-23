import os.path


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    def char_to_bool(c): return True if c == '#' else False
    def line_to_list(line): return [char_to_bool(c) for c in line]
    with open(input_path) as f:
        return [line_to_list(line) for line in f.read().splitlines()]


def init_next_cube(cube):
    new_cube = {}

    new_cube_min_z = min(cube.keys()) - 1
    new_cube_max_z = max(cube.keys()) + 1
    new_cube_h = len(cube[0]) + 2
    new_cube_w = len(cube[0][0]) + 2

    z_range = range(new_cube_min_z, new_cube_max_z + 1)
    y_range = range(new_cube_h)
    x_range = range(new_cube_w)

    for z in z_range:
        new_cube[z] = []
        for _ in y_range:
            new_cube[z].append([False] * new_cube_w)
    return new_cube, z_range, y_range, x_range


def get_points_info(x, y, z, cube):
    active_neighbours_count = 0
    point_is_active = False
    probing_range = range(-1, 2)
    probing_range2 = range(0, 3)
    for i in probing_range:
        z_probe = z + i
        for j in probing_range2:
            y_probe = y + j
            for k in probing_range2:
                x_probe = x + k
                try:
                    if cube[z_probe][y_probe][x_probe]:
                        if z_probe == z and y_probe == y and x_probe == x:
                            point_is_active = True
                        else:
                            active_neighbours_count += 1
                except (KeyError, IndexError):
                    pass
    return active_neighbours_count, point_is_active


def next_state_is_active(x, y, z, cube):
    active_neighbours_count, point_is_active = get_points_info(x, y, z, cube)

    if active_neighbours_count == 3 or (active_neighbours_count == 2 and point_is_active):
        return True
    else:
        return False


def get_next_cube(cube):
    active_count = 0
    next_cube, z_range, y_range, x_range = init_next_cube(cube)

    for z in z_range:
        for y in y_range:
            for x in x_range:
                active_state = next_state_is_active(x, y, z, cube)
                if active_state:
                    next_cube[z][y][x] = active_state
                    active_count += 1
    return active_count, next_cube


def part1(initial_slice):
    cube = {0: initial_slice}
    for _ in range(1):
        active_count, next_cube = get_next_cube(cube)
        print(next_cube[0])
        cube = next_cube
    return active_count


def part2(initial_slice):
    pass


if __name__ == '__main__':
    DAY = 17
    input_data = get_input(DAY, True)
    print(part1(input_data))
    print(part2(input_data))
