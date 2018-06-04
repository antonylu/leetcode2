"""
https://leetcode.com/problems/perfect-number/description/

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Approach #1, brute-force
        # trial error all numbers < num**.5
        # add them up and compare
        #
        # e.g., 28, Sqrt(28) =5.x, try 2~5
        # 2->14, 3x, 4->7, 5x
        # a = 1+2+14+4+7
        #
        # O(logn), 82%
        if num < 6: return False
        S = int(num**.5 + 1)
        a = 1
        for i in range(2,S):
            if num % i == 0 : a = a + i + num/i
        return a == num
        

        # Approach #2, lookup table
        #
        # O(1), 99%
        # 
        # https://en.wikipedia.org/wiki/List_of_perfect_numbers
        s = set([6,28,496,8128,33550336])
        return num in s
        
        
        
        
        


if __name__ == '__main__':
    s = Solution()
    tc = [28,100,7,1,6]
    an = [True, False, False, False, True]
    for i in range(len(tc)):
        print (s.checkPerfectNumber(tc[i]))
        #assert(s.checkPerfectNumber(tc[i])== an[i])
