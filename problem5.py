
def parse_row(data):
    num = ''
    for c in data:
        if c == 'F':
            num += '0'
        else:
            num += '1'
    return num

def parse_seat(data):
    num = ''
    for c in data:
        if c == 'L':
            num += '0'
        else:
            num += '1'
    return num

def parse_file(f_name):
    seat_id = 0
    with open(f_name, 'r') as fr:
        for line in fr:
            row = parse_row(line[0:7])
            seat = parse_seat(line[7:10])
            if (int(row, base=2) * 8 + int(seat, base=2)) > seat_id:
                seat_id = int(row, base=2) * 8 + int(seat, base=2)
    return seat_id

def parse_file2(f_name):
    seat_id = list(range(1, parse_file(f_name) + 1))
    with open(f_name, 'r') as fr:
        for line in fr:
            row = parse_row(line[0:7])
            seat = parse_seat(line[7:10])
            seat_id.remove(int(row, base=2) * 8 + int(seat, base=2))
    return seat_id

def clean_list(data):
    for index, num in enumerate(data):
        if num + 1 != data[index + 1]:
            return data[index + 1]


if __name__ == "__main__":
    print(
        'As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?'
    )

    print('the highest seat ID on a boarding pass for problem 1: {:d}'.format(parse_file('p5.txt')))
    print('the seat ID for problem 2: {:d}'.format(clean_list(parse_file2('p5.txt'))))