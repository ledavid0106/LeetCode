class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: 
            return n
        
        a, b, c = 0, 1, 2
        
        while (n > 2):
            a, b = b, c
            c = a + b
            n = n - 1
        
        return c