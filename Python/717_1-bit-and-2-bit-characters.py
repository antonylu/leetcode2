"""
https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False

Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # Approach #1, brute-force
        #
        # if 1: 2
        # if 0: 1
        # is the last char one or two bits?
        #
        # O(n), 35%
        i = 0
        length = len(bits)
        while i < length:
            if bits[i] == 1:
                digit = 2
            else:
                digit = 1
            i+= digit
        return digit == 1


if __name__ == '__main__':
    s = Solution()
    tc = [[1, 0, 0], [1, 1, 1, 0]]
    ans = [True, False]

    for i in range(len(tc)):
        r = s.isOneBitCharacter(tc[i])
        print (r)
        assert(r == ans[i])
