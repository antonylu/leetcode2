""" 
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Approach 2, use deque for BFS
from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach 1: brute force, recursive
        # if not root: return 0
        # return min(self.minDepth(root.left), self.minDepth(root.right))+1
        
        # Approach 2: BFS, return depth when a leaf is found.
        # if a node has no children, return the first found depth
        # Note: A leaf is a node with no children.
        # 100% 53ms
        if not root: return 0
        q = deque([root])
        depth = 1
        while len(q) > 0:
            level_nodes_number = len(q)
            for i in range(level_nodes_number ):
                n = q.popleft()
                if not n.left and not n.right: return depth
                if n.left  : q.append(n.left)
                if n.right : q.append(n.right)
            depth +=1
        return depth

if __name__ == "__main__":
    import helper
    null = None
    tc = [[3,9,20,null,null,15,7],[1,2]]
    s = Solution()
    t = helper.TestHelper()
    for test in tc:
        root = t.listToBinaryTree(test)
        print(s.minDepth(root))

