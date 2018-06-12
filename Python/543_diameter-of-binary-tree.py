"""
https://leetcode.com/problems/diameter-of-binary-tree/description/

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach #1, divide and conquer
        #
        # reconsider the problem as to find out the the longest path bettwen a node,
        # so the anser is longest path of left sub-tree + longest path of right sub-tree
        # in that case, reuse 104's answer and traverse all the nodes for max left+ max right
        # O(n^2)
        #

        # Approach #2, divide and conquer
        #
        # reconsider the problem as to find out the the longest path bettwen a node,
        # so the anser is longest path of left sub-tree + longest path of right sub-tree
        #
        # since we need to get left/right first, we need to traversal "post-order DFS"
        # reuse 104 by DFS returning maximum length, keep the maximum diameter with left+right at the same time
        #
        # post-order dfs, return maximum depth and remember maximum diameter
        #
        # O(n), 67%
        self.diameter = 0
        def dfs(node):
            if not node: return 0
            left  = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left+right)
            return 1+max(left,right)
        if root: dfs(root)
        return self.diameter

if __name__ == '__main__':
    s = Solution()
    tc  = [[1,2,3,4,5,None,None],[]]
    ans = [3,0]
    from helper import TestHelper
    th = TestHelper()

    for i in range(len(tc)):
        t = th.listToBinaryTree(tc[i])
        r = s.diameterOfBinaryTree(t)
        print (r)
        assert(r == ans[i])
