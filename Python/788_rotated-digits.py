"""
https://leetcode.com/problems/rotated-digits/description/

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.
Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other;
6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].

"""
xrange = range
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Approach #1, brute-force
        #
        # All digits in set([0,1,8,2,5,6,9])
        # at least one in set([2,5,6,9])
        #
        # O(n), 33%
        s1 = {0,1,8,2,5,6,9}
        s2 = {2,5,6,9}
        def isGood(n):
            good = False
            for c in str(n):
                i = int(c)
                if i not in s1: return False
                if i in s2: good = True
            return good
        count = 0
        for j in xrange(N+1):
            if isGood(j): count += 1

        return count





if __name__ == '__main__':
    s = Solution()
    tc =  [ 10,100,1000 ]
    ans = [ 4, 40, 316 ]
    for i in range(len(tc)):
        r = s.rotatedDigits(tc[i])
        print (r)
        assert(r == ans[i])
