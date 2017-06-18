class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        hash = dict()
        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for num in findNums:
            index = hash[num]
            res.append(self.search(nums, index, num))
        
        return res
    
    def search(self, nums, startIndex, target):
        for i in range(startIndex, len(nums)):
            if nums[i] > target:
                return nums[i]
        
        return -1