nums = [1,0,1,1,0,1]

def max_consecutive_ones(nums):
    max_ones = 0
    curr_ones = 0

    for i in range(len(nums)):
        if(nums[i]==1):
            curr_ones += 1
            max_ones = max(curr_ones,max_ones)

        elif(nums[i]==0):
            curr_ones =0

    return max_ones

print(max_consecutive_ones(nums))
