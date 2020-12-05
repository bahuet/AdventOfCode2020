path = 'inputs/1.txt'
xs = [int(x) for x in open(path).read().splitlines()]
for i in range(len(xs)):
    for j in range(i+1, len(xs)):
        if xs[i] + xs[j] == 2020:
            print('2',xs[i]*xs[j])
        for k in range(j+1, len(xs)):
            if xs[i] + xs[j] + xs[k] == 2020:
                print('3', xs[i] * xs[j] * xs[k])
