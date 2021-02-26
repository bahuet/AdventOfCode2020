with open('inputs/8.txt') as f:
    d=tuple(map(lambda x: (x[0],int(x[1])), map(lambda x: x.split(), f.read().splitlines())))
def run():
    pos = 0 
    acc = 0
    visited = set()
    while pos != len(d) - 1:
        if pos in visited:
            return False, acc 
        visited.add(pos)
        op, arg = d[pos]
        if op == 'acc':
            acc += arg
        elif op == 'jmp':
            pos += arg - 1
        pos += 1
    return True, acc

print(run())

