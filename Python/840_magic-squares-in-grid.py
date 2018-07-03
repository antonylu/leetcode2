"""
magic-squares-in-grid
https://leetcode.com/problems/magic-squares-in-grid/description/


A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15

"""
xrange = range
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Approach #1, brute-force
        #
        # The sum of row, column and diagnoals of magic square is 15
        # The center must be 5
        #
        #  1. 2 nested for loop, 0~len(grid)-2, 0~len(grid[0])-2
        #  2. check center is 5
        #     check 9 numers are 1~9
        #     check 8 sums ||| =_ X are 15
        #
        #  O(n), 37ms
        #
        def isMagicSquare(i,j):
            # a d g
            # b e h
            # c f i
            a,b,c,d,e,f,g,h,i = grid[i][j], grid[i+1][j], grid[i+2][j], grid[i][j+1], grid[i+1][j+1], grid[i+2][j+1], grid[i][j+2], grid[i+1][j+2], grid[i+2][j+2]
            if set([a,b,c,d,e,f,g,h,i]) != set([1,2,3,4,5,6,7,8,9]):
                return False
            return a+b+c == 15 and d+e+f == 15 and g+h+i == 15 and a+d+g == 15 and b+e+h == 15 and c+f+i == 15 and a+e+i == 15 and g+e+c ==15

        ans = 0
        for i, r in enumerate(grid[:-2]):
            for j, c in enumerate(grid[i][:-2]):
                if grid[i+1][j+1] == 5:
                    if isMagicSquare(i,j):
                        ans +=1
        return ans









if __name__ == '__main__':
    s = Solution()
    tc =  [  [[4,3,8,4],[9,5,1,9],[2,7,6,2]], [[10,3,5],[1,6,11],[7,9,2]]        ]
    ans = [  1, 0]
    for i in range(len(tc)):
        r = s.numMagicSquaresInside(tc[i])
        print (r)
        assert(r == ans[i])
