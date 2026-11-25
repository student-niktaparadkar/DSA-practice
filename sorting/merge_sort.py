def merge(arr, left, mid, right):

    n1 = mid - left + 1
    n2 = right - mid

    a = [0] * n1
    b = [0] * n2

    for i in range(n1):
        a[i] = arr[left + i]

    for i in range(n2):
        b[i] = arr[mid + i + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:

        if a[i] <= b[j]:
            arr[k] = a[i]
            k += 1
            i += 1

        else:
            arr[k] = b[j]
            k += 1
            j += 1

    while i < n1:
        arr[k] = a[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = b[j]
        k += 1
        j += 1


def mergeSort(arr, left, right):

    if left >= right:
        return

    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)

    merge(arr, left, mid, right)


def printArray(arr, n):

    for i in range(n):
        print(arr[i], end=" ")


arr = [3, 7, 5, 8, 4, 9, 1, 6, 1]
n = len(arr)

mergeSort(arr, 0, n - 1)

printArray(arr, n)
