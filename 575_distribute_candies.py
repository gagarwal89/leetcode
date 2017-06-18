class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sisterCandies = dict()
        for candy in candies:
            sisterCandies[candy] = True
        
        return min(len(sisterCandies), len(candies)/2)