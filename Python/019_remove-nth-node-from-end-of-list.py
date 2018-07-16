"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""
xrange = range
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Approach #1, two pass
        # 1 pass to know how many nodes, m
        # 2 pass to remove the m-n node
        #
        # O(n), 24ms, 100%
        #

        # get total number of nodes
        curr = head
        total = 1
        while curr.next:
            curr = curr.next
            total +=1
        if total == 1: return None

        # find the total-n node
        target = total - n
        if target <= 0: return head.next
        count = 1
        curr = head
        while count != target:
            curr = curr.next
            count +=1

        curr.next = curr.next.next
        return head


if __name__ == '__main__':
    s = Solution()
    tc =  [ ([1,2,3,4,5],2),([1],1),([1,2],2) ]
    ans = [ [1,2,3,5], [], [2] ]
    from helper import LinkListHelper
    llh =  LinkListHelper()

    for i in range(len(tc)):
        t = llh.listToLinkList(tc[i][0])
        r = s.removeNthFromEnd(t, tc[i][1])
        r = llh.linkListToList(r)
        print(r)
        assert(r == ans[i])
