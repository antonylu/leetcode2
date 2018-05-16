"""
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach #2, set with zip
        # zip(s,t) shall be one on one from s mapping to t
        # so the length of set of zip(s,t) shall be the same as set(s) and set(t)
        # 47ms, 92%
        return len(set(zip(s,t) ) ) == len(set(s)) == len(set(t))

        # Approach #1, hash table
        # dict[s]=t
        # enumerate s and t, replace t with a characters
        # compare s,t
        # O(2n) = O(n)
        # 95%, 46ms
        dict = {}
        a=s
        b=t
        s = list(a)
        t = list(b)
        sl = len(s)

        for i in range(sl):
            if s[i] in dict:
                s[i]=dict[s[i]]
            else: 
                dict[s[i]] = t[i]
                s[i]=t[i]
        if s != t: return False 
        
        t = list(a)
        s = list(b)
        dict.clear()
        for i in range(sl):
            if s[i] in dict:
                s[i]=dict[s[i]]
            else: 
                dict[s[i]] = t[i]
                s[i]=t[i]
        return s == t


if __name__ == "__main__":
    s = Solution()
    tc  = [("egg","add"), ("foo", "bar"), ("paper","title"),("ab","aa"),("aa","ab")]
    ans = [True, False, True, False, False]
    for t in tc:
        print(s.isIsomorphic(t[0],t[1]))

