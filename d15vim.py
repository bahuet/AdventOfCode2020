d = [6,13,1,15,2,0]
def nth_num(n):
    turn_rec = {num:turn for turn, num in enumerate(d[:-1], 1)}
    prev = d[-1]
    for turn in range(len(d)+1, n+1):
        if prev in turn_rec:
            num = turn - turn_rec[prev] - 1 
        else:
            num = 0
        turn_rec[prev] = turn - 1 
        prev = num
    return num
print(nth_num(2020))
#print(nth_num(30000000))
