"""
https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #1, dicrect
        # convert to binary string '0b000000001111' , count 1's number
        #
        return bin(n)[2:].count('1')

if __name__ == "__main__":
    s=Solution()
    tc = [11,128]
    for t in tc:
        print(s.hammingWeight(t))
