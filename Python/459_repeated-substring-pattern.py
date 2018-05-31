"""
https://leetcode.com/problems/repeated-substring-pattern/description/

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True

Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # approach #1, brute force
        #
        # check if substring s[0:n] can make the whole string, for n<= len(s)
        # how to check if a substring can make the whoe string?
        # check 
        #  1. len(s) % n == 0
        #  2. n >= set(s)
        #  then ?

        # approach #2, extend then break
        # Given whole string s, repeated string r
        #
        # First char of s is first char r
        # Last char of s is last char r
        # r         :[abc]
        # s = r*n
        # s         :[abc|abc] 
        # ss        :[abc|abc|abc|abc]
        # break ss  :[ bc|abc|abc|ab ]
        # in ss, we can't find s in first part of s and 2nd part of s alone
        # but if it s = r*n, we shall find at least one s which is concatenated by last (n-1) r in first s, and first r in second s
        #
        # O(n) for str.find(), 92%
        #
        # O(n) for str.find(), 96%
        ss = s+s
        return ss.find(s,1,len(ss)-1) != -1
        
        


if __name__ == '__main__':
    s = Solution()
    tc = ["abab","aba","abcabcabcabc"]
    an = [True,False,True]
    for i in range(len(tc)):
        print(s.repeatedSubstringPattern(tc[i]))
        assert(s.repeatedSubstringPattern(tc[i]) == an[i])
