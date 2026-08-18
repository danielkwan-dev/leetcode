class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        min_index = 0
        max_index = len(nums) - 1

        while min_index <= max_index:
            middle = (min_index + max_index ) // 2
            if nums[middle] < target:
                min_index = middle + 1
            elif nums[middle] > target:
                max_index = middle - 1
            else:
                return middle
            
        return -1
            
            

        