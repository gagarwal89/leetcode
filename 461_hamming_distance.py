class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        res = 0
        while xor != 0:
            if xor & 1 == 1:
                res += 1
            xor = xor >> 1
        
        return res