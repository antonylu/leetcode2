"""
https://leetcode.com/problems/reverse-bits/description/

Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Approach #1, convert to binary string, reverse, convert back
        # 88%
        s='{0:032b}'.format(n)[::-1]
        return int(s,2)

        # {} places a variable into a string
        # 0 takes the variable at argument position 0
        # : adds formatting options for this variable (otherwise it would represent decimal n)
        # 032 formats the number to 32 digits zero-padded on the left
        # b converts the number to its binary representation

if __name__ == "__main__":
    s=Solution()
    tc = [43261596]
    for t in tc:
        print(s.reverseBits(t))
