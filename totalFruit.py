class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        curr_len = 0
        max_len = 0
        seen = {}

        for i in range(len(fruits)):
            if fruits[i] not in seen:
                seen[fruits[i]] = 1
            else:
                seen[fruits[i]] += 1
            
            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                curr_len -= 1
                left += 1

            curr_len += 1
            max_len = max(max_len, curr_len)
    
        return max_len


            


        