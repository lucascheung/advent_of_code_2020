file_name = './day1.input'

with open(file_name) as f:
    content = f.readlines()
DATA = [int(x.strip()) for x in content]

# PART ONE      
def part_one(data, value):
    for x in data:
        if (value - x) in data:
            print(f"The numbers are {x} and {value - x}")
            print(f"The answer is part one {x * (value - x)}")
            return x * (value - x)
    return False

part_one(DATA, 2020)

# PART TWO
def part_two(data, value):
    for x in data:
        second_part = part_one(data, value - x)
        if second_part:
            print(f"The answer is part two {x * second_part}")
            return x * second_part

part_two(DATA, 2020)