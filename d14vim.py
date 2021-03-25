with open('inputs/14.txt') as f:
    lines = f.readlines()
import re
rexp = re.compile('^mem\[(\d+)\] = (\d+)$')
mem = {}
for line in lines:
    if line.starswith('mask'):
        mask = line[7:].rstrip()
    else:
        addr, val = map(int, rexp.findall(line)[0])
        
