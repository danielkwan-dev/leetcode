class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
            
        return k
        
        # have it start at index 1 since the first element will start off unique
        # i is the reader, k is the writer
        # if nums[i] is not equal to nums[k], that means it's not duplicates, so we can overwrite the 
        # element at nums[k] with nums[i] and increment k
        # this works since we only look for unique and we skip duplicates, k only gets incremented if we see unique, so it will be at the right position to overwrite as it is always <= i.