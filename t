with open('inputs/6.txt') as f:
	groups_raw = f.read().split('/n/n')
groups = tuple(map(lambda g:g.splitlines(), groups_raw))

