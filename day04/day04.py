import re
from IPython import embed

file_name = './day04.input'
with open(file_name) as f:
    content = f.read()

PASSPORTS = list(map(lambda x: dict(y.split(':') for y in x.replace('\n', ' ').split(' ')), content.split('\n\n')))

count = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = list(filter(lambda passport: all(item in passport for item in fields), PASSPORTS))

for p in valid_passports:
    byr = 1920 <= int(p['byr']) <= 2002
    iyr = 2010 <= int(p['iyr']) <= 2020
    eyr = 2020 <= int(p['eyr']) <= 2030
    if 'in' in p['hgt']:
        hgt = 59 <= int(p['hgt'].replace('in','')) <= 76
    elif 'cm' in p['hgt']:
        hgt = 150 <= int(p['hgt'].replace('cm','')) <= 193
    else:
        hgt = False
    hcl = re.fullmatch('#[0-9|a-f]{6}', p['hcl'])
    ecl = re.fullmatch('amb|blu|brn|gry|grn|hzl|oth', p['ecl'])
    pid = re.fullmatch(r'\d{9}', p['pid'])
    checks = [byr, iyr, eyr, hgt, hcl, ecl, pid]
    count += 1 if all(v for v in checks) else 0

print(len(valid_passports))
print(count)

