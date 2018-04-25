# https://leetcode.com/problems/merge-two-sorted-lists/description/
# 
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # brute force, iterative, compare nodes in two list one by one
        # append to the new list
        # refactor, don't check end. If one of the list is ended, append the none-ended list to the new list
        # O(n), 97%, 46ms 

        ml = ListNode(0)
        cur = ml

        while (l1 and l2):
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        cur.next = l1 or l2

        return ml.next

        

d = Solution()
print(d.mergeTwoLists())

