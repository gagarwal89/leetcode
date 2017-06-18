class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = dict()
        for index in range(len(nums)):
            hash[nums[index]] = index
        
        for index in range(len(nums)):
            diff = target-nums[index]
            if hash.get(diff) and hash[diff] != index:
                return [index, hash[diff]]
        
        return None