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
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach #1, brute force
        # count every character of the word 
        # compare the occurances
        # O(n), 70%
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
        s1 = count(s)
        t1 = count(t)

        return s1 == t1
        
        
                
if __name__ == "__main__":
    tc = [("anagram", "nagaram"),("rat","car"),("car","arc") ]
    s = Solution()
    for t in tc:
        print(s.isAnagram(t[0],t[1] ) )
