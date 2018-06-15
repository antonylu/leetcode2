"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Approach #1, BFS
        #
        # O(n), Python3, 99.8%
        # O(n), Python2, 
        
        from collections import deque
        if not root: return []
        q = deque([root])
        ans = []
        while len(q) >0:
            no_of_node = len(q)
            summ = 0
            for i in range(no_of_node):
                node = q.popleft()
                #print(node)
                if node:
                    summ += node.val
                    if node.left:  q.append(node.left)
                    if node.right: q.append(node.right)
            ans.append(summ/no_of_node)
        return ans
                
            
        
        


if __name__ == '__main__':
    s = Solution()
    tc  = [ [3,9,20,None,None,15,7],[3,9,20,15,7]]
    ans = [ [3, 14.5, 11], [3.0,14.5,11.0] ]
    from helper import TestHelper
    th = TestHelper()
    for i in range(len(tc)):
        t = th.listToBinaryTree(tc[i])
        r = s.averageOfLevels(t)
        print (r)
        #assert(r == ans[i])
