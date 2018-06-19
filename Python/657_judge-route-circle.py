"""
https://leetcode.com/problems/judge-route-circle/description/

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
"""
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Approach #1
        # Count string
        # L = R
        # U = D
        # O(n),66%
        from collections import Counter
        c = Counter(moves)
        return c['R'] == c['L'] and c['U'] == c['D']
        


if __name__ == '__main__':
    s = Solution()
    tc  = ["UD","LL","","ULRD","ULRDD"]
    ans = [ True,False,True,True,False ]

    for i in range(len(tc)):
        r = s.judgeCircle(tc[i])
        print (r)
        assert(r == ans[i])
