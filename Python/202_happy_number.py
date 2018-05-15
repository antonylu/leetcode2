"""
https://leetcode.com/problems/happy-number/description/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, 

and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 

Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution(object):
    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach #1, DP
        # continue to find next until it loops endlessly
        # use Set or Hash table to keep every result
        # check if the loops point (==) is 1
        # O(?) 47ms, 58%
                
        s = set()

        while n not in s:
            s.add(n)
            n = self.next(n)
        return True if n == 1 else False
        
    def next2(self,n):
        ans = 0
        for c in str(n):
            ans = ans+ int(c)*int(c)
        return ans

    def next(self,n):
        ans = 0
        while (n!= 0 ):
            (n,d) = divmod(n,10)
            ans = ans + d*d
            #print(ans)
        return ans
        
    def isHappy(self, n):
        # Approach #2, Floyd Cycle Detection
        # Turtle and Rabbit Race
        # if there is a loop, the rabbit will catch up the turtle finally
        # 46ms, 63%
        rabbit = self.next(n)
        turtle = n
        while rabbit != turtle:
            turtle = self.next(turtle)
            rabbit = self.next(rabbit)
            rabbit = self.next(rabbit)
            if rabbit ==1 or turtle ==1: return True 
        return True if turtle == 1 else False
        
        
        
        

if __name__ == "__main__":
    s=Solution()
    tc = [19,21,91]
    ans = [True]
    for t in tc:
        print(s.isHappy(t))
