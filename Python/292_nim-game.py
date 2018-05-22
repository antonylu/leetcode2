"""
https://leetcode.com/problems/nim-game/description/


You are playing the following Nim Game with your friend: There is a heap of stones on the table, 
each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. 
You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. 
Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.
"""
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach #1,
        # It looks like the terrifying 30 game
        # A simple %4 can determine the result
        # 1,2,3: True
        # 4: False
        # 5,6,7: True
        # 8: False
        # lost number is n which n%(3+1)=0, i.e, 4,8,12,16, etc...
        # 
        # O(1), 97%
        return n%4 != 0
        
        
        

if __name__ == "__main__":
    tc = [4,5,6,7,8,9,10,11,12]
    ans = [True, False, False, False]
    s = Solution()
    for t in tc:
        print(s.canWinNim(t))
