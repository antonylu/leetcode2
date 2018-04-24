# https://leetcode.com/problems/hamming-distance/description/
# 
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 231.
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # xor, count no. of 1
        # O(n), beats 5.06% 56ms
        z = x ^ y
        h = 0
        while z:
            h +=1
            z &= (z-1)
        return h
