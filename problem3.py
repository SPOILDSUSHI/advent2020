
def file_parse(f_name):
    with open('p3temp.txt', 'r') as fr:     
        with open(f_name, 'w') as fw:
            for index, line in enumerate(fr):
                while len(line.rstrip()) < index * 7:
                    line = line.rstrip()
                    line += line
                fw.write(line.rstrip() + '\n')

def sled(f_name, num_right, num_down):
    trees = 0
    with open(f_name, 'r') as fr:
        for index, line in enumerate(fr):
            if ((index % num_down == 0) and (line[int(index / num_down) * num_right] == '#')):
                trees += 1
    return trees


if __name__ == "__main__":
    print('Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?')

    # file_parse('p3.txt')    
    sled1 = sled('p3.txt', 1, 1)
    sled3 = sled('p3.txt', 3, 1)
    sled5 = sled('p3.txt', 5, 1)
    sled7 = sled('p3.txt', 7, 1)
    sled12 = sled('p3.txt', 1, 2)

    print('the number of trees for problem 1: {:d}'.format(sled3))
    print('the number of trees for problem 2 right 1: {:d}'.format(sled1))
    print('the number of trees for problem 2 right 3: {:d}'.format(sled3))
    print('the number of trees for problem 2 right 5: {:d}'.format(sled5))
    print('the number of trees for problem 2 right 7: {:d}'.format(sled7))
    print('the number of trees for problem 2 right 1 down 2: {:d}'.format(sled12))
    print('the number of trees for problem 2 all multiplied is: {:d}'.format(sled1 * sled3 * sled5 * sled7 * sled12))
