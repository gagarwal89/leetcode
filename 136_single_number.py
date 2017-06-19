class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]

        return xor