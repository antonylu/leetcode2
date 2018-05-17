"""
https://leetcode.com/problems/reverse-linked-list/description/


Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Approach #2, use 3 pointers
        # 42ms, 81%
        if not head: return head
        a = head
        b = head.next
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        head.next = None
        return a
            

        # Approach #1, use stack
        # push node to stack
        # create a new list with popped nodes
        # Time O(n), 44ms, 64%
        # space O(n)
        if not head: return head
        stack = []
        a = head
        while a:
            stack.append(a)
            a=a.next
        ans = stack.pop()
        a = ans
        while len(stack) != 0 :
            a.next = stack.pop()
            a = a.next
        a.next = None
        return ans

if __name__ == "__main__":
    import helper
    l = helper.LinkListHelper()
    tc = [[1,2,3,4,5],[6,6,6,1,2,6,3],[],[6,1,2,3,6],[1,2,2,1],[1]]
    s=Solution()
    
    ans = [True]
    for t in tc:
        t_list = l.listToLinkList(t)
        print(t)
        print(l.linkListToList(s.reverseList(t_list)))
        #assert(l.linkListToList(s.reverseList(t_list)) == t_list )