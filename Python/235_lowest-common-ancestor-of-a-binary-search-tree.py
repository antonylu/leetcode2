"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:
Input: root, p = 2, q = 8
Output: 6 
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root, p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
             according to the LCA definition.
"""
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Approach #1, 
        # as a BST, 
        #   all values in left  subtrees < root.val
        #   all values in right subtrees > root.val
        # so, the common ancestor must be   p <= LCA <= q
        # if p < node and q < node: search left
        # if p > node and q > node: search right
        # else: LCA
        # 54%
        a = p.val
        b = q.val
        while root:
            r = root.val
            if   a < r and b < r:
                root = root.left
            elif a > r and b > r:
                root = root.right
            else: 
                return root
                
if __name__ == "__main__":
    null = None
    test = [6,2,8,0,4,7,9,null,null,3,5]
    #test = [2,1]
    tc   = [(2,1),(2,8),(2,4)]
    import helper
    l = helper.TestHelper()
    root = l.listToBinaryTree(test)
    s = Solution()
#    for t in tc:
#        print((s.lowestCommonAncestor(root,TreeNode(2),)).val)
