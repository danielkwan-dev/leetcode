class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        res = 0
        num_copy = num

        while num_copy >= 10**(k-1):
            divisor = num_copy % 10**k
            num_copy = num_copy // 10
            if divisor != 0:
                if num % divisor == 0:
                    res += 1
        
        return res

        # make a copy of num since we will be altering it and we need to check the condiiton of whether the k digits are factors of num.
        # have a while loop running while the number of digits of the num_copy is greater than or equal to the target digits k
        # in the loop, we find the divisor to be the last k digits of num
        # remove the last digit of num
        # check if divisor is not 0 (so we dont do division by 0), and check if it is divisible, if so, add to result.  
