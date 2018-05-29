"""
https://leetcode.com/problems/path-sum-iii/description/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Approach #2, improve with dict
        # like two-sum question, use dict to save the number of nodes which has the same path_sum from root
        # for every node, find the number number of paths that ends in that node and starts from previous nodes
        # how to check? if meet, path_sum_root2end - path_sum_root2start should == target
        # i.e., for those nodes with path_sum_root2start =  path_sum_root2end - target, they can be start nodes which made the target valid
        # so, just look up for how many nodes with path_sum == path_sum_root2end - target is the answer
        #
        # expected O(n), 92%
        self.ans = 0
        d = {}
        def dfs(node,path_sum):
            d[path_sum] = d.get(path_sum,0) + 1
            path_sum += node.val
            self.ans += d.get(path_sum - sum, 0)
            #print(node.val,path_sum,self.ans,d)
            if node.left: dfs(node.left,path_sum)
            if node.right: dfs(node.right,path_sum)
            path_sum -= node.val
            d[path_sum] = d.get(path_sum,0) - 1
        
        if not root: return 0
        dfs(root,0)
        return self.ans

    def pathSum2(self, root, sum):
        # Approach #1, brute force
        # DFS every node and as if we take that node as starting root
        # with the every new root DFS every child node and check if the path sum == 8
        # O(n^2) 993ms, 55%
        ans = [0]
        def dfs(node, path_sum):
            path_sum += node.val
            if path_sum == sum:
                ans[0] += 1
            if node.left: dfs(node.left,path_sum)
            if node.right: dfs(node.right,path_sum)

        if not root: return 0
        
        def dfs2(node):
            dfs(node, 0)
            if node.left: dfs2(node.left)
            if node.right: dfs2(node.right)

        dfs2(root)
        return ans[0]
            
            
        
if __name__ == '__main__':
    s = Solution()
    tc = [([10,5,-3,3,2,None,11,3,-2,None,1],8),([5,3,2,3,-2,None,1],8),([],1)]
    #tc = [([10,5,-3,3,2,None,11,3,-2,None,1],8)]
    #tc = [([5,3,2,3,-2,None,1],8)]
    an = [3,2,0]
    import helper
    th = helper.TestHelper()
    for t in tc:
        print(s.pathSum(th.listToBinaryTree(t[0]),t[1] ))
