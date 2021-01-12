import os.path


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        decks = [[int(x) for i, x in enumerate(d.splitlines()) if i != 0] for d in f.read().split('\n\n')]
        return decks


def play_one_round(d1, d2):
    c1 = d1.pop(0)
    c2 = d2.pop(0)
    if c1 > c2:
        d1.extend([c1, c2])
    else:
        d2.extend([c2, c1])


def get_final_winning_deck(d1, d2):
    while len(d1) > 0 and len(d2) > 0:
        play_one_round(d1, d2)
    return d1 if len(d1) > 1 else d2


def compute_score(deck):
    score_aggr = 0
    for i, v in enumerate(deck):
        score_aggr += v * (len(deck) - i)
    return score_aggr


def part1(decks):
    winning_deck = get_final_winning_deck(decks[0][:], decks[1][:])
    score = compute_score(winning_deck)
    return score


def play_recursive_combat(d1, d2):
    history = set()
    while len(d1) > 0 and len(d2) > 0:
        round_key = str(d1) + str(d2)
        if round_key in history:
            return 1, []
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if c1 <= len(d1) and c2 <= len(d2):
            winner, _ = play_recursive_combat(d1[:c1], d2[:c2])
            if winner == 1:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
        else:
            if c1 > c2:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
        history.add(round_key)
    return (1, d1) if len(d1) > 1 else (0, d2)


def part2(decks):
    _, winners_deck = play_recursive_combat(decks[0][:], decks[1][:])
    return compute_score(winners_deck)


if __name__ == '__main__':
    DAY = 22
    decks = get_input(DAY, False)
    print(part1(decks))
    print(part2(decks))
