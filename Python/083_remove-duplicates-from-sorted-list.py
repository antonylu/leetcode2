""" 
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Approach 1: enumerate each node, remove the same nodes in-place
        # current: to compare, if same, check next node, if different, concatenate nodes then check next
        # check: to be checked node
        # O(n^2?)
        # 23%, 61ms
        """
        if head == None: return None
        current = head
        check = head.next
        while current is not None:
            while check is not None and current.val == check.val:
                current.next = check.next
                check=check.next
            current = current.next
        return head
        """
        # Approach 2: enumerate each node, remove the same nodes in-place
        # 
        # O(n), 99%, 50ms
        if head == None: return head
        current = head
        check = head.next
        while(check != None):
            if (current.val == check.val):
                current.next = check.next
                check = current.next
            else:
                current = current.next
                check   = check.next
        return head        
s = Solution()
test_case = [[],[1,1,2],[1,1,2,3,3]]
#test_case = [[1,1,2,3,3]]
#test_case = [[1,1,2]]

for i in test_case:
    head = ListNode(0)
    current = head
    for j in i:
        a = ListNode(j)
        current.next = a
        current = a
    s.deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next
