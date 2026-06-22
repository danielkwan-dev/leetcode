class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        char_map = {}
        max_len = 0

        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = 1
            else:
                char_map[s[i]] += 1
            while char_map[s[i]] > 2:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1

            max_len = max(max_len, i - left + 1)
        return max_len

        # sliding window pattern
        # idea: create dictionary that keeps track of the frequencies of the characters
        # if the frequency of a character ever exceeds 2, we need to shift the window so remove the element at the "left" position and increment left. 
        # find max len by finding max between the latest max_len and the window size (i - left + 1)
        
        