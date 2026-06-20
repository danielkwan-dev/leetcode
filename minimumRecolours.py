class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        left = 0
        curr_count = 0
        min_count = len(blocks)
        
        for i in range(len(blocks)):
            if blocks[i] == "W":
                curr_count += 1
            if i - left + 1 == k:
                min_count = min(min_count, curr_count)
                if blocks[left] == "W":
                    curr_count -= 1
                left += 1
        return min_count

        # sliding window. initialitze left pointer and a current and min count.
        # if the current element is white, that is one operation needed so add to the current count
        # if the size of the window (i - left + 1) is equal to k, it's time to shift the window
        # update min_count and if the colour at position "left" is white, remove 1 from curr_count
        # add 1 to left as we shift the window.
            
        