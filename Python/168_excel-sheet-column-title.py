"""
https://leetcode.com/problems/excel-sheet-column-title/description/
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
    
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Approach #1, 26 進位, 3位
        # 
        """
        A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
        B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
        Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
        """
        # 55%,32ms
        number2char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        while n > 26:
            (n,b) = divmod(n-1,26)
            r+=number2char[b]
        r+=number2char[n-1]
        return r[::-1]

if __name__ == "__main__":
    s=Solution()
    tc = [1,28,701,702]
    #tc = [1]
    for t in tc:
        print(s.convertToTitle(t))
        #s.convertToTitle(t)
