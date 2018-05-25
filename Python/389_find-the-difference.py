"""
https://leetcode.com/problems/find-the-difference/description/

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # dict, xor, diff
        # Approach #2, Counter count occurence of t
        # 32%
        from collections import Counter
        c1 = Counter(t)
        c2 = Counter(s)
        c3 = c1-c2
        return list(c3.elements())[0]
        
        # Approach #1, xor
        # xor every char in s and t
        # 97%
        ans = ord(t[0])
        for i in range(1,len(t)):
            ans ^= ord(t[i])
        for c in s:
            ans ^= ord(c)
        return chr(ans)


if __name__ == '__main__':
    tc = [("abcd","abcde"),("a","aa")]
    ans = ['e','a']
    s = Solution()
    for t in tc:
        #s.findTheDifference(i)
        print(s.findTheDifference(t[0],t[1]))
