import os.path


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    def char_to_bool(c): return True if c == '#' else False
    def line_to_list(line): return [char_to_bool(c) for c in line]
    with open(input_path) as f:
        return [line_to_list(line) for line in f.read().splitlines()]


def init_next_cube(cube):
    next_cube = {}

    next_cube_min_z = min(cube.keys()) - 1
    next_cube_max_z = max(cube.keys()) + 1
    next_cube_h = len(cube[0]) + 2
    next_cube_w = len(cube[0][0]) + 2

    z_range = range(next_cube_min_z, next_cube_max_z + 1)
    y_range = range(next_cube_h)
    x_range = range(next_cube_w)

    for z in z_range:
        next_cube[z] = []
        for _ in y_range:
            next_cube[z].append([False] * next_cube_w)
    return next_cube, z_range, y_range, x_range


def get_cube_points_neighbor_infos(z_next_cube, y_next_cube, x_next_cube, cube):
    active_neighbours_count = 0
    point_is_active = False
    probing_range = range(-1, 2)

    for i in probing_range:
        z_probe = z_next_cube + i
        for j in probing_range:
            y_probe = y_next_cube + j
            for k in probing_range:
                x_probe = x_next_cube + k
                try:
                    if y_probe < 0 or x_probe < 0:
                        raise IndexError
                    if cube[z_probe][y_probe][x_probe]:
                        if z_probe == z_next_cube and y_probe == y_next_cube and x_probe == x_next_cube:
                            point_is_active = True
                        else:
                            active_neighbours_count += 1
                except (KeyError, IndexError):
                    pass
    return active_neighbours_count, point_is_active


def next_state_is_active(z_next_cube, y_next_cube, x_next_cube, cube):
    active_neighbours_count, point_is_active = get_cube_points_neighbor_infos(
        z_next_cube, y_next_cube, x_next_cube, cube)

    if active_neighbours_count == 3 or (active_neighbours_count == 2 and point_is_active):
        return True
    else:
        return False


def get_next_cube(cube):
    active_count = 0
    next_cube, z_range, y_range, x_range = init_next_cube(cube)

    for z_next_cube in z_range:
        for y_next_cube in y_range:
            for x_next_cube in x_range:
                active_state = next_state_is_active(z_next_cube, y_next_cube - 1, x_next_cube - 1, cube)
                if active_state:
                    next_cube[z_next_cube][y_next_cube][x_next_cube] = active_state
                    active_count += 1
    return active_count, next_cube


def part1(initial_slice):
    cube = {0: initial_slice}
    for _ in range(6):
        active_count, next_cube = get_next_cube(cube)
        cube = next_cube
    return active_count


def init_next_hypercube(hypercube):
    next_hypercube = {}

    next_hypercube_min_w = min(hypercube.keys()) - 1
    next_hypercube_max_w = max(hypercube.keys()) + 1
    w_range = range(next_hypercube_min_w, next_hypercube_max_w + 1)

    for w in w_range:
        next_cube, z_range, y_range, x_range = init_next_cube(hypercube[0])
        next_hypercube[w] = next_cube

    return next_hypercube, w_range, z_range, y_range, x_range


def get_hypercube_points_neighbor_infos(w, z, y, x, hc):
    active_neighbours_count = 0
    point_is_active = False
    probing_range = range(-1, 2)
    for o in probing_range:
        w_probe = w + o
        for i in probing_range:
            z_probe = z + i
            for j in probing_range:
                y_probe = y + j
                for k in probing_range:
                    x_probe = x + k
                    try:
                        if y_probe < 0 or x_probe < 0:
                            raise IndexError
                        if hc[w_probe][z_probe][y_probe][x_probe]:
                            if w_probe == w and z_probe == z and y_probe == y and x_probe == x:
                                point_is_active = True
                            else:
                                active_neighbours_count += 1
                    except (KeyError, IndexError):
                        pass
    return active_neighbours_count, point_is_active


def next_hypercube_state_is_active(w_next_hc, z_next_hc, y_next_hc, x_next_hc, hypercube):
    active_neighbours_count, point_is_active = get_hypercube_points_neighbor_infos(
        w_next_hc, z_next_hc, y_next_hc, x_next_hc, hypercube)

    if active_neighbours_count == 3 or (active_neighbours_count == 2 and point_is_active):
        return True
    else:
        return False


def get_next_hypercube(hypercube):
    active_count = 0
    next_hypercube, w_range, z_range, y_range, x_range = init_next_hypercube(hypercube)
    for w in w_range:
        for z in z_range:
            for y in y_range:
                for x in x_range:
                    is_active = next_hypercube_state_is_active(w, z, y - 1, x - 1, hypercube)
                    if is_active:
                        next_hypercube[w][z][y][x] = is_active
                        active_count += 1
    return next_hypercube, active_count


def part2(initial_slice):
    # loop through hypercube iterations
    cube = {0: initial_slice}
    hypercube = {0: cube}
    for _ in range(6):
        hypercube, active_count = get_next_hypercube(hypercube)
    return active_count


if __name__ == '__main__':
    DAY = 17
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
