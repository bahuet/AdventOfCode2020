import re
with open('inputs/2.txt') as f:
    d = re.findall(r'(\d+)-(\d+)\s(\w):\s(\w+)',f.read())
valid = 0
for cmin, cmax, L, pwd in d:
    if int(cmin) <= pwd.count(L) <= int(cmax):
        valid += 1
print(valid)

