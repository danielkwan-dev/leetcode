class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_index = 0
        max_index = len(nums) - 1
        middle = max_index // 2
        
        while min_index <= max_index:
            middle = (max_index + min_index) // 2
            if target > nums[middle]:
                min_index = middle + 1
            elif target < nums[middle]:
                max_index = middle - 1
            elif target == nums[middle]:
                return middle
            
        return min_index
        