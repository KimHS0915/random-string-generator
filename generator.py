import random
import sys


def get_args(argv, default2, default3, default4):
    arg2 = default2
    arg3 = default3
    arg4 = default4
    if len(argv) > 4:
        arg4 = argv[4]
    if len(argv) > 3:
        arg3 = argv[3]
    if len(argv) > 2:
        arg2 = argv[2]
    return int(arg2), int(arg3), int(arg4)


def generate_str(argv):
    import string

    length, letters, _ = get_args(argv, 100, 1, 0)
    if letters not in range(4):
        print('arg error')
        sys.exit()
    dict = {
        0: string.printable,
        1: string.ascii_letters + string.digits,
        2: string.ascii_letters,
        3: string.digits,
    }
    letters = dict[letters]
    return ''.join(random.choices(letters, k=length))


def make_int_lst(min, max):
    if min < 0:
        min = -min
        negative = range(1, min)
        negative = [-i for i in negative]
        positive = list(range(0, max))
        return negative + positive
    else:
        return list(range(min, max))


def generate_int(argv):
    length, min, max = get_args(argv, 100, -100, 100)
    if length >= max - min:
        print('arg error')
        sys.exit()
    lst = make_int_lst(min, max)
    result = random.sample(lst, k=length)
    result = [str(i) for i in result]
    return ' '.join(result)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('no arg')
        sys.exit()
    if sys.argv[1] == 'str':
        result = generate_str(sys.argv)
    elif sys.argv[1] == 'int':
        result = generate_int(sys.argv)
    else:
        print('arg error')
        sys.exit()
    print(result)
