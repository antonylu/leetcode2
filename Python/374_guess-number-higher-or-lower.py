"""
https://leetcode.com/problems/guess-number-higher-or-lower/description/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
ans  = 6
def guess(num):
    if num == ans: return 0
    if num > ans:
        return -1
    else:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #2, use bisect to do linear search
        # O(n), 50%
        import bisect
        class C(object):
            __getitem__ = lambda _, i: -guess(i)

        # bisect try to get index from 1 to n, looking for -1's position
        # when get item from C[i], it calls -guess(i) which returns -1 until it returns 0
        # actually it is not binary search but it is linear search        
        return bisect.bisect(C(), -1, 1, n)
        

        # Approach #1, binary search
        # O(log n), 90%
        min = 1
        max = n
        while min <=max:
            mid = (min+max)//2
            if guess(mid) == 0: return mid
            if guess(mid) == 1: 
                min = mid +1
            else:
                max = mid -1
                

if __name__ == '__main__':
    tc = [1,10,100]
    s = Solution()
    for i in tc:
        print(s.guessNumber(i))


