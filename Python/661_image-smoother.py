"""
https://leetcode.com/problems/image-smoother/description/

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale 
(rounding down) of all the 8 surrounding cells and itself. 
If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach #1, two level nested loop, 
        # create a new matrix and return
        # calculate the value based on condition
        # note, to create a copy of list of objects, use deepcopy
        #
        #  (-1,-1),(0,-1),(1,-1)
        #  (-1, 0),(0, 0),(1, 0)
        #  (-1, 1),(0, 1),(1, 1)
        # O(n), 21%
        from copy import deepcopy
        A = deepcopy(M)
        y_len = len(M)
        x_len = len(M[0])
        offset = [ (-1,-1),(0,-1),(1,-1), (-1, 0),(0, 0),(1, 0), (-1, 1),(0, 1),(1, 1) ]
        for y in range(y_len):
            for x in range(x_len):
                sum = 0
                count = 0
                for o in offset:
                    x1 = x + o[0] 
                    y1 = y + o[1]
                    if x1>=0 and x1 <x_len and y1>=0 and y1 < y_len:
                        sum += M[y1][x1]
                        count += 1
                A[y][x] = sum//count
        return A
        


if __name__ == '__main__':
    s = Solution()
    tc  = [ [[1,1,1], [1,0,1], [1,1,1]],[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]] ]
    ans = [ [[0, 0, 0], [0, 0, 0], [0, 0, 0]],[[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]]
    for i in range(len(tc)):
        r = s.imageSmoother(tc[i])
        print (r)
        assert(r == ans[i])
