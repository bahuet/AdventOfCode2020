import re
from itertools import product
with open('inputs/14.txt') as f:
    lines = f.readlines()
rexp = re.compile('^mem\[(\d+)\] = (\d+)$')
mem1 = {}
mem2 = {}
def all_addr(addr, mask):
    addr_bin = format(addr, '036b')
    prod_args = []
    for ab, mb in zip(addr_bin, mask):
        if mb == '0':
            arg = ab
        elif mb == '1':
            arg = '1'
        else:
            arg = '01'
        prod_args.append(arg)
    for possible_addr in product(*prod_args):
        yield int(''.join(possible_addr), 2) 
for line in lines:
    if line.startswith("mask"):
        mask = line[7:].rstrip()
        hard_mask = int(mask.replace('1','0').replace('X','1'), 2)
        soft_mask = int(mask.replace('X','0'), 2)
    else:
        addr, val = map(int, rexp.findall(line)[0])
        mem1[addr] = val & hard_mask | soft_mask
        for new_addr in all_addr(addr, mask):
            mem2[new_addr] = val
print(sum(mem1.values()), sum(mem2.values()))



