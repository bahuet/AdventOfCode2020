with open('inputs/9.txt') as f:
    d = tuple(map(int, f.read().splitlines()))
def two_sum(nums, target):
    comps = set()
    for n in nums:
        if n in comps:
            return True
        else:
            comps.add(target - n)
    return False
for i, v in enumerate(d[25:], 25):
    if not two_sum(d[i-25:i], v):
        break
print(v)
start = 0
end = 0 
curr_sum = 0
while curr_sum != v:
    if curr_sum < v:
        curr_sum += d[end]
        end += 1
    elif curr_sum > v:
        curr_sum -= d[start]
        start += 1

min_ =  max_ = d[start]
for i in range(start, end):
    if d[i] > max_:
        max_ = d[i]
    if d[i] < min_:
        min_ = d[i]

print(min_ + max_)
