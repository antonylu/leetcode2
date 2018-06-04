"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Approach #1, brute-force, one phase
        #  1. DFS all nocdes for all vals and count in dict
        #  2. find dict keys with maximum counts
        #  
        # Time  O(n), 18%
        # Space O(n)
        self.dict = {}
        self.max  = 0
        def dfs(node):
            self.dict[node.val] = 1 + self.dict.get(node.val,0)
            self.max = self.max if self.dict[node.val] < self.max else self.dict[node.val]
            if node.left : dfs(node.left)
            if node.right: dfs(node.right)
        if root: dfs(root)

        return [k for k in self.dict.keys() if self.dict[k] == self.max ]

        # Approach #1, brute-force, two phases
        #  1. DFS all nocdes for all vals and count in dict
        #  2. find dict keys with maximum counts
        #  
        # O(n), 18%
        self.dict = {}
        self.max  = 0
        def dfs(node):
            self.dict[node.val] = 1 + self.dict.get(node.val,0)
            self.max = self.max if self.dict[node.val] < self.max else self.dict[node.val]
            if node.left : dfs(node.left)
            if node.right: dfs(node.right)
        if root: dfs(root)

        # return [k for k in self.dict.keys() if self.dict[k] == self.max ]
        #
        # additional list space without list comprehension
        # 39%
        ans = []
        for k,v in self.dict.items():
            if v == self.max: ans.append(k)
        return ans


if __name__ == '__main__':
    s = Solution()
    # tc = [[1,None,2,2]]
    #tc = [[1,None,2,None,None,2,None]]
    tc = [[1,2,3,4,5,6,3]]
    an = [[2]]
    import helper
    t=helper.TestHelper()
    for i in range(len(tc)):
        c = t.listToBinaryTree(tc[i])
        print (s.findMode(c))
        #assert(s.findMode(c) == an[i])
