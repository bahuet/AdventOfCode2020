import re
class DoubleRange:
    def __init__(self, values_list):
        self.amin, self.amax, self.bmin, self.bmax = values_list 
    def __contains__(self, n): #This is great
        return self.admin <= n <= self.amax or self.bmin <= n <= self.bmax
with open('inputs/16.txt') as f:
    ranges_raw, your_ticket_raw, nearby_tickets_raw = f.read().split('\n\n')
    ranges_rexp = re.compile(r'\d+')
    ranges = [DoubleRange(ranges_rexp.findall(line)) for line in ranges_raw.splitlines()]
    your_ticket = tuple(map(int, your_ticket_raw.splitlines()[1].split(',')))
    nearby_tickets = tuple(tuple(map(int, line.split(','))) for line in nearby_tickets_raw.splitlines()[1:])

