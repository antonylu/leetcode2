"""
https://leetcode.com/problems/excel-sheet-column-number/description/

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #1, because only 5x2 makes 0, so maybe count how many 5 in 1~N
        # 25 is 5x5, 25/5 = 5
        # 125 is 5x5x5, 125/5 = 25
        # 
        # 98%
        if n < 5: return 0
        n = n//5
        return n + self.trailingZeroes(n)
        

if __name__ == "__main__":
    s=Solution()
    tc = [3,5,10,1808548329]
    for t in tc:
        print(s.trailingZeroes(t))
        #s.convertToTitle(t)
