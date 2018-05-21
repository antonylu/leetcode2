"""
https://leetcode.com/problems/binary-tree-paths/description/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # Approach #1,  DFS, recursion
        # when leaf, append current path in ans[]
        # 
        # O(n), 65%
        ans = []
        path = []
        def go(root):
            path.append(root.val)
            if not root.left and not root.right:
                # append path string to ans
                s = str(path[0])
                for i in range(1,len(path)):
                    s+= "->"
                    s+= str(path[i])
                ans.append(s)
            if root.left:  go(root.left)
            if root.right: go(root.right)
            path.pop()
        if not root: return ans
        go(root)
        return ans

if __name__ == "__main__":
    tc = [1,2,3,None,5,None,None]
    s = Solution()
    import helper
    th = helper.TestHelper()
    r = th.listToBinaryTree(tc)
    print(s.binaryTreePaths( r ) )
