"""
https://leetcode.com/problems/shortest-distance-to-a-character/description/

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

"""
xrange = range
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # Approach #1, brute-force
        #
        # 1 loop locate all index of C in a list
        # bisect between i1 and i2, and min(d-i1,i2-d)
        i = 0
        L = []
        while i < len(S):
            i = S.find(C,i)
            if i == -1: break
            L.append(i)
            i += 1
        from bisect import bisect_left
        ans = []
        for j in xrange(len(S)):
            k = bisect_left(L, j)
            d = min(abs(L[k if k< len(L) else k-1] - j), abs(j-L[k-1 if k > 0 else 0]) )
            ans.append(d)
        return ans




if __name__ == '__main__':
    s = Solution()
    tc =  [  ("loveleetcode", 'e'), ("aaba",'b') ]
    ans = [ [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0], [2,1,0,1] ]
    for i in range(len(tc)):
        r = s.shortestToChar(*tc[i])
        print (r)
        assert(r == ans[i])
