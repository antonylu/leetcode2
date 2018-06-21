"""
https://leetcode.com/problems/repeated-string-match/description/

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach #2, improved DFS
        # 1 loop check 
        # reuse solution of 543 diameter of a binary tree
        #
        # post-order DFS, get left and right longest univalue path (LUP)
        #
        # if node.val == node.left.val, reuse left+1
        # otherwise, left = 0
        #
        # O(n), 58%
        self.ans = 0
        def dfs(node):
            if not node: return 0
            left  = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val == node.val:
                left = left +1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right = right +1
            else:
                right = 0
            
            self.ans = max(self.ans, left+right)
            return max(left,right)
        
        if root: dfs(root)
        return self.ans
        

        # Approach #1, brute-force
        # treat the question as find the LUP through a specific node
        # then apply to every node by traversal
        #
        # O(n*m), 1.64%
        self.ans = 0
        def lup(node): # return LUP of the node
            left  = 0
            right = 0
            if node.left  and node.left.val  == node.val: left  = lup(node.left)
            if node.right and node.right.val == node.val: right = lup(node.right)
            self.ans = max(self.ans, left+right)
            return max(left,right)+1
        def dfs(node):
            lup(node)
            if node.left:  dfs(node.left)
            if node.right: dfs(node.right)

        if not root: return 0
        
        dfs(root)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    tc  = [ [5,4,5,1,1,None,5], [1,4,5,4,4,None,5] ]
    ans = [ 2,2 ]
    from helper import TestHelper
    th = TestHelper()

    for i in range(len(tc)):
        t = th.listToBinaryTree(tc[i])
        r = s.longestUnivaluePath(t)
        print (r)
        #assert(r == ans[i])
