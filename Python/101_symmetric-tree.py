""" 
https://leetcode.com/problems/symmetric-tree/description/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Approach 1: recursion, return False if check fail. Else return isSymmetric(left,right) and isSymmetric(right)
        # 92%, 43ms
#        if root == None: return True
#        return self.isSymmetricTree(root.left,root.right)
#        
#    def isSymmetricTree(self, p, q):
#        """
#        :type p: TreeNode
#        :type q: TreeNode
#        :rtype: bool
#        """
#        # Approach 3: recursive, optimize
#        # O(n), 97%
#        if p == None and q == None: return True
#        if bool(p) ^ bool(q) : return False
#        if p.val != q.val : return False
#        return self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left)

        # Approach 4: iteration, use stack to do DFS recursion, return False if check fail 
        # 71%, 45ms
        if root == None: return True
        s = [[root.left,root.right]]
        while (len(s)>0):
            [p,q] = s.pop()
            if p == None and q == None: continue
            if bool(p) ^ bool(q) : return False
            if p.val != q.val : return False
            s.append([p.left,q.right])
            s.append([p.right,q.left])
        return True


        
s = Solution()
#test_case = [[1,2,3,0,0,0],[2,5,6]]
i = [[1,2,3,0,0,0],[2,5,6]]
#for in in test_case:

s.merge(i[0],3,i[1],3)
print(i[0])

