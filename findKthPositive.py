class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        for i in range(len(arr)):
            missing = arr[i] - (i+1)
            if missing >= k:
                return k+i
        
        return len(arr) + k
        