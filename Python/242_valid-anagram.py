"""
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

"""
class Solution(object):
    def isAnagram(self, s, t):
        # Approach #2, brute-force count every lowercase i s and t
        # if any of them different, return False
        #
        # 99%
        lower = 'abcdefghijklmnopqrstuvwxyz'
        for c in lower:
            if s.count(c) != t.count(c): return False
        return True

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach #1, brute force
        # count every character of the word 
        # compare the occurances
        # O(n), 70%
        # improve, 93%
        def count(s):
            """
            type s: str
            rtype: dict
            """
            dict = {}
            for c in s:
                if c in dict:
                    dict[c]+=1
                else:
                    dict[c]=0
            return dict
        return count(s) == count(t)
        
        
                
if __name__ == "__main__":
    tc = [("anagram", "nagaram"),("rat","car"),("car","arc") ]
    s = Solution()
    for t in tc:
        print(s.isAnagram(t[0],t[1] ) )
