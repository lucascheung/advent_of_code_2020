import re
from bag import Bag
from IPython import embed

DATA = list(map(lambda x: x.strip(), open('./day07.input').readlines()))
rule_r = r'(\w+ \w+) bags contain (.+).'
content_r = r'(\d+) (\w+ \w+) bags*'

bags = []
bags_dict = {}

for rule in DATA:
    rule_match = re.fullmatch(rule_r, rule)
    color = rule_match[1]
    content = dict(map(lambda c: (c[1], int(c[0])), re.findall(content_r, rule_match[2])))
    bags.append(Bag(color, content))
    bags_dict[color] = Bag(color, content)

bags.sort(key=lambda x: len(x.content))



def contain_at_least_one(color, bags):
    solved = []
    has_gold = []
    while len(solved) < len(bags):
        for bag in bags:
            if bag.empty():
                bag.has_gold = False
                bags = list(map(lambda b: b.remove(bag.color), bags))
                solved.append(bag.color)
            elif bag.contains(color) or any(map(lambda b: b.has_gold, list(filter(lambda x: x.color in bag.content.keys(), bags)))):
                bag.has_gold = True
                has_gold.append(bag.color)
                solved.append(bag.color)

        solved = list(set(solved))
        has_gold = list(set(has_gold))
    return len(has_gold)


print(contain_at_least_one('shiny gold', bags))




# total = []

# def add_bags(bags_dict, color):
#     for c, v in bags_dict[color].hard_content.items():
#         if add_bags(bags_dict, c):
#             print(c, v)
#             return v * add_bags(bags_dict, c)
#         else:
#             total.append(bags_dict[color].direct_bags)
            
# add_bags(bags_dict, 'shiny gold')

# embed()
