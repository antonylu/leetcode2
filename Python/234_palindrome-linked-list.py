"""
https://leetcode.com/problems/palindrome-linked-list/description/

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Approach #1, brute force
        # convert the LinkList to a list
        # compare all items, e.g, list[0] with list[len(list)-1]
        # Time  O(n) 39%, 142ms
        # Space O(n)
        def linkListToList(list):
            """
            :type list: ListNode 
            :rtype: List
            """
            curr = list
            ans = []
            while curr:
                ans.append(curr.val)
                curr = curr.next
            return ans
        list = linkListToList(head)
        l = len(list)
        i=0
        while i < (l +1)//2: # 3: 0,1, 4: 0,1
            if list[i] != list[l-1-i]: return False
            i+=1
        return True


# Your MyQueue object will be instantiated and called as such:
if __name__ == "__main__":
    tc = [[1,2],[1,2,2,1]]
    import helper
    l = helper.LinkListHelper()
    s = Solution()
    for t in tc:
        print(s.isPalindrome(l.listToLinkList(t)))
        