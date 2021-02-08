with open('inputs/4.txt') as f:
    d = f.read().split('\n\n')
KEYS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
print(sum(all(k in p for k in KEYS) for p in d))
def check_height(h):
    if h.endswith('cm'):
        return 150 <= int(h[:-2]) <= 193
    if h.endswith('in'):
        return 59 <= int(h[:-2]) <= 76
    return False
checks = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': check_height,
    'hcl': lambda x: x[0] == '#' and len(x) == 7 and all(c.isdigit() or c in 'abcdef' for c in x[1:]),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: len(x) == 9 and all(c.isdigit() for c in x),
    'cid': lambda x: True
        }
valid_count = 0
for r in d:
    passport = (field.split(':') for field in r.split())
    if all(checks[k](v) for k,v in passport):
        valid_count += 1

print(valid_count)
