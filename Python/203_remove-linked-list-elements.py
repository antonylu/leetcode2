"""
https://leetcode.com/problems/remove-linked-list-elements/description/

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Approach #1, two pointers, curr and next
        # find the ListNode with value n
        # if next.val == val
        #   curr.next = curr.next.next
        # O(n), 115ms, 38%
        if not head: return None
        ans  = head
        while ans and ans.val == val:
            ans = ans.next
        curr = ans
        while curr is not None:
            last = curr.next
            while last and last.val == val:
                curr.next = last.next
                last = last.next
            curr = curr.next
        return ans

    def removeElements(self, head, val):
        # Approach #2, recurive
        # the result depends on the next
        # escape condition
        # f(x)  = None,          for None
        #       = f(x.next)      for x.val = val
        # 155ms, 6%
        if not head: return head
        head.next = self.removeElements(head.next,val)
        return head.next if head.val == val else head
        

if __name__ == "__main__":
    import helper
    l = helper.LinkListHelper()
    tc = [[1,2,6,3,4,5,6],[6,6,6,1,2,6,3],[],[6,1,2,3,6],[1,2,2,1]]
    s=Solution()
    
    ans = [True]
    for t in tc:
        t_list = l.listToLinkList(t)
        print(t)
        print(l.linkListToList(s.removeElements(t_list,6)))

