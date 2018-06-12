"""
https://leetcode.com/problems/reshape-the-matrix/description/

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]

Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.


Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]

 Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Approach #1, brute-force
        # check validality first
        # rearrange the 2D list to 1D
        # rearrange 1D to 2D
        #
        # O(n), 97%

        R = len(nums)
        C = len(nums[0])
        if r*c != R*C: return nums
        a = []
        for i in range(R):
            a.extend(nums[i])
        ans = []
        # [1,2,3,4]
        # [1,2],[3,4]
        # [0:2],[2:4]
        for j in range(r):
            start = j*c
            ans.append(a[start:start+c])
        return ans


if __name__ == '__main__':
    s = Solution()
    tc  = [ ([[1,2],[3,4]],1,4),([[1,2],[3,4]],2,4) ]
    ans = [ [[1,2,3,4]], [[1,2],[3,4]] ]

    for i in range(len(tc)):
        r = s.matrixReshape(tc[i][0],tc[i][1],tc[i][2])
        print (r)
        assert(r == ans[i])
