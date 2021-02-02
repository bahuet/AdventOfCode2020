import re
with open('inputs/2.txt') as f:
    d = re.findall(r'(\d+)-(\d+)\s(\w):\s(\w+)',f.read())
valid = 0
valid2 = 0
for cmin, cmax, L, pwd in d:
    cmin = int(cmin)
    cmax = int(cmax)
    if cmin <= pwd.count(L) <= cmax:
        valid += 1
    if (pwd[cmin-1] == L) ^ (pwd[cmax-1] == L):
        valid2 += 1
print(valid, valid2)

