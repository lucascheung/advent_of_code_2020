from IPython import embed
import numpy as np

data = open('./day13.input').read().split('\n')

start = int(data[0])
buses = [int(b) for b in data[1].split(',') if b != 'x']

current = start
waiting = True
while waiting:
    for x in buses:
        if current % x == 0:
            print(x * (current-start))
            waiting = False
    current += 1


starting = []
bs = data[1].split(',')
for t, b in enumerate(bs):
    if b != 'x':
         starting.append(int(b))

step = np.prod(starting)



def check_condition(bs, current):
    for t, b in enumerate(bs):
        if b != 'x':
            if (current + t) % int(b) != 0:
                return False
    return True

bs = data[1].split(',')

current = (100000000000000 // int(bs[0]) + 1 ) * int(bs[0])
# current = int(bs[0])
print(current)
waiting = True
while waiting:
    print(current)
    if check_condition(bs, current):
        waiting = False
        print(current)
    else:
        current += step
