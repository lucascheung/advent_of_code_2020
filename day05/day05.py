file_name = './day05.input'
with open(file_name) as f:
    content = f.readlines()

SEATS = [x.strip() for x in content]

all_passes = []

for seat in SEATS:
    row_start = 0
    row_end = 127
    column_start = 0
    column_end = 7
    row = seat[:7]
    col = seat[7:]
    for r in row[:6]:
        if r == "F":
            row_end = (row_start + row_end) // 2
        else:
            row_start = (row_start + row_end) // 2 + 1

    f_r = row_start if row[6] == "F" else row_end
    for c in col[:2]:
        if c == "L":
            column_end = (column_start + column_end) // 2
        else:
            column_start = (column_start + column_end) // 2 + 1
    f_c = column_start if col[2] == "L" else column_end
    all_passes.append(f_r * 8 + f_c)
    
print(max(all_passes))

for x in range(min(all_passes), max(all_passes)):
    print(x) if x not in all_passes else None