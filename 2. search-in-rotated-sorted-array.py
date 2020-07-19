from algorithms import linear_search, binary_search


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1

    pivot_idx = find_pivot(input_list, 0, len(input_list) - 1)  # O(logn)
    if pivot_idx == len(input_list) - 1:
        return binary_search(input_list, 0, len(input_list) - 1, number)  # O(logn)
    elif input_list[0] <= number <= input_list[pivot_idx]:
        input_list = input_list[:pivot_idx + 1]
        return binary_search(input_list, 0, len(input_list) - 1, number)  # O(logn)
    elif number > input_list[-1]:
        return -1
    else:
        input_list = input_list[pivot_idx + 1:]
        return pivot_idx + 1 + binary_search(input_list, 0, len(input_list) - 1, number)  # O(logn)


def find_pivot(array, left_idx, right_idx):
    if right_idx == left_idx:
        return left_idx  # right_idx

    mid_idx = (left_idx + right_idx) // 2

    left = array[left_idx]
    mid = array[mid_idx]

    if mid > array[mid_idx + 1]:  # 3, ''4'', 1 ...
        return mid_idx
    if mid < array[mid_idx - 1]:  # ''3'', 1, 2
        return mid_idx - 1

    if left > mid:  # 3, ''4'', 0, 1, 2,   --> 3 > 0 --> pivot is in between
        return find_pivot(array, left_idx, mid_idx)  # pivot is before mid_idx
    # 2, 3, 4, ''5'', 1   --> 4 > 1 ---> pivot is in between
    return find_pivot(array, mid_idx + 1, right_idx)  # pivot is after mid_idx


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[3, 4, 5, 1, 2], 1])
    test_function([[1, 2, 3, 4, 5, 6], -1])
    test_function([[1, 2, 3, 4, 5, 6], 7])
    test_function([[], 7])
