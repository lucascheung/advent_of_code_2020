import re

file_name = './day02.input'
with open(file_name) as f:
    content = f.readlines()

DATA = [x.strip() for x in content]
regex = r"(\d+)-(\d+) (\w): (\w+)"

part_one = 0
part_two = 0
for line in DATA:
    matches = re.findall(regex, line)[0]
    minimum = int(matches[0])
    maximum = int(matches[1])
    letter = matches[2]
    pw = matches[3]
    if pw.count(letter) >= minimum and pw.count(letter) <= maximum:
        part_one += 1
    count = 0
    count += 1 if pw[minimum - 1] == letter else 0
    count += 1 if pw[maximum - 1] == letter else 0
    part_two += 1 if count == 1 else 0

print(f"Answer for part one: {part_one}")
print(f"Answer for part two: {part_two}")
