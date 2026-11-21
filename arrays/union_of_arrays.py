arr1 = [1, 2, 3, 4, 6]
arr2 = [2, 3, 5, 7]

def union_array(arr1,arr2):
    arr3 = []
    i =0
    j =0

    while(i<len(arr1) and j<len(arr2)):
        if(i==0 or arr1[i] == arr1[i-1]):
            i += 1

        if(j==0 or arr2[j] == arr2[j-1]):
            j += 1

        if(arr1[i]<arr2[j]):
            arr3.append(arr1[i])
            i += 1

        elif(arr2[j]<arr1[i]):
            arr3.append(arr2[j])
            j += 1

        else:
            arr3.append(arr1[i])

            i += 1
            j += 1

    while(i<len(arr1)):
        if(arr1[i] != arr1[i-1]):
            arr3.append(arr1[i])

            i += 1

    while(j<len(arr2)):
        if(arr2[j] != arr2[j-1]):
            arr3.append(arr2[j])

            j += 1

    return arr3

ans = union_array(arr1,arr2)

print(ans)
