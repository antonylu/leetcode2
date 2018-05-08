""" 
https://leetcode.com/problems/pascals-triangle/description/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Approach #1: recursive, 
        # Approach #2: iteration
        # based on previous list, create a new list with [0]+[1], [1]+[2]..., append 1 in front/back of the new list
        # O(n^2), 35ms, 72%
        if numRows == 0: return []
        r = []
        for i in range(numRows):
            r.append(self.pascal(i))
        return r
        
    pas = [                 \
                 [1],       \
                [1,1],      \
               [1,2,1],     \
              [1,3,3,1],    \
             [1,4,6,4,1]    \
          ]
    def pascal(self,n):
        if n < 5: return self.pas[n]
        list = self.pascal(n-1)
        rlist = [1]
        for j in range(1,len(list)):
            rlist.append(list[j-1] + list[j])
        rlist.append(1)
        return rlist


if __name__ == "__main__":
    s = Solution()
    for i in range(7):
        print(s.generate(i))

