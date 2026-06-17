class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        left = 0

        for i in range(len(nums)):
            if i - left > k:
                window.remove(nums[left])
                left += 1
            if nums[i] in window:
                return True
            window.add(nums[i])

        return False

        # create a hashset to keep track of values within the window
        # we have a defined window size k (i-k), so if i-k ever exceeds k, we need to remove the leftmost element from the set and move the window to the right
        # if we ever find an element in the hashset, we found a duplicate within the window
        # otherwise return false