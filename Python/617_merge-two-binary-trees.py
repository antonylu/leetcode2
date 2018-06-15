"""
https://leetcode.com/problems/merge-two-binary-trees/description/

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Approach #2, DFS
        #
        # O(n),99%
        if not t1: return t2
        if not t2: return t1
        t1.val += t2.val
        t1.left  = self.mergeTrees(t1.left,  t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        

        # Approach #1, serialize
        # convert to list
        # add items
        # convert to tree
        from helper import TestHelper
        helper = TestHelper()
        a1 = helper.binaryTreeToList(t1)
        a2 = helper.binaryTreeToList(t2)
        length = min(len(a1),len(a2))
        print(a1,a2)
        ans = []
        for i in range(length):
            if a1[i] and a2[i]:
                ans.append(a1[i]+a2[i])
            elif a1[i]:
                ans.append(a1[i])
            elif a2[i]:
                ans.append(a2[i])
        return helper.listToBinaryTree(ans)


if __name__ == '__main__':
    s = Solution()
    tc  = [ ([1,3,2,5],[2,1,3,None,4,None,7])]
    ans = [ [3,4,5,5,4,7]]
    from helper import TestHelper
    th = TestHelper()
    for i in range(len(tc)):
        ta = th.listToBinaryTree(tc[i][0])
        tb = th.listToBinaryTree(tc[i][1])
        r = s.mergeTrees(ta,tb)
        print (th.binaryTreeToList(r))
        #assert(r == ans[i])
