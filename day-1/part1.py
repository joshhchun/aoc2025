import sys

START_NUM = 50
MAX_NUM = 100


def read_input():
    for line in sys.stdin:
        yield (line[0], int(line[1:]))


def main():
    curr_num = START_NUM
    res = 0

    for dir, num in read_input():
        if dir == "R":
            curr_num = (curr_num + num) % MAX_NUM
        elif dir == "L":
            curr_num = (curr_num - num) % MAX_NUM

        if not curr_num:
            res += 1

    print(res)


if __name__ == "__main__":
    main()
