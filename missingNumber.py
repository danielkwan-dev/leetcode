class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        
        while i < len(nums):
            correct_index = nums[i] 
            if correct_index < len(nums) and nums[i] != nums[correct_index]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        

        
                
            
        