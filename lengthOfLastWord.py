class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splitList = s.split()
        return len(splitList[-1])

        # split the list using the split() function which creates a list of the words separated by spaces and removes trailing/leading/multiple spaces
        # return the last item of the list which is the last word