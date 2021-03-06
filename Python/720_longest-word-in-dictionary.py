"""
https://leetcode.com/problems/longest-word-in-dictionary/description/

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"

Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"

Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Approach #1, brute-force with set
        #
        # put to a set, from longest, check all substring in set
        # sort the words first, so that:
        #  a. longest length first, longest to shortest, len decreasing
        #  b. when length is the same, alphabetical increasing
        #
        # sort two times,
        #  b. words.sort()
        #  a. words.sort(key=len, reverse=True)
        #
        # remove those words with length > len(words)
        # from longest word, find existence of one char by a time
        # longest word, lexicographical order
        #
        # O(n log n), 97%
        length = len(words)

        words.sort()
        words.sort(key=len, reverse = True)
        s = set(words)
        def isValid(word):
            for i in range(len(word)):
                if word[:i+1] not in s: return False
            return True

        for word in words:
            if len(word) > length: continue # remove invalid
            if isValid(word): return word
        return ""



if __name__ == '__main__':
    s = Solution()
    tc = [["w","wo","wor","worl", "world"], ["a", "banana", "app", "appl", "ap", "apply", "apple"],[],["a"]]
    ans = ["world", "apple","","a"]

    for i in range(len(tc)):
        r = s.longestWord(tc[i])
        print (r)
        assert(r == ans[i])
