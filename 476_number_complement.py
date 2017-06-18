class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        placeValue = 0
        while num != 0:
            if num & 1 == 0:
                res += pow(2, placeValue)
            
            placeValue += 1
            num = num >> 1
        
        return res