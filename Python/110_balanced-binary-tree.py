""" 
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # The depth of the two subtrees of every node <=1
        # Approach 1: divide and conqure, if a tree isBlanced based on the two subtrees are balanced tree
        # 

        # Approach 2: divide and conqure, if a tree is balanced, the depths difference of left and right subtrees <=1
        # otherwise, not a balanced tree
        # 87%, 70ms
        return self.balanced_depth(root) != -1
    # return max depth of a tree, return -1 if not balanced
    def balanced_depth(self, node):
        if not node: return 0
        left_depth = self.balanced_depth(node.left)
        right_depth = self.balanced_depth(node.right)
        
        if left_depth  == -1 or right_depth == -1 or abs(right_depth - left_depth) > 1:
            return -1
        else:
            return max(left_depth,right_depth) + 1
        


if __name__ == "__main__":
    import helper
    null = None
    tc = [[3,9,20,null,null,15,7],[1,2,2,3,3,null,null,4,4]]
    s = Solution()
    t = helper.TestHelper()
    for test in tc:
        root = t.listToBinaryTree(test)
        print(s.isBalanced(root))

