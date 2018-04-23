# https://leetcode.com/problems/reverse-integer/description/
# 
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# Input: 123
# Output: 321
# 
# Example 2:
# Input: -123
# Output: -321
# 
# Example 3:
# Input: 120
# Output: 21
#
# Note:
# Assume we are dealing with an environment which could only store integers within 
# the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
# 
# 
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        sign = 1

        if(x <0): 
            x = abs(x)
            sign = -1
        # Solution 1, brute force, while loop
        # plus from right most digits
        # time  O(n), beats 85.29% Python 3, 60 ms
        # time  O(n), beats 33.3% Python, 60 ms
#
#        while(x!=0):
#            a = divmod(x,10)
#            r = r*10 + a[1]
#            x = a[0]

        # Solution 2
        # python can reverse string quickly
        # convert to string the reverse
        # time O(1), beats 62.27%, Python 57ms
        r = int(str(x)[::-1])

        r=r*sign
        if (r >= 2**31 or r <=-1*2**31): return 0

        return r

        
s = Solution()
print(s.reverse(-123))
