""" 
https://leetcode.com/problems/linked-list-cycle/description/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Approach #1 enumerate, use hash table to keep every node
        # return false if next is None
        # return true if next is in hash keys
        # O(n), 182ms 0%
        node = head 
        dict ={}
        while node:
            if node in dict:
                return True
            dict[node] = 1
            node=node.next
        return False    


if __name__ == "__main__":
    tc  = []
    ans = []
    s = Solution()
    for i,t in enumerate(tc):
        print (s.hasCycle(t))
        if(s.hasCycle(t) != ans[i]): print("incorrect: ",i,t)

