class Solution(object):
    def maxSubArray(self, nums):
        left = 0
        max_sum = nums[0]
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum
            
            if curr_sum < 0:
                curr_sum = 0
                left = i + 1
        
        return max_sum