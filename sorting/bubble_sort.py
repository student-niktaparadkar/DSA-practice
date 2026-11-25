def bubbleSort(arr, n):

    for i in range(n - 1):

        flag = True

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False

        # Optimized Bubble Sort
        if flag == True:
            break


def printArray(arr, n):

    for i in range(n):
        print(arr[i], end=" ")


arr = [2, 6, 4, 7, 9, 8]
n = len(arr)

bubbleSort(arr, n)
printArray(arr, n)
