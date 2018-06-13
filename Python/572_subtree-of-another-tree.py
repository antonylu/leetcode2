"""
https://leetcode.com/problems/subtree-of-another-tree/description/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # Approach #2, serialize then compare
        # pre-order DFS every node, convert to preorder list or string.
        # note that None and level shall be represented by special characters
        #
        # O(n), 91%
        #
        def preOrder(node): # to string
            if not node: return 'n'
            # separate node with ',' to avoid test case [12,2]
            return ','+"".join((str(node.val), preOrder(node.left), preOrder(node.right)))
        return preOrder(t) in preOrder(s)

        # Approach #1, brute-force
        # DFS every node, if node.val == t.val, check if sub-tree of node == sub-tree of t
        # O(n^2) worst, 19%
        #
        def sameTree(a,b):
            if not a and not b: return True
            if not a and b: return False
            if a and not b: return False
            if a.val != b.val: return False
            return sameTree(a.left, b.left) and sameTree(a.right,b.right)

        if not s: return False
        if sameTree(s,t): return True
        if self.isSubtree(s.left,t): return True
        if self.isSubtree(s.right,t): return True

        return False





if __name__ == '__main__':
    s = Solution()
    tc  = [ ([3,4,5,1,2,None,None],[4,1,2]),([12],[2])]#,([3,4,5,1,2,None,None,  None,None,0,None, None,None,None,None],[4,1,2])]
    ans = [ True, False, False ]
    from helper import BSTHelper
    th = BSTHelper()

    for i in range(len(tc)):
        t = th.listToBST(tc[i][0])
        ss = th.listToBST(tc[i][1])
        r = s.isSubtree(t,ss)
        print (r)
        assert(r == ans[i])
