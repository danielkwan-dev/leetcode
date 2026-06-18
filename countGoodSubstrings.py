class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)-2):
            window = s[i:i+3]
            if len(set(window)) == 3:
                res += 1
            
        
        return res

        # counter res, loop until len(s) - 2 since we're looking at substring length 3
        # have a window size 3 from i to i+3. convert it to a set to remove duplicates and if the length of it is 3 we know it's a good substring.
        