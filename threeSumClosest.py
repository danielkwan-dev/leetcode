class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = nums[0] + nums[1] + nums[2]
        nums.sort()

       

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return total
                
                if abs(target - total) <= abs(target - res):
                    res = total
                if total <= target:
                    left += 1
                else:
                    right -= 1
        return res

                
 
        