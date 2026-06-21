class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 0
        longest = 0

        while left < len(nums):
            if nums[left] % 2 == 0 and nums[left] <= threshold:
                
                right = left

                while (right + 1 < len(nums) and nums[right + 1] <= threshold and nums[right] % 2 != nums[right + 1] % 2):
                    right += 1
                
                longest = max(longest, right - left + 1)

                left = right + 1
            else:
                left += 1

        return longest

        # sliding window
        # initialize left and longest variables
        # while the left pointer is less than the length of nums, first check if the element at index left is even, if not, increment left by 1 to shift window
        # if nums[left] is even, initialize the right variable to be equal to left to account for the worst case where length = 1
        # while condition where while right + 1 is less than the length of nums, nums[right + 1] is at least equal to or less than the threshold, and the condition nums[right] % 2 != nums[right +1] % 2
        # increment right by 1 until while loop breaks, then find longest length and update left 

        