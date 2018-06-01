"""
https://leetcode.com/problems/license-key-formatting/description/

You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.


Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
"""
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # Approach #1a, naive
        #
        # split S from right part for every K chars
        #
        # "5F3Z2E9W", 4, len = 8, S[4:8], S[0:4]
        # "25G3J", 2, len = 5, S[3:5], S[1:3],  S[0:1]
        #
        # Time  O(n)
        # Space O(1)
        # remove list, process within one phase
        #
        # 15%
        S = S.replace('-','').upper()
        size = len(S)
        result = ""
        while size >= K:
            result = S[size-K:size] + "-" + result 
            size = size - K
        if size >0:
            result = S[:size] + "-" + result
        return result[:len(result)-1]

    def licenseKeyFormatting2(self, S, K):
        # Approach #1, naive
        #
        # split S from right part for every K chars
        #
        # "5F3Z2E9W", 4, len = 8, S[4:8], S[0:4]
        # "25G3J", 2, len = 5, S[3:5], S[1:3],  S[0:1]
        #
        # Time  O(n)
        # Space O(n)
        # 50ms, 83%
        S = S.replace('-','').upper()
        size = len(S)
        ans = []
        while size >= K:
            ans.append(S[size-K:size])
            size = size - K
        if size > 0:
            ans.append(S[:size])
        return '-'.join(ans[::-1])

        


if __name__ == '__main__':
    s = Solution()
    tc = [("5F3Z-2e-9-w", 4),("2-5g-3-J", 2)]
    an = ["5F3Z-2E9W","2-5G-3J"]
    for i in range(len(tc)):
        print (s.licenseKeyFormatting2(tc[i][0],tc[i][1]))
        #assert(s.licenseKeyFormatting2(tc[i][0],tc[i][1]) == an[i])
