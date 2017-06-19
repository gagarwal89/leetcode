class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        res = 0
        for num in nums:
            if num == 1:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 0
        
        return res