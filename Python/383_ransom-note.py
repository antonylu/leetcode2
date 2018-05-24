"""
https://leetcode.com/problems/ransom-note/description/

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Approach #2, use set()
        # search every letters use collections.Counter
        #
        # O(n), 86%
        r = set(ransomNote)
        for i in r:
            if ransomNote.count(i) > magazine.count(i): return False
        return True

        # Approach #1, naive,
        # use collections.Counter
        #
        # O(n), 20%
        from collections import Counter
        cN = Counter(ransomNote)
        cM = Counter(magazine)
        return len(cN-cM) == 0
                

if __name__ == '__main__':
    tc = [("a", "b"),("aa", "ab"),("aa", "aab"),("a","bcd")]
    ans = [False, False, True]
    s = Solution()
    for (i,j) in tc:
        print(s.canConstruct(i,j))


