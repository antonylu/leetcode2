"""
https://leetcode.com/problems/island-perimeter/description/

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # approach #1, brute-force
        # 
        # every 1 has 4 edges, if the adjacent number is 0 or not exist, edge +1
        # accumulate for every 1
        #
        # O(n) 28%
        ans = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    if j == 0   or grid[i][j-1] == 0: ans +=1 # Left
                    if i == 0   or grid[i-1][j] == 0: ans +=1 # Up
                    if j == w-1 or grid[i][j+1] == 0: ans +=1 # Right
                    if i == h-1 or grid[i+1][j] == 0: ans +=1 # Down
        return ans


if __name__ == '__main__':
    s = Solution()
    tc = [[0,1,0,0], \
          [1,1,1,0], \
          [0,1,0,0], \
          [1,1,0,0]]
    an = 16
#    for i in range(len(tc)):
    print(s.islandPerimeter(tc))
    #assert(s.islandPerimeter(tc) == an)
