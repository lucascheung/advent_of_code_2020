import re

regex = r'(\w{3}) (\S\d+)\n*'
DATA = list(map(lambda l: re.findall(regex, l)[0], open('./day08.input').readlines()))

def process(ct, idx, data, processed):
    processed.append(idx)
    if data[idx][0] == 'acc':
        ct += int(data[idx][1])
        idx += 1 
    elif data[idx][0] == 'nop':
        idx += 1
    elif data[idx][0] == 'jmp':
        idx += int(data[idx][1])
    return ct, idx, processed
    
def find_breakpoint(start_idx, data):
    count = 0
    index = start_idx
    processed = []
    while index not in processed and index < len(data):
        count, index, processed = process(count, index, data, processed)
    return count, index

def switch_one(data, idx):
    n_data = data.copy()
    if n_data[idx][0] == 'nop':
        n_data[idx] = ('jmp', n_data[idx][1])
    elif n_data[idx][0] == 'jmp':
        n_data[idx] = ('nop', n_data[idx][1])
    return n_data

print(find_breakpoint(0, DATA)[0])

max_count = 0
max_index = 0
for x in range(len(DATA)):
    data = switch_one(DATA, x)
    count, index = find_breakpoint(0, data)
    if index > max_index:
        max_count = count 
        max_index = index

print(max_count)
    