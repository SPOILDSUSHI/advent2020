
def number_parse(input):
    output = input.split('-')
    return (int(output[0]), int(output[1]))

def letter_parse(input):
    return input[0]

def file_parse(f_name):
    output = []
    with open(f_name) as fr:
        for line in fr:
            number, letter, password = line.strip().split(None, 2)
            output.append((number_parse(number), letter_parse(letter), password))
    return output

def check_passwords(data):
    valid = 0
    for i in data:
        if ((i[0][0] <= i[2].count(i[1])) and (i[2].count(i[1]) <= i[0][1])):
            valid += 1
    return valid

def check_passwords2(data):
    valid = 0
    for i in data:
        if ((i[2][i[0][0] - 1] == i[1]) or (i[2][i[0][1] - 1] == i[1])):
            if i[2][i[0][0] - 1] != i[2][i[0][1] - 1]:
                valid += 1
    return valid

if __name__ == "__main__":
    print(
        'How many passwords are valid according to their policies?'
    )
    print('Each policy actually describes two positions in the password, '
        'where 1 means the first character, 2 means the second character, '
        'and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) '
        'Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.'
    )
    

    print('the number of valid passwords is for problem 1: {:d}'.format(check_passwords(file_parse('p2.txt'))))
    print('the number of valid passwords is for problem 1: {:d}'.format(check_passwords2(file_parse('p2.txt'))))