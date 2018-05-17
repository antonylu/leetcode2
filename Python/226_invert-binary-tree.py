"""
https://leetcode.com/problems/invert-binary-tree/description/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Approach #1, DFS, switch left/right
        # recursive with stack
        # 35ms, 67%

        if not root: return root
        # pre-order
        tmp = root.left
        root.left  = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


        # Approach #1, BFS, switch left/right
        # use deque
        # 33ms, 83%
        from collections import deque
        if not root: return root
        q = deque([root])
        while(len(q)>0):
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                tmp = node.left
                node.left = node.right
                node.right = tmp
        return root
        
        



if __name__ == "__main__":
    import helper
    null = None
    tc = [[4,2,7,1,3,6,9]]
    a  = [[4,7,2,9,6,3,1]]
    s = Solution()
    t = helper.TestHelper()
    for test in tc:
        print(test)
        root = t.listToBinaryTree(test)
        r=t.binaryTreeToList(s.invertTree(root))
        print(r)
        assert(r == a[0])
    