"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

"""
xrange = range
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Approach #1, naive
        #
        # 2: abc
        # 3: def
        # 4: ghi
        # 5: jkl
        # 6: mno
        # 7: pqrs
        # 8: tuv
        # 9: wxyz
        #
        # O(3^n), 100%
        #
        if digits == "": return []

        buttons = [ "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for i in digits: # "23"
            tmp = []
            for j in buttons[int(i)]: #"abc"
                tmp.extend( [c+j for c in ans])
            ans = tmp
        return sorted(ans)

if __name__ == '__main__':
    s = Solution()
    tc =  [ "23", ""]
    ans = [ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], [] ]
    for i in range(len(tc)):
        r = s.letterCombinations(tc[i])
        print (r)
        assert(r == ans[i])
