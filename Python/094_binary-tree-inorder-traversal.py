# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def inorderTraversal(self, root):
        self.ans = []
        def dfs(root):
            if not root: return None
            dfs(root.left)
            self.ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.ans
# BFS



if __name__ == "__main__":
    import helper
    t = helper.TestHelper()
    test = [1,None,2,3]
    root = t.listToBinaryTree(test)

    s = Solution()
    print(s.inorderTraversal(root))
