import sys
import math


# playing around with generators again lol
def get_range():
    yield from map(
        lambda vals: (int(vals[0]), int(vals[1])),
        map(lambda interval: interval.split("-"), sys.stdin.readline().split(",")),
    )


def main():
    invalid_ids = []

    for interval in get_range():
        begin, end = interval
        num_digits = int(math.log10(abs(end))) + 1
        half_digs = num_digits // 2

        for dig in range(begin, end + 1):
            dig_len = int(math.log10(dig)) + 1
            str_dig = str(dig)
            if dig_len % 2 or dig_len // 2 > half_digs:
                continue

            if str_dig[: dig_len // 2] == str_dig[dig_len // 2 :]:
                invalid_ids.append(dig)

    print(sum(invalid_ids))


if __name__ == "__main__":
    main()
