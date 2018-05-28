"""
https://leetcode.com/problems/longest-palindrome/description/

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach #1, Greedy
        #
        # find the number of each characters [a~zA~Z]
        # add the biggest even number of each, then +1 if longestPalindrome < len(s)
        # O(n), 54%
        if len(s) <2: return len(s)
        from collections import Counter
        c = dict(Counter(s))
        ans = 0
        for k in c:
            ans += c[k]//2 * 2
        if ans < len(s):
            return ans +1
        else:
            return ans
        
            
        
if __name__ == '__main__':
    s = Solution()
    tc = ["abccccdd","aA","","aaAA","aaBb","aa","a","AB"]
    for t in tc:
        print(s.longestPalindrome(t))
