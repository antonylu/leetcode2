"""
https://leetcode.com/problems/rotate-string/description/

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""
xrange = range
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # Approach #1, brute-force
        #
        # enumerate all len(A)th possible shifted A and compoare with B
        # O(len(A))


        # Approach #2, if B in A+A
        #
        # if B in A+A and len(A)==len(B)
        #
        # O(n), 93%
        return len(A) == len(B) and B in A*2



if __name__ == '__main__':
    s = Solution()
    tc =  [ ('abcde', 'cdeab'), ('abcde', 'abced') ]
    ans = [ True, False ]
    for i in range(len(tc)):
        r = s.rotateString(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])
