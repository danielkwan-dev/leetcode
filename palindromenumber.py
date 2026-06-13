class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        return num == num[::-1]

        # convert num to str and check if it's reverse ([::-1]) is equal