d = [6,13,1,15,2,0]
def nth_num(n):
    turn_rec = {}
    turn = 1
    while turn <= n :
        try:
            num = d[turn-1]
        except IndexError:
            if last_seen_turn is not None:
                num = turn - last_seen_turn - 1 
            else:
                num = 0
        last_seen_turn = turn_rec.get(num)
        turn_rec[num] = turn
        turn += 1
    return num
print(nth_num(2020))
print(nth_num(30000000))
