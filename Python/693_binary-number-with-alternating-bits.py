"""
https://leetcode.com/problems/binary-number-with-alternating-bits/description/

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True

Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7

Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False

Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True

Explanation:
The binary representation of 10 is: 1010.
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach #1, naive 
        #
        # convert to bin presentation, bin(n)
        # compare bit by bit
        # O(n), 22%
        nb = bin(n)[2:]
        c1 = nb[0]
        for c in nb[1:]:
            if c == c1: return False
            c1 = c
        return True
        



if __name__ == '__main__':
    s = Solution()
    tc  = [ 5,7,11,10]
    ans = [ True, False, False, True ]


    for i in range(len(tc)):
        r = s.hasAlternatingBits(tc[i])
        print (r)
        assert(r == ans[i])
