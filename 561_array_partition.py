class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        sum = 0
        for i in range(0, len(sorted_nums), 2):
            sum += sorted_nums[i]
        
        return sum