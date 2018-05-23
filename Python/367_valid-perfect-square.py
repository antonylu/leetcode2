"""
https://leetcode.com/problems/valid-perfect-square/description/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # approach #1, Newton method to get near sqrt
        #
        # f(n+1) =(f(n)+num/f(n))/2
        # 96%
        
        x = num
        while x*x >num:
            x = (x+num/x)//2

        return x*x == num
            
        
        
        # approach #2, brute-force, binary search
        #
        # try x=1~n//2, if x^2< num and (x+1)^2 > num, return False
        # O(log N)
        
        # approach #3, cheating
        # num**(0.5)
        # O(1) 85%
        a = num** 0.5
        return int(a) == a
                    
                

if __name__ == '__main__':
    tc = [16,14,15,4,2,1,0,5]
    ans = [True,False,False,True,False,True,True,False]
    s = Solution()
    for i in range(len(tc)):
        print(s.isPerfectSquare(tc[i]))
        assert(s.isPerfectSquare(tc[i]) == ans[i])

