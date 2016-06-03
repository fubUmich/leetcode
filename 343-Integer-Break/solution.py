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
        while n > 4:
            result *= 3
            n -= 3
            
        result *= n
        
        return result