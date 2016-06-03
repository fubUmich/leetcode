class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
            
        result = 1
        while n >= 3:
            result *= 3
            n -= 3
        
        if n == 2:
            result *= 2
        elif n == 1:
            result = result * 4 / 3
        
        return result