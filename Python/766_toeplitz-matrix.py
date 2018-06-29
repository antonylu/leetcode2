"""
https://leetcode.com/problems/toeplitz-matrix/description/

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?

"""
xrange = range
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Approach #2, brute-force
        #
        # compare len(matrix) - 1 times
        #   compare matrix[0][:len-1] with matrix[1][1:]
        #   compare char by char
        #  example:
        #   [1,2,3,4],      \
        #   [5,1,2,3],      \
        #   [9,5,1,2]       \
        # compare [1,2,3]
        # compare [5,1,2]
        #
        # O(n), 10%
        for i in xrange(len(matrix)-1):
            for j in xrange(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]: return False
        return True

        # Approach #1, brute-force
        #
        # compare len(matrix) - 1 times
        #   compare matrix[0][:len-1] with matrix[1][1:]
        #  example:
        #   [1,2,3,4],      \
        #   [5,1,2,3],      \
        #   [9,5,1,2]       \
        # compare [1,2,3]
        # compare [5,1,2]
        #
        # O(n), 19%
        for i in xrange(len(matrix)-1):
            if matrix[i][:-1] != matrix[i+1][1:]: return False
        return True



if __name__ == '__main__':
    s = Solution()
    tc =  [[                \
            [1,2,3,4],      \
            [5,1,2,3],      \
            [9,5,1,2]       \
           ],               \
           [                \
            [1,2],          \
            [2,2]           \
           ],               \
           [                \
            [1,2],          \
            [2,1]           \
           ],[1]           ]
    ans = [  True, False, True, True]

    for i in range(len(tc)):
        r = s.isToeplitzMatrix(tc[i])
        print (r)
        assert(r == ans[i])
