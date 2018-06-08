"""
https://leetcode.com/problems/convert-bst-to-greater-tree/description/


Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Approach #1, reverse in-order traversal
        #
        # Since it is a BST, the keys greater are all in parent and lef-subtress
        # Thus we need to use reverse in-order DFS
        # 
        # O(n), 82%
        self.sum = 0
        
        def dfs(node):
            if node.right:dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            if node.left:dfs(node.left)

        if root: dfs(root)

        return root

if __name__ == '__main__':
    s = Solution()
    tc  = [[5,2,13]]
    ans = [[18,20,13]]
    from helper import BSTHelper
    bts = BSTHelper()
    
    for i in range(len(tc)):
        t = bts.listToBST(tc[i])
        r = s.convertBST(t)
        print (bts.BSTtoList(r))
        #assert(r == ans[i])
