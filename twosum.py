class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        char_map = {}

        for i in range(len(nums)):
            second_int = target - nums[i]

            if second_int in char_map:
                return [i, char_map[second_int]]

            char_map[nums[i]] = i
        