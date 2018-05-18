"""
https://leetcode.com/problems/delete-node-in-a-linked-list/description/

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Approach #1, brute-force
        #
        # at first glance it looks like it is an impossible question
        # in the example, if we want to remove node 3, we need to set 2.next = 4
        # How can we access 2.next?
        #
        # Thinking out of box.
        # if we can't modify the next, can we modify val, and makes 3->4, 4->None?
        #
        # O(n), 64ms
        while node.next:
            node.val = node.next.val
            tmp = node
            node = node.next
        tmp.next = None
            
                
if __name__ == "__main__":
    tc = [1,2,3,4]
    s = Solution()
    import helper
    LLH = helper.LinkListHelper()
    head  = LLH.listToLinkList(tc)
    node3 = head.next.next

    print(LLH.linkListToList(head))
    s.deleteNode(node3)
    print(LLH.linkListToList(head))
