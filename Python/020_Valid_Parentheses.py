# https://leetcode.com/problems/valid-parentheses/description/
# 
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# Input: "()"
# Output: true
# Example 2:
# 
# Input: "()[]{}"
# Output: true
# Example 3:
# 
# Input: "(]"
# Output: false
# Example 4:
# 
# Input: "([)]"
# Output: false
# Example 5:
# 
# Input: "{[]}"
# Output: true
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # dict parenthese
        # brute-force, enumerative, push to stack if not closed
        # O(n) 20.92%, 51ms
        stack = []
        d = {'(':')', '{':'}', '[':']'}
        pre = '('
        for c in s:
            if len(stack) ==0:
                if c not in d.keys(): return False
                stack.append(c)
            else:
                pre = stack.pop()
                # print(pre)
                if c != d[pre]:
                    stack.append(pre)
                    if c not in d.keys(): return False
                    stack.append(c)

        return not stack


d = Solution()
print(d.isValid("()"))
print(d.isValid("()[]{}"))
print(d.isValid("(]"))
print(d.isValid("([)]"))
print(d.isValid("{[]}"))
print(d.isValid("){"))
