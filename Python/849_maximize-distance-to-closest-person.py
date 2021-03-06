"""
https://leetcode.com/problems/maximize-distance-to-closest-person/description/

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.

"""
xrange = range
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # Approach #1a, naive with index
        #
        # 3 conditions
        #  1. in the middle longest consecutive 0s
        #       1:1
        #       2:1
        #       3:2
        #       4:2
        #       5:3
        #       6:3
        #       n:(n+1)//2
        #  2. the first if it is 0
        #  3. the last, if it is 0
        #
        # O(n), 84ms
        #
        first0 = seats.index(1)
        last0  = seats[::-1].index(1)

        middle0 = 0
        count = 0
        for s in seats:
            if s == 0:
                count+=1
            else:
                middle0 = max(middle0, count)
                count = 0

        return max(first0, last0, (middle0+1)//2)

        # Approach #1, naive
        #
        # 3 conditions
        #  1. in the middle longest consecutive 0s
        #       1:1
        #       2:1
        #       3:2
        #       4:2
        #       5:3
        #       6:3
        #       n:(n+1)//2
        #  2. the first if it is 0
        #  3. the last, if it is 0
        #
        # O(n), 84ms
        #
        first0, last0, middle0 = 0,0,0
        while seats[first0]   == 0: first0+=1
        while seats[-last0-1] == 0: last0 +=1
        count = 0
        for s in seats:
            if s == 0:
                count+=1
            else:
                middle0 = max(middle0, count)
                count = 0

        return max(first0, last0, (middle0+1)//2)




if __name__ == '__main__':
    s = Solution()
    tc =  [ [1,0,0,0,1,0,1], [1,0,0,0] ]
    ans = [ 2, 3 ]
    for i in range(len(tc)):
        r = s.maxDistToClosest(tc[i])
        print (r)
        assert(r == ans[i])
