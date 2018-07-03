"""
https://leetcode.com/problems/buddy-strings/description/

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true

Example 2:

Input: A = "ab", B = "ab"
Output: false

Example 3:

Input: A = "aa", B = "aa"
Output: true

Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

"""
xrange = range
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # Approach #1, two pointer
        #
        # two pointer to remember the index of two difference
        # check equal by swap it
        #
        # O(n), 46ms
        #
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        diff = []
        for i in xrange(len(A)):
            if A[i] != B[i]:
                diff.append(i)
        if len(diff) != 2: return False
        if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True
        return False




if __name__ == '__main__':
    s = Solution()
    tc =  [ ("ab","ba"), ("ab","ab"), ("aa", "aa"),("aaaaaaabc",  "aaaaaaacb"), ("", "aa") ]
    ans = [ True, False, True, True, False ]
    for i in range(len(tc)):
        r = s.buddyStrings(*tc[i])
        print (r)
        assert(r == ans[i])
