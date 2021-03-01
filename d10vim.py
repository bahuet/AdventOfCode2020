with open('inputs/10.txt') as f:
    d = list(map(int, f.read().splitlines()))
    d = [0] + d + [max(d)+3]
nums = sorted(d)
dist1, dist3 = 0, 0
for cur, nxt in zip(nums, nums[1:]):
    delta = nxt - cur
    if delta == 1:
        dist1 += 1
    elif delta == 3:
        dist3 += 1
ans = dist1 * dist3
print('Part 1:', ans)

