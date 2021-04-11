import re
class DoubleRange:
    def __init__(self, values_list):
        self.amin, self.amax, self.bmin, self.bmax = values_list 
    def __contains__(self, n): #This is great
        return self.amin <= n <= self.amax or self.bmin <= n <= self.bmax
with open('inputs/16.txt') as f:
    ranges_raw, your_ticket_raw, nearby_tickets_raw = f.read().split('\n\n')
    ranges_rexp = re.compile(r'\d+')
    ranges = [DoubleRange(map(int, ranges_rexp.findall(line))) for line in ranges_raw.splitlines()]
    your_ticket = tuple(map(int, your_ticket_raw.splitlines()[1].split(',')))
    nearby_tickets = tuple(tuple(map(int, line.split(','))) for line in nearby_tickets_raw.splitlines()[1:])
def invalid_fields(ticket):
    for val in ticket:
        if all(val not in rng for rng in ranges):
            yield val
count = 0
for ticket in nearby_tickets:
    for f in invalid_fields(ticket):
        count += f
print(count)
def ticket_is_valid(ticket):
    return all(any(v in rng for rng in ranges) for v in ticket)
possible = [set(range(len(your_ticket))) for _ in range(len(ranges))] # list of sets of all possible real positions for each range field.
for ticket in filter(ticket_is_valid, nearby_tickets):
    for poss, rng in zip(possible, ranges):
        for i, value in enumerate(ticket):
            if value not in rng:
                poss.discard(i)
assigned = [None] * len(possible)
while any(possible):
    for i, poss in enumerate(possible):
        if len(poss) == 1:
            assigned[i] = match =  poss.pop()
            break
    for poss in possible:
        poss.discard(match)
from math import prod
print(assigned)
print(prod(your_ticket[i] for i in assigned[:6] ))
