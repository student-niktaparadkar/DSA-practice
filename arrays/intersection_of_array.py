arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 2, 3, 5, 6]

def intersection(arr1,arr2):
    arr3 = []

    i=0
    j=0

    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]<arr2[j]):
            i += 1

        elif(arr2[j]<arr1[i]):
            j += 1

        else:
            arr3.append(arr1[i])
            i += 1
            j += 1

    return arr3


ans = intersection(arr1,arr2)
print(ans)
