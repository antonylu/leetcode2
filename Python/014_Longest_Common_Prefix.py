# https://leetcode.com/problems/longest-common-prefix/description/
# 
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# Note:
# All given inputs are in lowercase letters a-z.
import os
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # brute force, iterative
        # os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
        # O(n), beats 63.6% 42ms
        if not strs: return ''

        cp = strs[0]
        for s in strs:
            cp = os.path.commonprefix([cp, s])

        return cp

s = Solution()
print(s.longestCommonPrefix(["flower","flow","floeright"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))


