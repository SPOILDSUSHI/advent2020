import re

def byr_parse(input):
    if ((int(input) >= 1920) and (int(input) <= 2002)):
        return True
    return False

def iyr_parse(input):
    if ((int(input) >= 2010) and (int(input) <= 2020)):
        return True
    return False

def eyr_parse(input):
    if ((int(input) >= 2020) and (int(input) <= 2030)):
        return True
    return False

def hgt_parse(input):
    if 'cm' in input:
        if ((int(input.split('cm')[0]) >= 150) and (int(input.split('cm')[0]) <= 193)):
            return True
    else:
        if ((int(input.split('in')[0]) >= 59) and (int(input.split('in')[0]) <= 76)):
            return True
    return False

def hcl_parse(input):
    if re.search(r'\#[0-9a-f]{6}', input):
        return True
    return False

def ecl_parse(input):
    if (
        ('amb' == input) or\
        ('blu' == input) or\
        ('brn' == input) or\
        ('gry' == input) or\
        ('grn' == input) or\
        ('hzl' == input) or\
        ('oth' == input)
    ):
        return True
    return False

def pid_parse(input):
    if re.search(r'[0-9]{9}', input):
        if len(input) == 9:
            return True
    return False

def file_parse2(f_name):     
    valid = 0
    temp_line = ''
    with open(f_name, 'r') as fr:
        for line in fr:
            if line != '\n':
                temp_line += line.rstrip() + ' '
            else:
                try:
                    s = temp_line.split('byr:')
                    byr = s[1].split(None, 1)[0]

                    s = temp_line.split('iyr:')
                    iyr = s[1].split(None, 1)[0]

                    s = temp_line.split('eyr:')
                    eyr = s[1].split(None, 1)[0]

                    s = temp_line.split('hgt:')
                    hgt = s[1].split(None, 1)[0]

                    s = temp_line.split('hcl:')
                    hcl = s[1].split(None, 1)[0]

                    s = temp_line.split('ecl:')
                    ecl = s[1].split(None, 1)[0]

                    s = temp_line.split('pid:')
                    pid = s[1].split(None, 1)[0]

                except IndexError:
                    byr = False
                    iyr = False
                    eyr = False
                    hgt = False
                    hcl = False
                    ecl = False
                    pid = False
                if (
                    (byr_parse(byr)) and\
                    (iyr_parse(iyr)) and\
                    (eyr_parse(eyr)) and\
                    (hgt_parse(hgt)) and\
                    (hcl_parse(hcl)) and\
                    (ecl_parse(ecl)) and\
                    (pid_parse(pid))
                ):
                    valid += 1
                temp_line = ''
    return valid

def file_parse(f_name):     
    valid = 0
    temp_line = ''
    with open(f_name, 'r') as fr:
        for line in fr:
            if line != '\n':
                temp_line += line.rstrip() + ' '
            else:
                if (
                    ('byr:' in temp_line) and\
                    ('iyr:' in temp_line) and\
                    ('eyr:' in temp_line) and\
                    ('hgt:' in temp_line) and\
                    ('hcl:' in temp_line) and\
                    ('ecl:' in temp_line) and\
                    ('pid:' in temp_line)
                ):
                    valid += 1
                temp_line = ''
    return valid

if __name__ == "__main__":
    print(
        'Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?'
    )

    print('the number of valid Passports for problem 1: {:d}'.format(file_parse('p4.txt')))
    print('the number of valid Passports for problem 2: {:d}'.format(file_parse2('p4.txt')))
