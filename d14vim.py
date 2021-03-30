with open('inputs/14.txt') as f:
    lines = f.readlines()
import re
rexp = re.compile('^mem\[(\d+)\] = (\d+)$')
mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line[7:].rstrip()
        and_mask = int(mask.replace('1','0').replace('X','1'),2)
        or_mask = int(mask.replace('X','0'),2)
    else:
        addr, val = map(int, rexp.findall(line)[0])
        mem[addr] = val & and_mask | or_mask
print(sum(mem.values()))
