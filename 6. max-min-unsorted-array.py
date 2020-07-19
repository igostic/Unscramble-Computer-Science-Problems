import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if ints is None or len(ints) == 0:
        print('Invalid input:', ints)
        return float('inf'), float('-inf')

    min_found = ints[0]
    max_found = ints[0]

    for item in ints:
        if item < min_found:
            min_found = item

        if item > max_found:
            max_found = item

    return min_found, max_found


if __name__ == '__main__':
    test1 = [i for i in range(0, 10)]
    random.shuffle(test1)
    print("Pass" if ((0, 9) == get_min_max(test1)) else "Fail")

    test2 = [i for i in range(0, 100)]
    random.shuffle(test2)
    print("Pass" if ((0, 99) == get_min_max(test2)) else "Fail")

    test3 = [i for i in range(0, 1000)]
    random.shuffle(test3)
    print("Pass" if ((0, 999) == get_min_max(test3)) else "Fail")

    # Edge cases
    print("Pass" if ((-9, 0) == get_min_max([i for i in range(0, -10, -1)])) else "Fail")
    print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
    print("Pass" if ((float('inf'), float('-inf')) == get_min_max([])) else "Fail")
    print("Pass" if ((float('inf'), float('-inf')) == get_min_max(None)) else "Fail")
    print("Pass" if ((-100, 99) == get_min_max([i for i in range(-100, 100)])) else "Fail")
