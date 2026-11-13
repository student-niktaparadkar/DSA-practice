nums = [2,2,3,1,1]

#first_approach:-
def non_repeating_num(nums):
    xor1 = 0

    for i in range(len(nums)):
        xor1 ^= nums[i]

    return xor1

print(non_repeating_num(nums))


#second_approach:-
def max_num(nums):
    larg_num = nums[0]

    for i in range(len(nums)):
        if(larg_num<nums[i]):
            larg_num = nums[i]

    return larg_num


def non_repeating_num(nums):
    list = [0]*(max_num(nums)+1)

    for i in range(len(nums)):
        list[nums[i]] += 1

    for i in range(len(nums)):
        if(list[nums[i]] == 1):
            return nums[i]


print(non_repeating_num(nums))
