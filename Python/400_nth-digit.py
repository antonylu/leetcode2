"""
https://leetcode.com/problems/nth-digit/description/

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:
Input: 3
Output: 3

Example 2:
Input: 11
Output: 0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

"""
import bisect
class Solution(object):
    def findNthDigit1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #1, brute-force
        # list all numbers and breaks into single digit number
        # get the n-th element
        # unrealistic,  Time Limit Exceeded
        # 
        lst = []
        for i in range(1,n+1):
            s =str(i)
            for j in s:
                lst.append(j)
        return int(lst[n-1])

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #2, divide and conqure
        #
        # 1 digit : 1~9, 9 x 1 = 9 digits
        # 2 digits: 10~99, 90 x 2 = 180 digits
        # 3 digits: 100~999, 900 x 3 = 2700 digits
        # 4 digits: 1000~9999, 9000 x 4 = 36000 digits
        # 5 digits: 10000~99999, 90000 x 5 = 450000 digits
        # ...
        # n digits: 9 x pow(10, n-1) x n  digits
        #
        # 
        #
        #  9, 90*2, 900*3, 9000*4
        #  1,2,...9,  1,0, 1,1, 1,2, 1,3...9,9,   1,0,0,
        #  
        #  For example gave N = 1000, then 1000-9-180 = 811, it means the 811th digit local in [100, 999], and we know each number like 100 has three digit, so 811 / 3 = 270,
        #  Then, we know the 270th number in [100, 999], is 270th + 100 (start from 100) = 370.
        #  370 still has three digit, which one is the answer? 3, 7, 0
        #  811 % 3 = 1, so the first one is the answer, so return 3.
        #  
        #  
        #  1. find n in which group, 1 digit? 2 digits?
        #  2. then find the digit in which number
        #  3. then find the digit
        #  
        # 
        # groups = []
        # g,i = 0, 1
        # while g < pow(2,31):
        #     g = 9 * pow(10,i-1) * i
        #     groups.append(g)
        #     i+=1
        # print(groups)
        # exit(0)
        #if n < 10:
        #   return n
        #  
        #  31ms, 95%
        groups = [9, 180, 2700, 36000, 450000, 5400000, 63000000, 720000000, 8100000000]
        g = bisect.bisect_left(groups,n) # 2
        nth = n - sum(groups[:g]) -1 # 1000 - 9 - 180 = 811
        d,m = divmod(nth,g+1)
        number = d+pow(10,g)
        return int(str(number)[m])


if __name__ == '__main__':
    tc =  [3,10,11,12,13,14,15, 92,93,94,95,96, 97,98,99,  100,101,102,103]
    ans = [3,1 ,0 ,1 ,1 ,1 ,2 ,  5, 1, 5, 2, 5,  3, 5, 4,    5,  5,  5, 6]
    s = Solution()
    for i in range(len(tc)):
        print(s.findNthDigit(tc[i]))
        #print(s.findNthDigit2(tc[i]))
        assert(s.findNthDigit(tc[i]) == ans[i])
        #assert(s.findNthDigit2(tc[i]) == ans[i])
