def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = nums[0]
        for i in range(1,k):
            max_sum += nums[i]

        curr_sum = max_sum
        for i in range(k,len(nums)):
            curr_sum += nums[i]

            curr_sum -= nums[i-k]

            max_sum = max(curr_sum,max_sum)

        return max_sum/k
