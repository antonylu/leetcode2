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
        # Solution 3, Optimization
        # memorization with max/min
        # 
        # range: [−2**31,  2**31 − 1] = [2147483647, -2147483648]
        # use Python default str/reverse/int conversion
        # 
        # time O(1), beats 54.53%, Python 59ms
        if x < 0:
            y  = - int(str(-x)[::-1])
        else:
            y  = int(str(x)[::-1])
        if y > 2147483647 or y < -2147483648:
            return 0
        return y
        
s = Solution()
print(s.reverse(-123))
