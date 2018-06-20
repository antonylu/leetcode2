"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node.
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach #3, DFS
        # O(n),30%
        self.minimum_1st = root.val
        self.minimum_2nd = 2147483648

        def dfs(node):
            if node.val >self.minimum_1st and node.val <  self.minimum_2nd:
                self.minimum_2nd = node.val
            if node.left : dfs(node.left)
            if node.right: dfs(node.right)

        dfs(root)

        if self.minimum_2nd != 2147483648: return self.minimum_2nd
        return -1


        # Approach #1, traverse, set, sort, 2nd smallest

        # Approach #2, BFS
        # the root is the smallest
        # BFS and find a larger one > root.val
        # if not found, -1
        # O(n), 6%
        # improve by removing level check
        # O(n), 97%
        if not root: return -1

        from collections import deque
        q = deque([root])
        minimum_1st = root.val
        minimum_2nd = 2147483648
        while len(q) > 0:
            node = q.popleft()
            if node.val >minimum_1st and node.val <  minimum_2nd:
                minimum_2nd = node.val
            if node.left : q.append(node.left)
            if node.right: q.append(node.right)
        if minimum_2nd != 2147483648: return minimum_2nd
        return -1




if __name__ == '__main__':
    s = Solution()
    tc  = [ [2,2,5,None,None,5,7],[2,2,2],[1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1] ]
    ans = [ 5,-1,2 ]
    from helper import TestHelper
    th = TestHelper()

    for i in range(len(tc)):
        t = th.listToBinaryTree(tc[i])
        r = s.findSecondMinimumValue(t)
        print (r)
        assert(r == ans[i])
