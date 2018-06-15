"""
https://leetcode.com/problems/construct-string-from-binary-tree/description/

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # Approach #1, dfs, pre-order, with careful placement of (,)
        # () must be removed for non-necessary items
        # so it must be placed outside the dfs(node)
        # O(n), 12%
        self.ans = ""
        def dfs(node):
            self.ans += str(node.val)
            if node.left:
                self.ans += "("
                dfs(node.left)
                self.ans += ")"
            elif node.right:
                self.ans += "()"

            if node.right:
                self.ans += "("
                dfs(node.right)
                self.ans += ")"
        
        if t: dfs(t)
        return self.ans

if __name__ == '__main__':
    s = Solution()
    tc  = [ [1,2,3,4],  [1,2,3,None,4]]
    ans = [ "1(2(4))(3)", "1(2()(4))(3)"]
    from helper import TestHelper
    th = TestHelper()
    for i in range(len(tc)):
        t = th.listToBinaryTree(tc[i])
        r = s.tree2str(t)
        print (r)
        assert(r == ans[i])
