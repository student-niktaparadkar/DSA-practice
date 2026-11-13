nums = [3,3]
target = 6

#brut force:-
def two_sum(nums,target):
    for i in range(len(nums)):
       sum = nums[i]
       for j in range(i+1,len(nums)):
          sum += nums[j]
          if(sum == target):
             return i,j

    return -1,-1

print(two_sum(nums,target))


#optimal approach:-
def two_sum(nums,target):
    dict = {}

    list1 = []

    for i in range(len(nums)):
        first = nums[i]
        sec = target-first

        if(sec in dict):
            list1.append(i)
            list1.append(dict[sec])

            return i,dict[sec]
            
        dict[first] = i

    return -1,-1

ans = two_sum(nums,target)
print(ans)
             
