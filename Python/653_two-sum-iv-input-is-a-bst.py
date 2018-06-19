"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # Approach #1, DP+DFS
        # DFS and remember in k-n.val in set s
        # return true if any n.val in set s
        # O(n), 29%
        self.set = set()
        self.ans = False
        def dfs(node):
            if node.val in self.set:
                self.ans = True
            else:
                self.set.add(k - node.val)
            if node.left : dfs(node.left)
            if node.right: dfs(node.right)

        if root: dfs(root)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    tc  = [ ([5,3,6,2,4,None,7],9),([5,3,6,2,4,None,7],28)]
    ans = [ True,False ]
    from helper import TestHelper
    th = TestHelper()

    for i in range(len(tc)):
        t = th.listToBinaryTree(tc[i][0])
        r = s.findTarget(t,tc[i][1])
        print (r)
        #assert(r == ans[i])
