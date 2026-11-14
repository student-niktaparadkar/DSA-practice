nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_subarray(nums,k):
    max_sum = 0
    for i in range(k):
        max_sum += nums[i]

    curr_sum = max_sum
    for i in range(k,len(nums)):
        curr_sum += nums[i]

        curr_sum -= nums[i-k]

        max_sum = max(max_sum,curr_sum)

    return max_sum

print(max_sum_subarray(nums,k))
