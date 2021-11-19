"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach #1: memorization
            sort each word, add to dict, sorted word as key, append original word to value list
            generate result from dict

            O(m) x O(n log n) sorted
            python3 100ms, 66%
            python2 68ms, 99.83%
        """
        d = defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            d[k].append(s)
        return [v for v in d.values()]


if __name__ == '__main__':
    s = Solution()
    tcs =  [["eat","tea","tan","ate","nat","bat"],       [""],   ["a"]  ] 
    ans = [[["ate","eat","tea"],["nat","tan"],["bat"]], [[""]], [["a"]]]
    for i in range(len(tcs)):
        r = s.groupAnagrams(tcs[i])
        print (r)
        #assert(r == ans[i])
