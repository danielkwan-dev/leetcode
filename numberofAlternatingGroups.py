class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        left = 0
        res = 0
        right = 2

        while right < len(colors):
            if colors[left] == colors[right] and colors[left+1] != colors[left]:
                res += 1
            left += 1
            right += 1        

        if colors[0] != colors[-1]:
            if colors[1] == colors[-1]:
                res += 1
            if colors[-2] == colors[0]:
                res += 1
        return res
        
        # sliding window
        # we have a fixed window size of 3, so start left at index 0 and right at index 3
        # while loop that goes until right reaches the end of the array
        # if the condition that the left and right elements are equal to each other and not equal to the middle element is true, add to count
        # after while loop, consider the case of the ends of the array
        # it'll only count if the first and last element are different colours
        # two cases: use the first two elements and the last element or use the first element and last two elements
        # check if second element is equal to the last element 
        # check if the second last element is equal to the first element