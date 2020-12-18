import re
from collections import deque
DATA = [re.findall('(\w)(\d+)',x.strip())[0] for x in open('./day12.input').readlines()]

d = 0
f = 'E'
s = deque(list('ESWN'))

for i in DATA:
    if i[0] in 'ES':
        d += int(i[1])
    elif i[0] in 'WN':
        d -= int(i[1])
    elif i[0] == 'F':
        d += int(i[1]) if f in 'ES' else 0
        d -= int(i[1]) if f in 'WN' else 0
    elif i[0] == 'L':
        s.rotate(int(i[1])//90)
        f = s[0]
    elif i[0] == 'R':
        s.rotate(-int(i[1])//90)
        f = s[0]

print(abs(d))

wx = 10
wy = 1
d = 0
for i in DATA:
    arg = int(i[1])
    if i[0] == 'F':
        d += (wx + wy) * arg
    elif i[0] == 'N':
        wy += arg
    elif i[0] == 'S':
        wy -= arg
    elif i[0] == 'E':
        wx += arg
    elif i[0] == 'W':
        wx -= arg
    elif i[0] == 'L':
        while arg:
            wx, wy = -wy, wx
            arg -= 90
    elif i[0] == 'R':
        while arg:
            wx, wy = wy, -wx
            arg -= 90

print(abs(d))