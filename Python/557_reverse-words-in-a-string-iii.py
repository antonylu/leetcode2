"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach #1,
        # split word, revese, " ".join()
        #
        # O(n) 80%
        return " ".join([ i[::-1] for i in s.split() ])

if __name__ == '__main__':
    s = Solution()
    tc  = ["Let's take LeetCode contest"]
    ans = ["s'teL ekat edoCteeL tsetnoc"]

    for i in range(len(tc)):
        r = s.reverseWords(tc[i])
        print (r)
        assert(r == ans[i])
