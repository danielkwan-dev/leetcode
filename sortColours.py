class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ones = 0
        twos = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            elif nums[i] == 1:
                ones += 1
            elif nums[i] == 2:
                twos += 1
        
        j = 0
        while zeroes > 0:
            nums[j] = 0
            zeroes -= 1
            j += 1


        while ones > 0:
            nums[j] = 1
            ones -= 1
            j += 1

        while twos > 0:
            nums[j] = 2
            twos -= 1
            j += 1
        
        return nums
        