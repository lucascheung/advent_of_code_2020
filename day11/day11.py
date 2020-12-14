import copy

og_grid = list(map(lambda x: list(x.strip()), open('./day11.input').readlines()))

def check_no_occupied(grid, x, y, r):
    top_left = grid[y-r][x-r] != '#' if x+1 > r and y+1 > r else True
    top_middle = grid[y-r][x] != '#' if y+1 > r else True
    top_right = grid[y-r][x+r] != '#' if x < len(grid[0])-r and y+1 > r else True
    middle_left = grid[y][x-r] != '#' if x+1 > r else True
    middle_right = grid[y][x+r] != '#' if x < len(grid[0])-r else True
    bottom_left = grid[y+r][x-r] != '#' if x+1 > r and y < len(grid)-1 else True
    bottom_middle = grid[y+r][x] != '#' if y < len(grid)-1 else True
    bottom_right = grid[y+r][x+r] != '#' if x < len(grid[0])-r and y < len(grid)-1 else True  
    return "#" if all([top_left, top_middle, top_right, middle_left, middle_right, bottom_left, bottom_middle, bottom_right]) else grid[y][x]

def check_number_occupied(grid, x, y, r, n):
    count = 0
    count += 1 if (grid[y-r][x-r] == '#' if x+1 > r and y+1 > r else False) else 0
    count += 1 if (grid[y-r][x] == '#' if y+1 > r else False) else 0
    count += 1 if (grid[y-r][x+r] == '#' if x < len(grid[0])-1 and y+1 > r else False) else 0
    count += 1 if (grid[y][x-r] == '#' if x+1 > r else False) else 0
    count += 1 if (grid[y][x+r] == '#' if x < len(grid[0])-1 else False) else 0
    count += 1 if (grid[y+r][x-r] == '#' if x+1 > r and y < len(grid)-1 else False) else 0
    count += 1 if (grid[y+r][x] == '#' if y < len(grid)-1 else False) else 0
    count += 1 if (grid[y+r][x+r] == '#' if x < len(grid[0])-1 and y < len(grid)-1 else False) else 0
    return "L" if count >= n else grid[y][x]

moving = True

grid = copy.deepcopy(og_grid)
while moving:
    count = 0
    new_grid = copy.deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'L':
                new_grid[y][x] = check_no_occupied(grid, x, y, 1)
            if grid[y][x] == '#':
                new_grid[y][x] = check_number_occupied(grid, x, y, 1, 4)
    count += sum([x.count('#') for x in new_grid])
    if new_grid == grid:
        moving = False
    grid = copy.deepcopy(new_grid)

# Part One
print(count)


def fn_top_left(grid, x, y):
    r = 1
    while 0 <= x-r and 0 <= y-r:
        if grid[y-r][x-r] != '.':
            return grid[y-r][x-r]
        r +=1
    return '.'

def fn_top_middle(grid, x, y):
    r = 1
    while  0 <= y-r:
        if grid[y-r][x] != '.':
            return grid[y-r][x]
        r +=1
    return '.'

def fn_top_right(grid, x, y):
    r = 1
    while x+r <= len(grid[0])-1 and 0 <= y-r:
        if grid[y-r][x+r] != '.':
            return grid[y-r][x+r]
        r +=1
    return '.'

def fn_middle_left(grid, x, y):
    r = 1
    while 0 <= x-r:
        if grid[y][x-r] != '.':
            return grid[y][x-r]
        r +=1
    return '.'

def fn_middle_right(grid, x, y):
    r = 1
    while x+r <= len(grid[0])-1:
        if grid[y][x+r] != '.':
            return grid[y][x+r]
        r +=1
    return '.'

def fn_bottom_left(grid, x, y):
    r = 1
    while 0 <= x-r and y+r <= len(grid)-1:
        if grid[y+r][x-r] != '.':
            return grid[y+r][x-r]
        r +=1
    return '.'

def fn_bottom_middle(grid, x, y):
    r = 1
    while y+r <= len(grid)-1:
        if grid[y+r][x] != '.':
            return grid[y+r][x]
        r +=1
    return '.'

def fn_bottom_right(grid, x, y):
    r = 1
    while x+r <= len(grid[0])-1 and y+r <= len(grid)-1:
        if grid[y+r][x+r] != '.':
            return grid[y+r][x+r]
        r +=1
    return '.'


def check_no_occupied_nearest(grid, x, y):
    top_left = fn_top_left(grid, x, y) != '#'
    top_middle = fn_top_middle(grid, x, y) != '#'
    top_right = fn_top_right(grid, x, y) != '#'
    middle_left = fn_middle_left(grid, x, y) != '#'
    middle_right = fn_middle_right(grid, x, y) != '#'
    bottom_left = fn_bottom_left(grid, x, y) != '#'
    bottom_middle = fn_bottom_middle(grid, x, y) != '#'
    bottom_right = fn_bottom_right(grid, x, y) != '#'
    return "#" if all([top_left, top_middle, top_right, middle_left, middle_right, bottom_left, bottom_middle, bottom_right]) else grid[y][x]

def check_number_occupied_nearest(grid, x, y, n):
    count = 0
    count += 1 if fn_top_left(grid, x, y) == '#' else 0
    count += 1 if fn_top_middle(grid, x, y) == '#' else 0
    count += 1 if fn_top_right(grid, x, y) == '#' else 0
    count += 1 if fn_middle_left(grid, x, y) == '#' else 0
    count += 1 if fn_middle_right(grid, x, y) == '#' else 0
    count += 1 if fn_bottom_left(grid, x, y) == '#' else 0
    count += 1 if fn_bottom_middle(grid, x, y) == '#' else 0
    count += 1 if fn_bottom_right(grid, x, y) == '#' else 0
    return "L" if count >= n else grid[y][x]

moving = True

grid = copy.deepcopy(og_grid)
while moving:
    count = 0
    new_grid = copy.deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'L':
                new_grid[y][x] = check_no_occupied_nearest(grid, x, y)
            if grid[y][x] == '#':
                new_grid[y][x] = check_number_occupied_nearest(grid, x, y, 5)
    count += sum([x.count('#') for x in new_grid])
    if new_grid == grid:
        moving = False
    grid = copy.deepcopy(new_grid)

# Part Two
print(count)
