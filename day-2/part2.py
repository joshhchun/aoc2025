import sys
import math


# playing around with generators again lol
def get_range():
    yield from map(
        lambda vals: (int(vals[0]), int(vals[1])),
        map(lambda interval: interval.split("-"), sys.stdin.readline().split(",")),
    )


def main():
    invalid_ids = set()

    for interval in get_range():
        begin, end = interval
        num_digits = int(math.log10(abs(end))) + 1
        half_digs = num_digits // 2

        # loop through all digits <= half the length of the max number
        for dig in range(10**half_digs + 1):
            curr_mult = 2
            while True:
                new_str = str(dig) * curr_mult
                new_dig = int(new_str)
                if len(new_str) > num_digits or new_dig > end:
                    break

                if begin <= new_dig <= end:
                    invalid_ids.add(new_dig)
                    curr_mult += 1
                # case that num is too small, but larger comb might work
                elif new_dig < begin:
                    curr_mult += 1

    print(sum(invalid_ids))


if __name__ == "__main__":
    main()
