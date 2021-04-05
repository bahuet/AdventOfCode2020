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
