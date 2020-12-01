file_name = './day1.input'

with open(file_name) as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

# PART ONE      
def part_one(content, value):
    for x in content:
        if (value - x) in content:
            print(f"The numbers are {x} and {value - x}")
            print(f"The answer is part one {x * (value - x)}")
            return x * (value - x)
    return False

part_one(content, 2020)

# PART TWO
def part_two(content, value):
    for x in content:
        second_part = part_one(content, value - x)
        if second_part:
            print(f"The answer is part two {x * second_part}")
            return x * second_part

part_two(content, 2020)