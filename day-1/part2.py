import sys

START_NUM = 50
MAX_NUM = 100


def read_input():
    for line in sys.stdin:
        yield (line[0], int(line[1:]))


def calc_cycles(first_click, num) -> int:
    if not first_click:
        return num // MAX_NUM
    elif first_click <= num:
        return 1 + ((num - first_click) // MAX_NUM)
    return 0


def main():
    curr_num = START_NUM
    res = 0

    for dir, num in read_input():
        if dir == "R":
            first_click = (MAX_NUM - curr_num) % MAX_NUM
            res += calc_cycles(first_click, num)
            curr_num = (curr_num + num) % MAX_NUM
        elif dir == "L":
            first_click = curr_num % 100
            res += calc_cycles(first_click, num)
            curr_num = (curr_num - num) % MAX_NUM

    print(res)


if __name__ == "__main__":
    main()
