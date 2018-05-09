""" 
https://leetcode.com/problems/valid-palindrome/description/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Approach #1, brute force
        # compare character by character, with min and max index
        # ignore any non-alphanumeric characters.
        # O(n)

        # Approach #2, brute force
        # strip non alphanumeric
        # if len(s)%2 == 1: return False
        # reverse s[:mid], compare with s[mid:]
        # O(?n), time > Approach #1
        # 54ms, 99%
        if not s: return True
        import re
        pattern = re.compile('[\W]+')
        s = pattern.sub('', s)
        s = s.upper()
        (mid,odd) = divmod(len(s),2)
        s1 = s[:mid]
        if odd: 
            s2 = s[:mid:-1]
        else:
            s2 = s[:mid-1:-1]
        
        return s1 == s2
        
        


if __name__ == "__main__":
    tc  = ["A man, a plan, a canal: Panama", "race a car",""]
    ans = [True, False,True]
    s = Solution()
    for i,t in enumerate(tc):
        print (s.isPalindrome(t))
        if(s.isPalindrome(t) != ans[i]): print("incorrect: ",i,t)

