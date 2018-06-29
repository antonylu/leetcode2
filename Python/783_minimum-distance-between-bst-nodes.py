"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.

"""
xrange = range
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach #1, pre-order DFS
        # enumerate left-subtree's right-most-leaf - node, node - right-subtree's left-most-leaf
        # O(n), 35%
        candidate = []
        def rightMostLeaf(node):
            if node.right:
                return rightMostLeaf(node.right)
            else:
                return node.val
        def leftMostLeaf(node):
            if node.left:
                return leftMostLeaf(node.left)
            else:
                return node.val
        def dfs(node):
            if node.left :
                candidate.append(node.val-rightMostLeaf(node.left))
                dfs(node.left)
            if node.right:
                candidate.append(leftMostLeaf(node.right)-node.val)
                dfs(node.right)

        if root: dfs(root)

        return min(candidate)


if __name__ == '__main__':
    s = Solution()
    tc =  [[4,2,6,1,3,None,None]]
    ans = [  1]
    from helper import BSTHelper

    bsth = BSTHelper()

    for i in range(len(tc)):
        bst = bsth.listToBST(tc[i])
        r = s.minDiffInBST(bst)
        print (r)
        assert(r == ans[i])
