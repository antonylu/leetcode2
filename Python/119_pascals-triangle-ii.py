""" 
https://leetcode.com/problems/pascals-triangle-ii/description/

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
    def getRow2(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Approach #2: iteration
        # 2 dimension array
        # r[i][j]
        # 70%, 34ms
        # O(n), S(n)
        r = [[1]]
        for i in range(1,rowIndex+1): #
            rlist = [1]
            for j in range(1,i):
                rlist.append(r[i-1][j-1] + r[i-1][j])
            rlist.append(1)

            r.append(rlist)
        return r[-1]
        

    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Approach #1: recursive, 
        # based on previous list, create a new list with [0]+[1], [1]+[2]..., append 1 in front/back of the new list
        # O(k), 36ms, 46%
        r = []
        for i in range(numRows+1):
            r.append(self.pascal(i))
        return r[-1]
        
    pas = [                                \
                 [1],                      \
                [1,1],                     \
               [1,2,1],                    \
              [1,3,3,1],                   \
             [1,4,6,4,1],                  \
            [1, 5, 10, 10, 5, 1],          \
           [1, 6, 15, 20, 15, 6, 1],       \
          [1, 7, 21, 35, 35, 21, 7, 1],    \
         [1, 8, 28, 56, 70, 56, 28, 8, 1]  \
        ]
    def pascal(self,n):
        if n < len(self.pas): return self.pas[n]
        list = self.pascal(n-1)
        rlist = [1]
        for j in range(1,len(list)):
            rlist.append(list[j-1] + list[j])
        rlist.append(1)
        self.pas.append(rlist)
        return rlist


if __name__ == "__main__":
    s = Solution()
    for i in range(10):
        print(s.getRow(i))

