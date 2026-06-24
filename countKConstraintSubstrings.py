class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        count = [0, 0]
        res = 0

        for i in range(len(s)):
            count[int(s[i])] += 1

            while (count[0] > k and count[1] > k):
                count[int(s[left])] -= 1
                left += 1
            res += i - left + 1

        return res

        # since we're only looking at 0s and 1s, create a list that has two elements with count starting at 0
        # 0th index represents 0, 1 index represents 1s
        # add 1 to the count depending on what number is seen
        # create while loop that runs when both the counts are > k
        # decerement the element at the left position from count and increment left by 1
        # result is the number of substrings which will be i - left + 1 for every iteration


                


        