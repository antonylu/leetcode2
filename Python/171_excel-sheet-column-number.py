"""
https://leetcode.com/problems/excel-sheet-column-number/description/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach #1, use chr() and ord()
        # mapping Alpha A to number, ord('A') - ord('A')+ 1
        # 26 進位
        # 74% 49ms
        sum = 0
        for c in s:
            sum = sum * 26
            sum = sum + ord(c) - ord('A') +1
        return sum

if __name__ == "__main__":
    s=Solution()
    tc = ["A","AB","ZY","ZZ"]
    for t in tc:
        print(s.titleToNumber(t))
        #s.convertToTitle(t)
