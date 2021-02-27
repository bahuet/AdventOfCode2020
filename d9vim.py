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
