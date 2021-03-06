""" 
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Approach 1a: 
        # BFS, append to list
        # O(n), 38%, 51ms
        if not root: return []
        q = deque([root])
        list = []
        while (len(q)>0):
            subList = []
            level_number = len(q)
            for i in range(level_number):
                n = q.popleft()
                subList.append(n.val)
                if (n.left): q.append(n.left)
                if (n.right): q.append(n.right)
            list.append(subList)
        return list
        # Approach 2:
        # use List instead of deque because each iteration just handle One each level
        # perhaps performance would be better (?)

if __name__ == "__main__":
    import helper
    t = helper.TestHelper()
    test = [3,9,20,None,None,15,7]
    root = t.listToBinaryTree(test)

    s = Solution()
    print(s.levelOrder(root))
