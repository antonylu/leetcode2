"""
https://leetcode.com/problems/valid-palindrome-ii/description/

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True

Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Approach #1, brute-force
        # check palindrome for the string
        # if not, remove a char a check palindrome
        # O(n*n)

        # Approach #2, two pointers
        # With 2 pointers, point to the first and last char
        # check one by one, if not the same, get two candidates by removing first or last characters
        # check if one of the candidate is a palindrome
        # O(n), 88%
        def isPalindrome(s):
            (mid,odd) = divmod(len(s),2)
            s1 = s[:mid]
            if odd:
                s2 = s[:mid:-1]
            else:
                s2 = s[:mid-1:-1]
            return s1 == s2

        right = len(s) -1
        left  = 0
        while left < right:
            if s[left] != s[right]:
                # breaks two candidates
                c1 = s[left:right]
                c2 = s[left+1:right+1]
                return isPalindrome(c1) or isPalindrome(c2)
            else:
                left +=1
                right-=1
        return True



if __name__ == '__main__':
    s = Solution()
    tc  = [ "aba","abca","abcdeffedcba","abcdeffedcbaa","abcdeffedcbaab"]
    ans = [ True, True,True, True,False]

    for i in range(len(tc)):
        r = s.validPalindrome(tc[i])
        print (r)
        assert(r == ans[i])
