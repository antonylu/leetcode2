"""
https://leetcode.com/problems/detect-capital/description/

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Approach #1, Naive
        # 
        # 1st, don't care
        # 2nd, if 1st lower, 2nd must be lower
        # 3rd~, if 1st and 2nd upper, must be upper
        #     , if 1st upper and 2nd lower, must be lower
        #     , if 1st lower, must be lower
        #  
        
        # Approach #2, regex
        #
        #  * all upper: ^[A-Z]+$
        #  * first upper and others are lower: ^[A-Z][a-z]*$
        #  * all lower: ^[a-z]+$
        #  
        #  O(n), 25%
        import re
        p1 = r"^[A-Z]+$"
        p2 = r"^[A-Z][a-z]*$"
        p3 = r"^[a-z]+$"
        if re.match(p1, word) or re.match(p2,word) or re.match(p3,word):
            return True
        else:
            return False
        


if __name__ == '__main__':
    s = Solution()
    tc = ["USA", "FlaG", "G", "g", "False"]
    an = [True, False, True, True, True]
    for i in range(len(tc)):
        print (s.detectCapitalUse(tc[i]))
        #assert(s.detectCapitalUse(tc[i])== an[i])
