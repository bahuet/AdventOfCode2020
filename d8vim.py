with open('inputs/8.txt') as f:
    d=tuple(map(lambda x: (x[0],int(x[1])), map(lambda x: x.split(), f.read().splitlines())))
def cons_ins(op, arg, pos, acc):
    if op == 'acc':
        acc += arg
    elif op == 'jmp':
        pos += arg - 1
    pos += 1
    return pos, acc

def run(pos, acc):
    visited = set()
    while pos != len(d):
        visited.add(pos)
        new_pos, new_acc = cons_ins(*d[pos], pos, acc)
        if new_pos in visited:
            return False, acc, pos, visited
        else:
            pos = new_pos
            acc = new_acc
    return True, acc, pos, visited

print(run(0,0)[1])

WINNING = set()
LOSING = set()
for i in range(len(d)):
    if i in WINNING or i in LOSING:
        continue
    finished, *_, visited = run(i,0)
    if finished:
        WINNING |= visited
    else:
        LOSING |= visited
pos2 = 0
acc2 = 0
switched = False
while pos2 != len(d):
    op, arg = d[pos2]
    if not switched:
        if op == 'jmp':
            switched_op = 'nop'
        elif op == 'nop':
            switched_op = 'jmp'
        else:
            switched_op = None
        if switched_op and cons_ins(switched_op, arg, pos2, 0)[0] in WINNING:
            switched = True
            op = switched_op
    pos2, acc2 = cons_ins(op, arg, pos2, acc2)
print(acc2)
