class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if ((nums[left] ** 2) >= (nums[right] ** 2)):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        return res
        