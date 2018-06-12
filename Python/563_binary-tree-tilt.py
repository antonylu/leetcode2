"""
https://leetcode.com/problems/binary-tree-tilt/description/

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach #1, DFS to get sum, post-order to accumulate tilt
        #
        # O(n), 67%
        #
        self.tilt = 0
        def dfsSum(node):
            if not node: return 0
            left  = dfsSum(node.left)
            right = dfsSum(node.right)
            self.tilt += abs(left - right)
            return left+right+node.val

        dfsSum(root)
        return self.tilt


if __name__ == '__main__':
    s = Solution()
    tc  = [[1,2,3],[1,2,3,4,5,6,7]]
    ans = [1,7]
    from helper import TestHelper
    th = TestHelper()

    for i in range(len(tc)):
        t = th.listToBinaryTree(tc[i])
        r = s.findTilt(t)
        print (r)
        assert(r == ans[i])
