"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/


Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach #1, naive brute force
        # 
        # DFS traverse all nodes n, find it's closest two values n> and <n
        # Since it is a BST, its nearest ist
        #  * Left sub-tree's right most leave
        #  * Right sub-tree's left most leave
        #  O(n), 36%
        self.ans = float("inf")
        def biggest(node):
            big = node
            while big.right: big = big.right
            return big.val
            
        def smallest(node):
            small = node
            while small.left: small = small.left
            return small.val
            
        def dfs(node):
            if node.left:
                self.ans = min(self.ans, node.val - biggest(node.left))
                dfs(node.left)
            if node.right:
                self.ans = min(self.ans, smallest(node.right) - node.val)
                dfs(node.right)
        dfs(root)
        return self.ans
        
        


if __name__ == '__main__':
    s = Solution()
    tc = [[1,None,3,2],[1,None,3,2,5]]
    an = [1]
    import helper
    th = helper.BSTHelper()

    for i in range(len(tc)):
        #print(tc[i])
        t = th.listToBST(tc[i])
        #print(th.BSTtoList(t))
        print (s.getMinimumDifference(t))
        #assert(s.getMinimumDifference(t) == an[i])
