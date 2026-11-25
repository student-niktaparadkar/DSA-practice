def partition(arr, left, right):

    pivot = arr[left]

    i = left - 1
    j = right + 1

    while True:

        # Move i until an element >= pivot is found
        while True:
            i += 1
            if arr[i] >= pivot:
                break

        # Move j until an element <= pivot is found
        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr, left, right):

    if left >= right:
        return

    part = partition(arr, left, right)

    quickSort(arr, left, part)
    quickSort(arr, part + 1, right)


def printArray(arr, n):

    for i in range(n):
        print(arr[i], end=" ")


arr = [2, 7, 4, 8, 5, 1, 5, 7, 3, 6]
n = len(arr)

quickSort(arr, 0, n - 1)

printArray(arr, n)
