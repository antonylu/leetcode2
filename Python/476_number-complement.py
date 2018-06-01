"""
https://leetcode.com/problems/number-complement/description/

You are given a map in form of a two-dimensional iWinter is Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Approach #1, bitwise manipulation
        #
        #         5: 0000 0101
        #        ~5: 1111 1010 --> -6
        #      mask: 0000 0111
        # ~5 & mask: 0000 0010
        #
        # how to get mask?
        # count how many significant bits of 5
        # >>> bin(1000) 
        # '0b1111101000'
        # -1 : 1111 1111
        #
        # O(1), 93%
        n = len(bin(num))-2
        mask = ~(-1 << n)
        return mask & ~num


if __name__ == '__main__':
    s = Solution()
    tc = [5,1]
    an = [2,0]
    for i in range(len(tc)):
        print (s.findComplement(tc[i]))
        assert(s.findComplement(tc[i]) == an[i])
