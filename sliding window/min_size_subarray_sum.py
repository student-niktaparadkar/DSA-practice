nums = [2,3,1,2,4,3]
target = 7


def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum =0
        min_len =float('inf')

        left =0
        right =0
        while(right<len(nums)):
            sum += nums[right]

            while(sum >= target):
                min_len = min(min_len,right-left+1)

                sum -= nums[left]

                left += 1

            right += 1

        if(min_len == float('inf')):
            return 0

        return min_len

            

