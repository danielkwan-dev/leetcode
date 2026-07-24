class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[correct_index] != nums[i]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        
        return result
        