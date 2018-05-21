"""
https://leetcode.com/problems/add-digits/description/

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Approach #1, brute-force,
        # O(1), 84%
        while num > 9:
            num,d = divmod(num,10)
            num+=d
        return num
            


if __name__ == "__main__":
    tc = [38,1231,251234,3584357]
    s = Solution()
    for t in tc:
        print(s.addDigits(t) )
