"""
https://leetcode.com/problems/can-place-flowers/description/

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Approach #1, naive
        #
        # count no. of serial 0s
        # 10001    : 3: 1
        # 1000001  : 5: 2
        # 100000001: 7: 3
        # 10 xn ..1: (n-1)//2
        #
        # O(n), 100%
        c = 1
        ans = 0
        flowerbed.append(0)
        for e in flowerbed:
            if e == 0: 
                c+=1
            else:
                if c > 2: ans += (c-1)//2
                c = 0
        if c > 2: ans += (c-1)//2

        return ans >= n


if __name__ == '__main__':
    s = Solution()
    tc  = [ ([1,0,0,0,1], 1),([1,0,0,0,1], 2) ]

    ans = [ True, False ]

    for i in range(len(tc)):
        r = s.canPlaceFlowers(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])
