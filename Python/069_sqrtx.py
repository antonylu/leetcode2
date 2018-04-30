""" 
https://leetcode.com/problems/sqrtx/description/

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Approach 1: brute-force, enumerate and test (i^2<=x) for all integer i, (0< i < x)
        #   Time O(n)
        # Approach 2: brute-force, bineary search and test (i^2<=x) for all integer i, (0< i < x)
        #   Time O(log n)
        # Approach 3: Newton method (?)
        #   Time O(log n?)
        
        # Approach 1: brute-force, enumerate and test (i^2<=x) for all integer i, (0< i < x)
        #   Time O(n*m)
        #   Space: MemoryError in range()
        # if x <=1: return x
        # for i in range(x,1,-1):
        #     if i*i <= x: return i
        # Approach 1: brute-force, enumerate and test (i^2<=x) for all integer i, (0< i < x)
        #   Time O(n*m): Time exceeded
        # if x <=1: return x
        # i = x
        # while i>0:
        #     if i*i <= x: return i
        #     i = i-1

        # Approach 4: use default function x**(1/2), cheating
        # 52ms, 100%
        return int(x**(1/2))
        
        # Approach 2: brute-force, bineary search and test (i^2<=x && (i+1)^2 >x) for all integer i, (0< i < x)
        #   Time O(log n)
        #  38%, 67ms
        if x <=1: return x
        min = 1
        max = x//2
        while min <= max:
            mid = int((min+max)//2)
            #print(min,mid,max)
            t = mid **2
            if t == x: return mid
            if t <=x and (mid+1)**2 > x : return mid
            if t < x:
                min = mid+1
            else:
                max = mid-1
        

s = Solution()
test_case = [4,8,9,81,80,2147395599]
#test_case = [4]
for i in test_case:
    print(s.mySqrt(i))
