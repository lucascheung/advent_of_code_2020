data = list(map(lambda x: int(x.strip()), open('./day09.input').readlines()))

p = 25

def add_up(preamble, value):
    for x in preamble:
        if (value - x) in preamble and value != 2 * x:
            return True
    return False

for i in range(p, len(data)):
    if not add_up(data[i-p:i], data[i]):
        part_one = data[i]
        print(data[i])

for i in range(len(data)):
    l = 2
    seeking = True
    while sum(data[i:i+l]) <= part_one and seeking:
        if sum(data[i:i+l]) == part_one:
            print(min(data[i:i+l])+max(data[i:i+l]))
            seeking = False
        else:
            l += 1