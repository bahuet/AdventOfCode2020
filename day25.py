import os.path


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        return tuple(int(x) for x in f.read().splitlines())


def transform_once(val, subject_number):
    return val * subject_number % 20201227


def get_transform_generator():
    val = 1
    subject_number = 7
    while True:
        val = transform_once(val, subject_number)
        yield val


def find_loop_sizes(card_pub_key, door_pub_key):
    card_loop_size = None
    door_loop_size = None
    loop_count = 0
    pub_key_gen = get_transform_generator()

    while card_loop_size is None or door_loop_size is None:
        current_pub_key = next(pub_key_gen)
        if current_pub_key == card_pub_key:
            card_loop_size = loop_count
        if current_pub_key == door_pub_key:
            door_loop_size = loop_count
        loop_count += 1
    print(card_loop_size, door_loop_size)
    return card_loop_size, door_loop_size


def part1(data):
    card_pub_key, door_pub_key = data
    card_loop_size, door_loop_size = find_loop_sizes(card_pub_key, door_pub_key)
    subject_number = door_pub_key
    val = 1
    for _ in range(card_loop_size + 1):
        val = transform_once(val, subject_number)
    
    return val



def part2(data):
    pass


if __name__ == '__main__':
    DAY = 25
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
