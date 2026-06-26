class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        max_len = 0
        sort = nums.sort()

        for i in range(len(nums)):
            while nums[i] - nums[left] > 1:
                left += 1
            if nums[i] - nums[left] == 1:
                max_len = max(max_len, i - left + 1)

            
        return max_len
            
        # sort the array since the biggest and smallest numbers will always be at the ends of the window
        # initialize left variable which increments while the difference is greater than 1
        # once the difference is exactly 1, find the max between the current window size and current max_len

        