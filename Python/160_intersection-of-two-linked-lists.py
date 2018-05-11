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
        # Approach #3, TODO
        # a trick that traversal twice for both lists at the same time
        # Similar to "turtle and rabbit race", if they have intersection, consder one list is a head of another list with x nodes
        # connect end of a to start of b, connect end of b to start of a
        # two animals should traverse both list with the same distance
        # a stops at end of list b, and b stops at end of list a
        # if there is a intersection, they should be stopped at the same end nodes
        # if no intersection, they stop at different nodes
        # O(m+n)
        # 95%, 345ms
        a = headA
        b = headB
        while a is not b:
            if a is None: 
                a = headB
            else:
                a = a.next
            if b is None: 
                b = headA
            else:
                b = b.next

        return a
        

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
    
    
