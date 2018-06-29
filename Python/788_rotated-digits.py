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
        # Approach #2, set operation
        #
        # All digits in set([0,1,8,2,5,6,9])
        # at least one in set([2,5,6,9])
        #
        # O(n), 45%
        s1 = set('0182569')
        s2 = set('2569')
        def isGood(n):
            n = set(str(n))
            if len(n & s2) == 0: return False
            if not n <= s1: return False
            return True
        count = 0
        for j in xrange(N+1):
            if isGood(j): count += 1

        return count

        # Approach #1, brute-force
        #
        # All digits in set([0,1,8,2,5,6,9])
        # at least one in set([2,5,6,9])
        #
        # O(n), 74%
        s1 = set('0182569')
        s2 = set('2569')
        def isGood(n):
            good = False
            for c in str(n):
                if c not in s1: return False
                if c in s2: good = True
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
