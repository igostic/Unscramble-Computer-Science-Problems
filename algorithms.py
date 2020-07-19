# Linear search
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# Binary search
def binary_search(array, left_idx, right_idx, target):
    mid_idx = (left_idx + right_idx) // 2
    mid = array[mid_idx]

    if mid == target:
        return mid_idx
    elif left_idx == right_idx:
        return -1
    elif mid < target:
        return binary_search(array, mid_idx + 1, right_idx, target)
    return binary_search(array, left_idx, mid_idx, target)


# Quicksort
def quicksort(array):
    sort(array, 0, len(array) - 1)


def sort(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while right_idx >= left_idx:
        pivot = array[pivot_idx]
        left = array[left_idx]
        right = array[right_idx]

        if left > pivot:
            swap(array, left_idx, right_idx)

        if left <= pivot:
            left_idx += 1
        if right >= pivot:
            right_idx -= 1

    swap(array, pivot_idx, right_idx)
    sort(array, start_idx, right_idx - 1)
    sort(array, pivot_idx + 1, end_idx)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
