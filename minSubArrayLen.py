class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        min_length = len(nums) + 1
        curr_length = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            while curr_sum >= target:
                curr_length = i - left + 1

                if min_length > curr_length:
                    min_length = curr_length
                curr_sum -= nums[left]
                left += 1                
            
        if min_length <= len(nums):
            return min_length
        return 0
            
            
# sliding window
# define left pointer, and keep track of current length, sum and min length
# loop through, add the current element to curr_sum, when the current sum is above or equal to the target (while loop), find the current length using i - left + 1 (size of window). 
# if the current length is less than min length, set min length to the current length
# remove the left most element from the curr_sum and loop until curr_sum is less than target
# if min length is at least equal or smaller to len(nums), return min length, otherwise return 0.