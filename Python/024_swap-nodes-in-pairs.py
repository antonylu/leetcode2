"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
xrange = range
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Approach #1, naive
        # 3 point to the first 3 nodes
        # swap by 
        # b.next = a
        # a.next = c
        #   redo c
        # return ans
        #
        # O(n)
        
        a = head
        if a and a.next:
            ans = a.next
        else:
            return a

        d = ListNode(0)
        
        while a and a.next:
            b = a.next
            a.next = b.next
            b.next = a
            d.next = b
            a = a.next
            d = b.next
        return ans


if __name__ == '__main__':
    s = Solution()
    tc =  [[1,2], [1,2,3],[1,2,3,4,5], [1,2,3,4] ]
    ans = [[2,1], [2,1,3],[2,1,4,3,5], [2,1,4,3] ]
    import helper 
    ll = helper.LinkListHelper() 
    
    for i in range(len(tc)):
        print( ll.linkListToList(ll.listToLinkList(tc[i])))
    
    for i in range(len(tc)):
        r = s.swapPairs(ll.listToLinkList(tc[i]))
        r = ll.linkListToList(r)
        print(r)
        assert(r == ans[i])
