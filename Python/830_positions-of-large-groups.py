"""
https://leetcode.com/problems/positions-of-large-groups/description/

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]


Note:  1 <= S.length <= 1000



"""
xrange = range
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        # Approach #1, naive
        #
        # use list to remember info
        #
        # Input: "abbxxxxzzy"
        #        d['x'] = [3,6]
        #  
        #  O(n), 77ms
        #
        #S = list(S)
        start= 0
        current = S[0]
        ans = []
        for i, c in enumerate(S):
            if c != current:
                if i - start >=3: # aaab 0123
                    ans.append( [start, i-1] )
                start = i
                current = c
        # check the ending bbb 789
        if i - start >=2 :
            ans.append( [start, i] )
        return ans



if __name__ == '__main__':
    s = Solution()
    tc =  [ "nnnhaaannnm"      , "babaaaabbb" , "abbxxxxzzy",  "abc", "abcdddeeeeaabbbcd"   , "aaa"  , "aa" ]
    ans = [ [[0,2],[4,6],[7,9]], [[3,6],[7,9]], [[3,6]]     ,   []  , [[3,5],[6,9],[12,14]] , [[0,2]], []  ]
    for i in range(len(tc)):
        r = s.largeGroupPositions(tc[i])
        print (r)
        assert(r == ans[i])
