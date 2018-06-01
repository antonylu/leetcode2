"""
https://leetcode.com/problems/keyboard-row/description/

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Approach #1, use set()
        # 
        # O(n), 78%
        key1 = set("qwertyuiop")
        key2 = set("asdfghjkl")
        key3 = set("zxcvbnm")
        ans = []
        for w in words:
            ws = set(w.lower())
            if ws <= key1 or ws <= key2 or ws <= key3:
                ans.append(w)
        return ans
        


if __name__ == '__main__':
    s = Solution()
    tc = [["Hello", "Alaska", "Dad", "Peace"]]
    an = [["Alaska", "Dad"]]
    for i in range(len(tc)):
        print (s.findWords(tc[i]))
        #assert(s.findWords(tc[i]) == an[i])
