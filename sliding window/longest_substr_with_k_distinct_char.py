arr = [1, 2, 1, 2, 3, 2, 2]

def k_distinct_ele(arr):
    dict = {}
    max_len =0
    left = 0

    for right in range(len(arr)):
        if arr[right] in dict:
            dict[arr[right]] += 1

        else:
            dict[arr[right]] =1

        while(len(dict)>2):
            max_len = max(max_len,right-left+1)

            dict[arr[left]] -= 1

            if(dict[arr[left]]==0):
                del dict[arr[left]]

            left += 1

    return max_len

print(k_distinct_ele(arr))

        


