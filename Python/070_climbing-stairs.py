""" 
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(1) = 1   => 1
        # f(2) = 1+1       or 2   => 2
        # f(3) = 1+1+1     or 2+1     or 1+2 => 3
        # f(4) = 1+1+1+1   or 2+1+1   or 1+2+1   or 1+1+2              or 2+2 => 5 
        # f(5) = 1+1+1+1+1 or 2+1+1+1 or 1+2+1+1 or 1+1+2+1 or 1+1+1+2 or 2+2+1, or 2+1+2 or 1+2+2 => 8
        # step to (n-1)+1 plus steps to (n-2)+2
        # f(n) = f(n-1) + f(n-2)
        # Looks like Fibonaci's Sequence

        # Approach 1: Recursive
        # Time O(n!),  Time Limit Exceeded
        # if n < 4: return n
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        
        # Approach 2: Iteration
        # O(n), 
        # Python 2 96%
        # Python 3 100%
        if n < 4: return n
        s1 = 2
        s2 = 3
        i  = 3
        while(i<n):
            s = s1+s2
            s1= s2
            s2= s
            i+=1
        return s
            
        
        # Approach 3: Dynamic programming
        # memorization + devide and conqure + recursive

s = Solution()
test_case = [2,3,38]
for i in test_case:
    print(s.climbStairs(i))
