file_name = './day03.input'
with open(file_name) as f:
    content = f.readlines()

MAP = [x.strip() for x in content]

def trees_encountered(shift_right, shift_down):
    idx = 0
    count = 0
    for line in MAP[shift_down::shift_down]:
        idx += shift_right if (idx + shift_right) <= len(MAP[0]) - 1 else - len(MAP[0]) + shift_right
        count += 1 if line[idx] == '#' else 0
    return count

# PART ONE
print(f'Answer for Part One: {trees_encountered(3, 1)}')

#PART TWO
print(
trees_encountered(1, 1) * \
trees_encountered(3, 1) * \
trees_encountered(5, 1) * \
trees_encountered(7, 1) * \
trees_encountered(1, 2)
)
