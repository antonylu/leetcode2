"""

Given a array of non-negative integers, 
Find the maximum sum of continuous L integers and continuous R integers, where all the index of those L intergers are smaller than the index of those R integers.

Example 1:
[10,3,9,4,5,1,13], L=2, R=3
Result = 32, 
the 2 of left parts are 10 and 3
the 3 of right parts are 5,1,13

Example 2:
[4,1,2,1,5], L=2, R=2
Result = 13, 
the 2 of left parts are 4,1
the 3 of right parts are 2,1,5

Example 3:
[1,1,2,5,3,1,1,1,7], L=2, R=3
Result = 17, 
the 2 of left parts are 5,3
the 3 of right parts are 1,1,7


"""

class Solution(object):
    # Approach #1, brute force, enumerate all possible cases and keep the maximum
    def maxLeftRight(self, lst, L, R):
        """
        :type lst: list of Non-negative int
        :type L: int
        :type R: int
        :rtype: int
        """
        maxi = 0
        for i in range(len(lst)-L-R+1):
            for j in range(i+L,len(lst)-R+1):
                maxi = max(maxi, sum(lst[i:i+L]) + sum(lst[j:j+R]))
        return maxi

if __name__ == "__main__":
    s=Solution()
    tc = [[10,3,9,4,5,1,13], [4,1,2,1,5],[1,1,2,5,3,1,1,1,7]]
    for t in tc:
        print(s.maxLeftRight(t,2,3))
