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
        # Approach #2, no loop
        # https://en.wikipedia.org/wiki/Digital_root
        # f(n) = 0                  if n=0
        #      = 1 + ((n-1)%9)      if n>0
        # 
        # O(1), 92%
        return 0 if num == 0 else (num-1)%9 +1
        
        # Approach #1, brute-force,
        # O(1), 84%
        while num > 9:
            num,d = divmod(num,10)
            num+=d
        return num
            


if __name__ == "__main__":
    tc = [38,1231,251234,3584357]
    ans = [2,7,8,8]
    s = Solution()
    for t in tc:
        print(s.addDigits(t) )
