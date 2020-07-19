from algorithms import quicksort


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        print('Input list must have a length greater than 2')
        return input_list

    quicksort(input_list)  # O(nlogn)
    first, second = '', ''
    for i in range(len(input_list) - 1, -1, -2):
        first += str(input_list[i])
        if i - 1 >= 0:
            second += str(input_list[i - 1])

    # print(first, second)
    return [int(first), int(second)]  # O(n + nlogn) --> O(nlogn)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[1], [1]])
    test_function([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [97531, 86420]])
