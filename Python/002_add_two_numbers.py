# https://leetcode.com/problems/add-two-numbers/description/
# 
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # List Operation, add node one by one, add carry node when necessary
        # Time  O(n), beats 69.33%, 142ms
        # Space O(n)
        result = ListNode(0)
        curr = result
        carry = 0
        while (l1 != None or l2 != None):
            n1 = n2 = 0
            if l1!= None: 
                n1=l1.val
                l1=l1.next
            if l2!= None: 
                n2=l2.val
                l2=l2.next
            s = n1 + n2 + carry
            carry = s/10
            s = s % 10
            curr.next = ListNode(s)
            curr = curr.next

        if carry!=0:
            curr.next = ListNode(carry)
        
        return result.next
