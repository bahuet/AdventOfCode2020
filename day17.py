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

    for z in range(new_cube_min_z, new_cube_max_z + 1):
        new_cube[z] = []
        for y in range(new_cube_h):
            new_cube[z].append([False] * new_cube_w)
    return new_cube


def next_state_is_active(x, y, z, cube):
    point_is_active = False
    neighbours_active = 0
    next_state_active = False
    for z_probe in range(z-1, z+2):
        for y_probe in range(y-1, y+2):
            for x_probe in range(x-1, x+2):
                try:
                    if cube[z_probe][y_probe][x_probe]:
                        if z_probe == z and y_probe == y and x_probe == x:
                            point_is_active = True
                        else:
                            neighbours_active += 1
                except (KeyError, IndexError):
                    pass

    if neighbours_active == 3 or (point_is_active and neighbours_active == 2):
        next_state_active = True
    return next_state_active


def get_next_cube(cube):
    active_count = 0
    next_cube = init_next_cube(cube)
    # TODO recuperer ces infos depuis init_next_cube plutot 
    z_range = range(min(next_cube.keys()), max(next_cube.keys()) + 1)
    y_range = range(len(next_cube[0]))
    x_range = range(len(next_cube[0][0]))

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
    for i in range(1):
        active_count, next_cube = get_next_cube(cube)
        print(next_cube)
        cube = next_cube
    return active_count


def part2(initial_slice):
    pass


if __name__ == '__main__':
    DAY = 17
    input_data = get_input(DAY, True)
    print(part1(input_data))
    print(part2(input_data))
