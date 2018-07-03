"""
https://leetcode.com/problems/backspace-string-compare/description/

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

"""
xrange = range
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # Approach #1, brute-force
        #
        # Time:  O(n), 43ms
        # Space: O(n)
        #
        s,t =[], []
        for c in S:
            if c != '#':
                s.append(c)
            else:
                if len(s) >0: del s[-1]
        for b in T:
            if b != '#':
                t.append(b)
            else:
                if len(t) >0: del t[-1]
        return s == t    


if __name__ == '__main__':
    s = Solution()
    tc =  [  ("ab#c", "ad#c"), ( "ab##", "c#d#"), ("a##c", "#a#c"), ("a#c", "b") ]
    ans = [  True, True, True, False ]
    for i in range(len(tc)):
        r = s.backspaceCompare(*tc[i])
        print (r)
        assert(r == ans[i])
