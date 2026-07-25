class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        track = {}
        found = []

        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1

            if nums[correct_index] != nums[i]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] in track:
                found.append(nums[i])
            else:
                track[nums[i]] = i
        
        return found
            
        