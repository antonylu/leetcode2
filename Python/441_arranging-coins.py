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
    def arrangeCoins1(self, n):
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
            #print(",",fk)
            if fk<=n<fk1: return k
            k+=1
    def arrangeCoins(self, n):
        # Approach #3, reverse engineering
        # n = f(k) = (k+1)*k/2 = (k^2+k)/2
        # k = g(n) ~= sqrt(2n)-1
        # O(1), 93%
        """
        if n < 10012:
            d = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011]
            from bisect import bisect
            return bisect(d,n)
        """
        
        k   = int((2*n)**0.5)-1
        fk1 = k*(k+1)//2
        while True:
            fk  = fk1
            fk1+= k+1
            #print(",",fk)
            if fk<=n<fk1: return k
            k+=1
        

        # Approach #2, 
        # create the lookup table for 65535's entries
        # d = [1, 3, 6, 10, ... 2147450880]
        # from bisect import bisect
        # return bisect(d,n)
        # it works but leetcode rejected:
        # Your code is too long. Please reduce your code size and try again.

    def arrangeCoins(self, n):
        # Approach #4, math reverse engineering
        # n = f(k) = (k+1)*k/2 = (k^2+k)/2
        # k = g(n) ~= sqrt(2n+0.25)-0.5
        # 1+2+3+...+x = n
        # -> (1+x)x/2 = n
        # -> x^2+x = 2n
        # -> x^2+x+1/4 = 2n +1/4
        # -> (x+1/2)^2 = 2n +1/4
        # -> (x+0.5) = sqrt(2n+0.25)
        # -> x = -0.5 + sqrt(2n+0.25)
        # O(1), 82.6%
        return int(((2*n+0.25)**.5)-0.5)

if __name__ == '__main__':
    s = Solution()
    tc = [5,8,12,1,3,6,40,pow(2,31)]
    #tc = [pow(2,31)]
    an = [2,3,4,1,2,3,8,65535]
    for i in range(len(tc)):
        print(s.arrangeCoins(tc[i]))
        assert(s.arrangeCoins(tc[i]) == an[i])
