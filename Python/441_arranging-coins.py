"""
https://leetcode.com/problems/arranging-coins/description/

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #1, naive
        #
        # for kth, n = f(k) = 1+2+..+kth = (k+1)*k/2
        # f(k+1) = f(k) + k+1
        # 
        # brute force, 
        # from 1 to n, f(k) <=n and f(k+1) >n
        # return k
        #
        # O(n), 13%
        if n == 0: return 0
        k   = 1
        fk1 = 1
        while True:
            fk  = fk1
            fk1+= k+1
            if fk<=n<fk1: return k
            k+=1
            



if __name__ == '__main__':
    s = Solution()
    tc = [5,8,12,1,3,6,pow(2,31)]
    an = [2,3,4,1,2,3,65535]
    for i in range(len(tc)):
        print(s.arrangeCoins(tc[i]))
        assert(s.arrangeCoins(tc[i]) == an[i])
