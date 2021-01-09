import os.path
import re
from functools import reduce


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        return f.read()


def parse_input(inputdata):
    tiles = {}
    for rawtile in inputdata.strip().split('\n\n'):
        tile_line = rawtile.split('\n')
        tileid = int(re.match('Tile (\d+):', tile_line[0])[1])
        tiles[tileid] = [list(line) for line in tile_line[1:]]
    return tiles


def get_tile_patterns(tile):
    top_pattern = right_pattern = left_pattern = bot_pattern = ''
    for i in range(len(tile)):
        top_pattern += tile[0][i]
        bot_pattern += tile[-1][-i-1]
        left_pattern += tile[-i-1][0]
        right_pattern += tile[i][-1]
    return [top_pattern, right_pattern, bot_pattern, left_pattern]


def get_active_tile_patterns(tile, patterns_tiles):
    return remove_unique_patterns(get_tile_patterns(tile), patterns_tiles)


def build_tiles_sides_patterns(tiles):
    tiles_sides_patterns = {}
    for tileid, tile in tiles.items():
        tiles_sides_patterns[tileid] = get_tile_patterns(tile)
    return tiles_sides_patterns


def get_pattern_numeric_value(pattern):
    num = 0
    for i, c in enumerate(pattern):
        if c == '#':
            num += 10**i
    return num


def get_pattern_universal_num_value(pattern):
    return min(get_pattern_numeric_value(pattern), get_pattern_numeric_value(pattern[::-1]))


def get_patterns_tiles(tiles_sides_patterns):
    patterns_tiles = {}
    for tileid, tile_patterns in tiles_sides_patterns.items():
        for pattern in tile_patterns:
            pattern_univ_num = get_pattern_universal_num_value(pattern)
            if not patterns_tiles.get(pattern_univ_num):
                patterns_tiles[pattern_univ_num] = [tileid]
            else:
                patterns_tiles[pattern_univ_num].append(tileid)
    return patterns_tiles


def pattern_is_unique(pattern, patterns_tiles):
    return len(patterns_tiles[get_pattern_universal_num_value(pattern)]) == 1


def remove_unique_patterns(tile_patterns, patterns_tiles):
    for pat_idx, pattern in enumerate(tile_patterns):
        # side is unique
        if pattern_is_unique(pattern, patterns_tiles):
            tile_patterns[pat_idx] = None
    return tile_patterns


def get_corners(tiles_sides_patterns):
    corners = []
    for tileid, tile_patterns in tiles_sides_patterns.items():
        # is it a corner?
        if tile_patterns.count(None) == 2:
            corners.append(tileid)
    return corners


def part1(data):
    tiles = parse_input(data)
    tiles_sides_patterns = build_tiles_sides_patterns(tiles)
    patterns_tiles = get_patterns_tiles(tiles_sides_patterns)
    for tile_patterns in tiles_sides_patterns.values():
        remove_unique_patterns(tile_patterns, patterns_tiles)
    corners = get_corners(tiles_sides_patterns)
    return reduce(lambda x, y: x*y, corners)


def rotate_tile(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]


def flip_tile(m, axis):
    tempm = m.copy()
    if axis == 1:
        for i in range(0, len(tempm), 1):
            tempm[i].reverse()
    elif axis == 0:
        tempm.reverse()
    else:
        raise Exception
    return tempm


def get_pat_pos_on_tile(pattern, tile_patterns):
    pattern_univ = get_pattern_universal_num_value(pattern)
    for i, pat in enumerate(tile_patterns):
        if get_pattern_universal_num_value(pat) == pattern_univ:
            return i, pat == pattern


def get_adapted_tile(pattern, position, tile):
    # rotate tile until the pattern matches
    tile_patterns = get_tile_patterns(tile)
    pat_pos_on_tile, needs_flipping = get_pat_pos_on_tile(pattern, tile_patterns)

    # fix HERE
    while (pat_pos_on_tile-2) % 4 != position:
        tile = rotate_tile(tile)
        tile_patterns = get_tile_patterns(tile)
        pat_pos_on_tile, needs_flipping = get_pat_pos_on_tile(pattern, tile_patterns)
    # flip tile if necessary
    if needs_flipping:
        tile = flip_tile(tile, (pat_pos_on_tile + 1) % 2)
    return tile


def get_test_image_matrix():
    with open('inputs/20test_img2.txt') as f:
        test_image_matrix = []
        for tiles_block_index, tiles_block in enumerate(f.read().split('\n\n')):
            block_tile_matrices = []
            for line_index, line in enumerate(tiles_block.split('\n')):
                for tile_index_in_line, tile_line in enumerate(line.split(' ')):
                    try:
                        block_tile_matrices[tile_index_in_line]['tile'].append(list(tile_line))
                    except:
                        block_tile_matrices.append({'tile': [list(tile_line)], 'tileid': 0})
            test_image_matrix.append(block_tile_matrices)
        return test_image_matrix


def get_final_image(matrix):
    """Remove borders and fuse into one big matrix"""
    final_image = []
    # matrix is a list of list of tiles.
    # a tile is also a list of list.
    for tile_y, list_of_tiles in enumerate(matrix):
        for tile_x, tile_dict in enumerate(list_of_tiles):
            shortened_height_tile = tile_dict['tile'][1:-1]
            for tile_line_index_within_tile, tile_line in enumerate(shortened_height_tile):
                shortened_length_tile_line = tile_line[1:-1]
                try:
                    final_index = tile_y * len(shortened_height_tile) + tile_line_index_within_tile
                    final_image[final_index].extend(shortened_length_tile_line)
                except Exception as e:
                    final_image.append(shortened_length_tile_line)
    return final_image


def part2(data):

    monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
    # todo:
    # build a dict with tileid:[side patterns], with globally unique patterns set to None
    tiles = parse_input(data)
    tiles_sides_patterns = build_tiles_sides_patterns(tiles)
    patterns_tiles = get_patterns_tiles(tiles_sides_patterns)
    for tile_patterns in tiles_sides_patterns.values():
        remove_unique_patterns(tile_patterns, patterns_tiles)
    corners = get_corners(tiles_sides_patterns)

    # make a new matrix with all the tiles connected and rotated:
    # take a corner and rotate it until its active sides are to the right and bottom (topleft corner)
    # use that to set all the x == 0 tiles
    # then do all the lines all by one
    image_matrix = [[None] * 12 for _ in range(12)]
    topleft_tile_id = corners[0]
    topleft_tile = tiles[topleft_tile_id]

    topleft_tile_patterns = get_active_tile_patterns(topleft_tile, patterns_tiles)
    while 1:
        topleft_tile = rotate_tile(topleft_tile)
        topleft_tile_patterns = get_active_tile_patterns(topleft_tile, patterns_tiles)
        if topleft_tile_patterns[1] and topleft_tile_patterns[2]:
            break
    image_matrix[0][0] = {'tileid': topleft_tile_id, 'tile': topleft_tile}

    for y in range(1, 12):
        upper_tile_dict = image_matrix[y - 1][0]
        upper_tile_bot_pattern = get_tile_patterns(upper_tile_dict['tile'])[2]
        upper_tile_bot_univ_num = get_pattern_universal_num_value(upper_tile_bot_pattern)
        current_tileid = next(v for v in patterns_tiles[upper_tile_bot_univ_num] if v != upper_tile_dict['tileid'])
        image_matrix[y][0] = {'tileid': current_tileid,
                              'tile': get_adapted_tile(upper_tile_bot_pattern, 2, tiles[current_tileid])}
    for x in range(1, 12):
        for y in range(12):
            left_tile_dict = image_matrix[y][x - 1]
            left_tile_right_pattern = get_tile_patterns(left_tile_dict['tile'])[1]
            left_tile_right_univ_num = get_pattern_universal_num_value(left_tile_right_pattern)
            current_tileid = next(v for v in patterns_tiles[left_tile_right_univ_num] if v != left_tile_dict['tileid'])
            image_matrix[y][x] = {'tileid': current_tileid,
                                  'tile': get_adapted_tile(left_tile_right_pattern, 1, tiles[current_tileid])}

    #test_image_matrix = get_test_image_matrix()
    # fuse is all together in one big list, remove the borders

    final_image = get_final_image(image_matrix)

    monster_list = [list(line) for line in monster.split('\n')]
    possible_monsters = []
    for i in range(4):
        current_m = monster_list
        for _ in range(i):
            current_m = rotate_tile(current_m)
        possible_monsters.append(current_m)
        possible_monsters.append(flip_tile(current_m, 0))

    # then, do a monster pattern scan for all 4 orientations and their 4 flipped mirror images on the entire image
    monster_size = len([1 for c in monster if c == '#'])

    def detect_monster(x, y, monster, image):
        for m_y in range(len(monster)):
            for m_x in range(len(monster[m_y])):
                try:
                    if monster[m_y][m_x] == '#' and image[y+m_y][x+m_x] != '#':
                        return False
                except:
                    return False
        print('monster at', x, y)
        return True

    def get_water_roughness(image):
        monster_count = 0
        sharp_count = 0
        for y, line in enumerate(image):
            for x, _ in enumerate(line):
                found_monster = False
                for monster in possible_monsters:
                    if detect_monster(x, y, monster, image):
                        found_monster = True
                if found_monster:
                    monster_count += 1
                elif image[y][x] == '#':
                    sharp_count += 1

        print('monster count:', monster_count)
        return sharp_count - monster_count * monster_size

    # TEST

    # test_image = [list(line) for line in open('inputs/20test_img.txt').read().splitlines()]
    # for i, final_image_line in enumerate(final_image):
    #     for j, c in enumerate(final_image_line):
    #         if test_image[i][j] != c:
    #             raise Exception
    # print(get_water_roughness(test_image))

    # (because we cannot know if we have to correct orientation or side)
    # is it possible that monster patterns overlap ?
    # if not, we can just count the number of '#' in the pattern and add them up
    # if yes, we'll have to do something else, we'll see later
    # gl
    return get_water_roughness(final_image)


# 2148 too low
# 2530 too high
if __name__ == '__main__':
    DAY = 20
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
