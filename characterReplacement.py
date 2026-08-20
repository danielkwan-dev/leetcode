class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        max_len = 0
        max_freq = 0
        seen = {}

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            max_freq = max(max_freq, seen[s[i]])
            
            while (i - left + 1 - max_freq)  > k:
                seen[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, i - left + 1)
        
        return max_len