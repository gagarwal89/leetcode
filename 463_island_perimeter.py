class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[rowIndex])):
                if grid[rowIndex][colIndex] == 1:
                    # Top
                    if rowIndex-1<0 or grid[rowIndex-1][colIndex] == 0:
                        perimeter += 1
                    
                    # Bottom
                    if rowIndex+1>=len(grid) or grid[rowIndex+1][colIndex] == 0:
                        perimeter += 1

                    # Left
                    if colIndex-1<0 or grid[rowIndex][colIndex-1] == 0:
                        perimeter += 1

                    # Right
                    if colIndex+1>=len(grid[rowIndex]) or grid[rowIndex][colIndex+1] == 0:
                        perimeter += 1
        
        return perimeter