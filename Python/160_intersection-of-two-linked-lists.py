""" 
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Approach #2, use hash table or set to speed up lookup
        # O(n)+O(m)
        # 56%, 381ms
        s = set()
        a = headA
        while a is not None:
            s.add(a)
            a = a.next
        b = headB
        while b is not None:
            if b in s: return b
            b = b.next
        return None
        

        # Approach #1, brute force. Search every node of A in list B
        # O(n*m)
        # Time Limit Exceeded
        a = headA
        while a is not None:
            b = headB
            while b is not None:
                if a is b: 
                    return a
                else:
                    b = b.next
            a = a.next
        return None


if __name__ == "__main__":
    s=Solution()
    listA = ListNode(1)
    listB = ListNode(2)
    listA.next = listB
    print(s.getIntersectionNode(listA,listB))
    
    
