class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        mincut = [i for i in xrange(-1, n)]
        
        for i in xrange(n):
            for j in range(min(i+1, n-i)):
                if s[i-j] != s[i+j]:
                    break
                mincut[i+j+1] = min(mincut[i+j+1], mincut[i-j]+1)
                
            for j in range(1, min(i+2, n-i)):
                if s[i-j+1] != s[i+j]:
                    break
                mincut[i+j+1] = min(mincut[i+j+1], mincut[i-j+1] + 1)
        
        return mincut[n]
                