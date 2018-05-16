""" 
Leetcode Test Helper

listToBinaryTree()
Given a List, return a Binary Tree 

For example:
Given a list [3,9,20,None,None,15,7]
return a binary tree 
    3
   / \
  9  20
    /  \
   15   7
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class TestHelper(object):
    def listToBinaryTree(self, list):
        """
        :type list: List[int]
        :rtype: TreeNode
        """
        # Approach 1: 
        # Suppose the list is complete
        # Brute force, BFS create nodes and link it
        if len(list) == 0: return None
        root = TreeNode(list.pop(0))
        q = deque([root])
        while(len(list) > 0):
            current_node = q.popleft()
            i = list.pop(0)
            if i:
                n = TreeNode(i)
                current_node.left = n
                q.append(n)
            if(len(list)>0):
                i = list.pop(0)
                if i:
                    n = TreeNode(i)
                    current_node.right = n
                    q.append(n)
        return root

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkListHelper(object):
    def listToLinkList(self, list):
        """
        :type list: List[int]
        :rtype: ListNode
        """
        # Approach #1
        # Brute force 
        dummy_head = ListNode(0)
        current_node = dummy_head 
        for i in list:
            current_node.next = ListNode(i)
            current_node = current_node.next
        return dummy_head.next
            
    def linkListToList(self, list):
        """
        :type list: ListNode 
        :rtype: List
        """
        curr = list
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans
