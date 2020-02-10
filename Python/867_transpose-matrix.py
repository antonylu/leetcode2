"""
transpose-matrix

https://leetcode.com/problems/transpose-matrix/

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach #3, copy in place
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
        
        
        # Approach #2, brute force
        row_no    = len(A)
        column_no = len(A[0])
        ans       = []
        for i in range(column_no): #3
            row = []
            for j in range(row_no): #2
                row.append(A[j][i])
            ans.append(row)
        return ans

        # Approach #1, use numpy 
        #
        import numpy as np
        return np.array(A).transpose().tolist()
                
        


if __name__ == '__main__':
    s = Solution()
    tc =  ([[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6]])
    ans = ([[1,4,7],[2,5,8],[3,6,9]], [[1,4],[2,5],[3,6]])
    for i in range(len(tc)):
        r = s.transpose(tc[i])
        print (r)
        assert(r == ans[i])
