"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""
xrange = range
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach #1, brute-force
        #
        # define a isPalindrome()
        # enumerate all possibilities from len(s), len(s)-1 ... 0
        #    C(n,2) = n(n-1)/2, O(n^2)
        # isPalindrome(), O(n)
        #
        # O(n^3)

        # Approach #2, center and expand palindrome
        #
        # Take every index as center O(n), expand and find maximum palindrom
        # The starting point may be odd or even number of letters, say "a" or "aa" expand => "bab", "baab"
        #
        # expand palindrome to maximum takes O(n), check s[left-1] == s[right+1]
        #
        # overall O(n^2), 75%
        #
        def expandPalindrome(left,right):
            while left>=0 and right < len(s) and s[left] == s[right]: # "babad"
                left  -=1
                right +=1
            return s[left+1:right]

        ans = ""
        for i in xrange(len(s)):
            s1 = expandPalindrome(i,i) # "bab"
            if len(s1) >len(ans): ans = s1
            s2 = expandPalindrome(i,i+1) # "baab"
            if len(s2) >len(ans): ans = s2

        return ans

if __name__ == '__main__':
    s = Solution()
    tc =  [ "a", "babad", "cbbd" ]
    ans = [ "a", "bab", "bb" ]
    for i in range(len(tc)):
        r = s.longestPalindrome(tc[i])
        print (r)
        assert(r == ans[i])
