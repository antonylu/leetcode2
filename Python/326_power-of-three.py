"""
https://leetcode.com/problems/range-sum-query-immutable/description/


Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach #2, tricky
        #
        # the maximum power of 3 as integer is 3^19 = 1162261467
        # 
        #
        # O(n), 60%
        if n < 1 : return False
        return 1162261467 % n == 0

        # Approach #1, naive
        #
        # power of 3 are 1,3,9,27,81...
        # continue divide it by 3 would result 1
        #
        # O(n), 45%
        if n == 0: return False
        if n == 1: return True
        while n%3 == 0:
            n=n/3

        return n == 1

        


# Your NumArray object will be instantiated and called as such:

if __name__ == "__main__":
    tc  = [27,0,9,45,1,-3]
    ans = [True, False, True, False, True, False]
    s = Solution()
    for i in range(len(tc)):
        print( s.isPowerOfThree(tc[i]))
        assert(s.isPowerOfThree(tc[i]) == ans[i])