""" 
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Approach 2: 
        # level order: 0 -3 9 -10 5
        # pre order: 0 -3 -10 9 5
        # inorder: -10 -3 0 5 9
        # looks like an inorder revers to tree
        # decide root in the middle, use DFS
        # nums[len//2] as root, divide left/right as two sub-trees
        # Similar to binary search, min, mid, max
        # create tree recursively
        # O(n) 8% 129ms
        max = len(nums)
        if max == 0: return None
        mid = max//2
        node = TreeNode(nums[mid])
        if max == 1: return node
        node.left = self.sortedArrayToBST(nums[0:mid])
        if max == 2: return node
        node.right = self.sortedArrayToBST(nums[mid+1:max])
        return node



        # Approach 1: brute force, BFS and grow nodes
        # However, the answer needs highly matched
        # Wrong Answer
        # import deque from collections
        # l = len(nums)
        # if(l==0): return None
        # root = TreeNode(nums[0])
        # q = deque([])
        # curr_node = root
        # for i in range(1,l):
        #     node = TreeNode(nums[i])
        #     q.append(node)
        #     if (not curr_node.left): 
        #         curr_node.left = node
        #     else:
        #         curr_node.right = node
        #         curr_node = q.popleft()
        # return root
        

if __name__ == "__main__":
    import helper
    t = helper.TestHelper()
    test = [-10,-3,0,5,9]
    root = t.listToBinaryTree(test)

    s = Solution()
    print(s.sortedArrayToBST(root))
