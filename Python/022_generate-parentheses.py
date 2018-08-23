"""
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
xrange = range
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Approach #1, recursion
        #
        # keep track of (left, right) pair
        # n nairs =  n-1 pairs  + () in any sequence by following:
        #  add ( if left < n
        #  only add ) when left > right
        #
        #
        #
        ans = []
        def gen(a, left, right):
            if len(a) == 2*n:
                ans.append(a)
            if left < n:
                gen(a+'(', left+1,right)
            if left > right:
                gen(a+')', left, right+1)
                
        gen("",0,0)

        return ans



if __name__ == '__main__':
    s = Solution()
    tc =  [ 3,4 ]
    ans = [ [  "((()))",  "(()())",  "(())()",  "()(())",  "()()()"],["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"] ]
    for i in range(len(tc)):
        r = s.generateParenthesis(tc[i])
        print(r)
        assert(r == ans[i])
