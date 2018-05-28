"""
https://leetcode.com/problems/sum-of-left-leaves/description/

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach #1, BFS with deque
        # enqueue with touple (TreeNode, isLeft)
        # O(n), 64%
        from collections import deque
        if not root: return 0
        q = deque([(root, False)])
        sum = 0
        while(len(q)>0):
            (n, isLeft) = q.popleft()
            if(isLeft and not n.right and not n.left):
                sum += n.val
            if(n.left):
                q.append((n.left,True))
            if(n.right): 
                q.append((n.right,False))
        return sum

if __name__ == '__main__':
    s = Solution()
    tc = [[],[3,9,20,None,None, 15, 7]]
    from helper import TestHelper
    th = TestHelper()
    for t in tc:
        r = th.listToBinaryTree(t)
        print(s.sumOfLeftLeaves(r))
