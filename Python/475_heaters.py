"""
https://leetcode.com/problems/heaters/description/

You are given a map in form of a two-dimensional iWinter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.

Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.s
"""
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # Approach #1b, binary search 
        # optimise by
        #  1. remove list 57%
        #  2. remove min() 86%
        #  3. remove corner case checks in loop
        # Space O(1)
        # Time  O(nlogn), 97.63%
        heaters.sort()
        heaters = [-2147483647] + heaters + [2147483648]
        maximum = 0
        from bisect import bisect
        for h in houses:
            i = bisect(heaters,h)
            d1 = heaters[i]-h
            d2 = h - heaters[i-1]
            d = d1 if d1<d2 else d2
            maximum = maximum if maximum > d else d
        return maximum
        
        # Approach #1a, binary search 
        # optimise by
        #  1. remove list 57%
        #  2. remove min() 86%
        # Space O(1)
        # Time  O(nlogn), 
        heaters.sort()
        maximum = 0
        from bisect import bisect
        for h in houses:
            i = bisect(heaters,h)
            if i == 0: d = heaters[i]-h
            elif i == len(heaters): d = h - heaters[len(heaters)-1]
            else:
                d1 = heaters[i]-h
                d2 = h - heaters[i-1]
                d = d1 if d1<d2 else d2
            maximum = maximum if maximum > d else d
        return maximum
        
        # Approach #1, binary search 
        #
        # for every hose, find it's nearest heater
        # sort, then binary search 
        # find the max value of all min distance
        # 
        # Time  O(m logn), 32%
        # Space O(m)
        #
        # houses.sort() # no need to sort houses, 36%
        heaters.sort()
        distances = []
        from bisect import bisect
        for h in houses:
            i = bisect(heaters,h)
            if i == 0: d = heaters[i]-h
            elif i == len(heaters): d = h - heaters[len(heaters)-1]
            else:
                d = min(heaters[i]-h, h - heaters[i-1])
            distances.append(d)
        return max(distances)


if __name__ == '__main__':
    s = Solution()
    tc = [([1,2,3],[2]), ([1,2,3,4],[1,4]),([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])]
    an = [1,1,161834419]
    for i in range(len(tc)):
        print (s.findRadius(tc[i][0],tc[i][1]))
        assert(s.findRadius(tc[i][0],tc[i][1]) == an[i])
