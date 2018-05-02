""" 
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach 1: Brute force, DFS and save max-depth
        # 78ms, 9%
        if root == None: return 0
        if root.left == None and root.right == None : return 1
        if root.left == None: return 1 + self.maxDepth(root.right)
        if root.right == None: return 1 + self.maxDepth(root.left)
        return 1+max(self.maxDepth(root.right), self.maxDepth(root.left))


        
        
s = Solution()
#test_case = [[1,2,3,0,0,0],[2,5,6]]
t = [3,9,20,null,null,15,7]
#i = [[1,2,3,0,0,0],[2,5,6]]
#for in in test_case:

print(s.maxDepth(t))

