"""
https://leetcode.com/problems/largest-triangle-area/solution/

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""
xrange = range
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # Approach #1, brute-force
        #
        # calculate all possible triangles area and get max()
        # triangle formula:
        #  1. shoelace formula, https://en.wikipedia.org/wiki/Shoelace_formula
        #  say 3 points a,b,c
        #    xa  ya
        #    xb  yb
        #    xc  yc
        #    xa  ya
        #  area = ((xa*yb+xb*yc+xc*ya) - (ya*xb+yb*xc+yc*xa)) /2
        #
        # use itertools.combinations(points,3)
        #
        # O(n), 180ms
        #
        import itertools
        area = 0
        for (a,b,c) in itertools.combinations(points,3):
            #print(a,b,c)
            area = max(area, abs((a[0]*b[1]+b[0]*c[1]+c[0]*a[1]) - (a[1]*b[0]+ b[1]*c[0]+c[1]*a[0])) *.5)
        return area



if __name__ == '__main__':
    s = Solution()
    tc =  [  [[1,0],[0,0],[0,1]], [[0,0],[0,1],[1,0],[0,2],[2,0]]]
    ans = [ .5, 2.0 ]
    for i in range(len(tc)):
        r = s.largestTriangleArea(tc[i])
        print (r)
        assert(r == ans[i])
