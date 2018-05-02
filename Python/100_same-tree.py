""" 
https://leetcode.com/problems/same-tree/description/

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Approach 1: brute force, 
        # 1. traverse tree into list, recursively
        # 2. compare list

        # Approach 2: brute force, compare one by one, return false when !=

        # Approach 3: recursive
        # O(n), 58%
        if p == None and q == None: return True
        if p == None and q != None: return False
        if p != None and q == None: return False
        if p.val != q.val : return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Approach 3: recursive, optimize
        # O(n), 97%
        if p == None and q == None: return True
        if bool(p) ^ bool(q) : return False
        if p.val != q.val : return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
s = Solution()
#test_case = [[1,2,3,0,0,0],[2,5,6]]
i = [[1,2,3,0,0,0],[2,5,6]]
#for in in test_case:

s.merge(i[0],3,i[1],3)
print(i[0])

