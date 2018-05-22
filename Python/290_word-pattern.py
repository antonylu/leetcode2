"""
https://leetcode.com/problems/word-pattern/description/


Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Approach #1, use hash map to keep dict["dog"] = "a"
        # go through list
        # if not in dict, put in dict
        # if in dict, get in dict and check 
        # O(n), 68%
        
        S2P = {}
        P2S = {}
        s = str.split()
        if len(s) != len(pattern): return False
        #print(s)
        for i in range(len(s)):
            if s[i] in S2P:
                if S2P[s[i]] != pattern[i]:
                    return False
            elif pattern[i] in P2S:
                if s[i] != P2S[pattern[i]]:
                    return False
            else:
                S2P[s[i]] = pattern[i]
                P2S[pattern[i]] = s[i]
        return True
        

if __name__ == "__main__":
    tc = [("abba", "dog cat cat dog"),("abba", "dog cat cat fish"),("aaaa", "dog cat cat dog"),("abba", "dog dog dog dog")]
    ans = [True, False, False, False]
    s = Solution()
    for t in tc:
        print(s.wordPattern(t[0],t[1]))
