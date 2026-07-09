class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        left = 0
        curr_product = 1
        res = 0 

        for i in range(len(nums)):
            curr_product *= nums[i]

            while curr_product >= k:
                curr_product //= nums[left]
                left += 1
            
            res += i - left + 1
        
        return res