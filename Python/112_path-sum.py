""" 
https://leetcode.com/problems/path-sum/description/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Approach #1, DFS, recursively replace val with sum
        # if None, return False
        # for every node, sum = val + parent's val
        # if no child, return True if val == sum
        # if has child, return hasPathSum(left) or hasPathSum(right)
        
        # Approach #2, DFS, recursively check if child has sum
        # check child with sum = sum - val
        # if no child (left==right==None), return true if sum = val
        # if has child, return hasPathSum(left) or hasPathSum(right)
        # if None, return False
        # 58ms, 94%
        if not root: return False
        if not root.left and not root.right: return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

if __name__ == "__main__":
    import helper
    null = None
    tc = [[5,4,8,11,None,13,4,7,2,None,None,None,1]]
    s = Solution()
    t = helper.TestHelper()
    for test in tc:
        root = t.listToBinaryTree(test)
        print(s.hasPathSum(root,22))

