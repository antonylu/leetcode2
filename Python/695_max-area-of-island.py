"""
https://leetcode.com/problems/max-area-of-island/description/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Approach #1, DFS with seen table
        #
        # DFS to search connected land 4-directionally
        #
        #               (r-1,c)
        #       (r,c-1)    1    (r,c+1)
        #               (r+1,c)
        #
        # mark 0 as seen
        # time : O(n), n = r*c, 45%
        # space: O(l), l = number of lands
        def dfs(r,c):
            if 0<= r < R and 0<=c <C and grid[r][c]:
                grid[r][c] = 0
                return (1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1) )
            else:
                return 0

        R = len(grid)
        C = len(grid[0])
        lands = [0]

        for i in range(R):
            for j in range(C):
                land = dfs(i,j)
                if land > 0: lands.append(land)

        return max(lands)


if __name__ == '__main__':
    s = Solution()
    tc  = [[ \
 [0,0,1,0,0,0,0,1,0,0,0,0,0], \
 [0,0,0,0,0,0,0,1,1,1,0,0,0], \
 [0,1,1,0,1,0,0,0,0,0,0,0,0], \
 [0,1,0,0,1,1,0,0,1,0,1,0,0], \
 [0,1,0,0,1,1,0,0,1,1,1,0,0], \
 [0,0,0,0,0,0,0,0,0,0,1,0,0], \
 [0,0,0,0,0,0,0,1,1,1,0,0,0], \
 [0,0,0,0,0,0,0,1,1,0,0,0,0]], \
 [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]], \
 [[0]] \
 ]

    ans = [ 6,4,0 ]


    for i in range(len(tc)):
        r = s.maxAreaOfIsland(tc[i])
        print (r)
        assert(r == ans[i])
