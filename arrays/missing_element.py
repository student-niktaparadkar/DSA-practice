nums = [9,6,4,8,3,5,7,0,1]

#first approach:-
def missing_number(nums):
    total_sum = 0

    for i in range(1,len(nums)+1):
        total_sum += i

    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

    missing_num = total_sum - sum

    return missing_num

print(missing_number(nums))


#second approach:-
def missing_value(nums):
    xor1 = 0

    for i in range(1,len(nums)+1):
        xor1 ^= i

    xor2 = 0

    for i in range(len(nums)):
        xor2 ^= nums[i]


    xor3 = xor1 ^ xor2

    return xor3

print(missing_value(nums))
