arr = [10, 20, 10, 30, 40, 20, 50, 30, 60]

def reverse_array(arr):
    i = 0
    j = len(arr)-1
    
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

        j -= 1

    return arr

rev_arr = reverse_array(arr)
print(rev_arr)
