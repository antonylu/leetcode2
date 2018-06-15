"""
https://leetcode.com/problems/sum-of-square-numbers/description/

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False


"""
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        # Approach #1, brute-force with sqrt
        # 
        # c = a^2+b^2
        # a^2 = c - b^2
        # possible b is between 1~sqrt(c)
        #
        # O (sqrt c), 92%
        #
        from math import sqrt
        for b in range(int(sqrt(c))+1):
            a = sqrt(c - b*b)
            if a.is_integer(): return True
        
        return False


if __name__ == '__main__':
    s = Solution()
    tc  = [ 5,3, 34, 35,2,0]
    ans = [ True, False, True, False, True,True]
    for i in range(len(tc)):
        r = s.judgeSquareSum(tc[i])
        print (r)
        assert(r == ans[i])
