"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.


"""
xrange = range
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Approach #1, naive
        # 
        # the index of the maximum value
        # 
        # O(n), 64ms
        for i in xrange(len(A)):
            if A[i]>A[i+1]: return i




if __name__ == '__main__':
    s = Solution()
    tc =  [ [0,1,0], [0,2,1,0]]
    ans = [ 1, 1 ]
    for i in range(len(tc)):
        r = s.peakIndexInMountainArray(tc[i])
        print (r)
        assert(r == ans[i])
