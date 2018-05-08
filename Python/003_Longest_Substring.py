# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# 
# Given a string, find the length of the longest substring without repeating characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# 
# 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach #1, brute force, 
        # search character s[j] in s[i,j]
        # if not found, next
        # if found at k, maximum = max(maximum, j-i). i = k
        # Python 2: 106ms, 66%
        # Python 3: 84ms, 92%
        length = len(s)
        if length <2: return length
        maximum = 0
        i = 0
        for j in range(1,length):
            k = s.find(s[j],i,j)
            if ( k >=0 ): # found
               maximum = max(maximum, j-i) 
               i = k+1
        maximum = max(maximum, j-i+1) 
        return maximum
        

s=Solution()
tc=["abcabcbb","bbbbb", "pwwkew","c","au","abcd"]
for t in tc:
    print(s.lengthOfLongestSubstring(t))