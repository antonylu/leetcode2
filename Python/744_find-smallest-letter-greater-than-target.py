"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

"""
import bisect
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Approach #1a, binary search
        #
        # O(log n), 100%
        #
        i = bisect.bisect_right(letters,target)
        return letters[i%len(letters)]

        # Approach #1, binary search
        #
        # O(log n), 79%
        #
        from bisect import bisect_right
        i = bisect_right(letters,target)
        if i == len(letters): i = 0
        return letters[i]






if __name__ == '__main__':
    s = Solution()
    tc =  [ (["c", "f", "j"], "a" ),(["c", "f", "j"], "c" ),(["c", "f", "j"], "d" ),(["c", "f", "j"], "g" ),(["c", "f", "j"], "j" ),(["c", "f", "j"], "k" ) ]
    ans = [  "c","f", "f", "j", "c", "c"  ]

    for i in range(len(tc)):
        r = s.nextGreatestLetter(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])
