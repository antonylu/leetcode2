"""
https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:
Input:
26
Output:
"1a"

Example 2:
Input:
-1
Output:
"ffffffff"

"""
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Approach #1
        # divmod(num,16)
        # becuase python's integer > 2^32
        # for negative, +2^32 to make it as a positive
        # -1: ffff ffff  => 2^32 -1 = 1 0000 0000 - 1 = FFFF FFFF
        # -2: ffff fffe  => 2^32 -1 = 1 0000 0000 - 1 = FFFF FFFF
        #
        # 94%
        
        hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        ans = ""
        if num == 0: return "0"
        if num <0: num += 2**32
        while num != 0:
            num, m = divmod(num,16)
            ans = hex[m] + ans
            
        return ans
        
        
        
if __name__ == '__main__':
    s = Solution()
    tc = [26,27,0xFF, 0x28,0xFFFFABCD,-1,0]
    ans = ["1a","1b","ff","28","ffffabcd","ffffffff","0"]
    for t in tc:
        print(s.toHex(t))
