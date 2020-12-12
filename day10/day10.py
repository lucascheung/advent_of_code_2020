data = sorted(list(map(lambda x: int(x.strip()), open('./day10.input').readlines())))
data.insert(0, 0)
one = 0
three = 1

for i in range(len(data)-1):
    if data[i+1]-data[i] == 1:
        one += 1
    elif data[i+1]-data[i] == 3:
        three += 1
print(one * three)

two_diff = 1
three_diff = 1
current = 2 if data[2] - data[0] < 3 else 1

for i in range(3,len(data)):
    old_current = current
    current += two_diff if data[i] - data[i-2] <= 3 else 0
    current += three_diff if data[i] - data[i-3] <= 3 else 0
    three_diff = two_diff
    two_diff = old_current
    
print(current)
