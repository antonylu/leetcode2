"""
https://leetcode.com/problems/trim-a-binary-search-tree/description/

Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2

Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # Approach #1, serialize
        # transform to list, crop the list based on (L,R)
        # recreate a Tree with the cropped list
        # O(n)
        
        # Approach #2, recursion
        # 
        #  ....L...R...
        #
        # if not root: return None
        # if root.val > R: return trimBST(root.left)
        # if root.val < L: return trimBST(root.right)
        # else: 
        #   root.left  = trimBST(root.left)
        #   root.right = trimBST(root.right)
        #  
        #  O(n), 98%
        #  
        if not root: return None
        if root.val > R: return self.trimBST(root.left,L,R)
        if root.val < L: return self.trimBST(root.right,L,R)
        root.left  = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right,L,R)
        return root



if __name__ == '__main__':
    s = Solution()
    tc  = [ ([1,0,2],1,2)],([3,0,4,None,2,None,None,None,None,1,None],1,3,) ]
    ans = [ [1,None,2],[3,2,None,1] ]
    from helper import BSTHelper
    th = BSTHelper()

    for i in range(len(tc)):
        t = th.listToBST(tc[i][0])
        r = s.trimBST(t,tc[i][1],tc[i][2])
        print (r)
        #assert(r == ans[i])
