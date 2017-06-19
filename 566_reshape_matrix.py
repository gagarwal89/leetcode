class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        if r * c != len(nums) * len(nums[0]):
            return nums

        res = [[None] * c for i in range(r)]
        resRow = 0
        resCol = 0
        for rowIndex in range(len(nums)):
            for colIndex in range(len(nums[rowIndex])):
                if resCol == c:
                    resCol = 0
                    resRow += 1

                res[resRow][resCol] = nums[rowIndex][colIndex]
                resCol += 1
        
        return res