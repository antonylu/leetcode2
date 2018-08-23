"""
https://leetcode.com/problems/divide-two-integers/description/

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2


Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #(a,b) = divmod(dividend,divisor)
        a = int(float(dividend)/divisor)
        if a > 2147483647: return 2147483647
        if a < -2147483648: return -2147483648
        return a
        



if __name__ == '__main__':
    s = Solution()
    tc =  [ (10,3), (7,-3) ]
    ans = [ 3, -2]
    for i in range(len(tc)):
        r = s.divide(*tc[i])
        print(r)
        assert(r == ans[i])
