DATA = open('./day06.input').read().split('\n\n')

part_one = sum(map(lambda g: len(set(list(g.replace('\n', '')))), DATA))
part_two = sum(map(lambda g: len(set.intersection(*map(set, g.split('\n')))), DATA))

print(part_one)
print(part_two)