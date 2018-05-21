"""
https://leetcode.com/problems/first-bad-version/description/


You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
#    return version >= 1702766719
    return version >= 4
#2126753390 versions
#1702766719 is the first bad version.

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #2, binary search
        # O(log n), 30ms, 88%
        max = n
        min = 1
        while min <= max:
            mid = (max+min)//2
            if isBadVersion(mid):
                max = mid -1
            else:
                min = mid +1
        while not isBadVersion(mid): mid+=1
        return mid
        

        # Approach #1, naive, linear search from 1st version
        #
        # result is n if 
        # f(n)   returns True
        # f(n-1) returns False
        #
        # O(n)
        # Memory with range
        for v in range(1,n+1):
            if isBadVersion(v): return v-1
        # Time Limit Exceeded
        v=1
        while not isBadVersion(v): v+=1
        return v
        
        

if __name__ == "__main__":
    tc = [9,6,4,12,7]
    #tc = [2126753390]
    s = Solution()
    for t in tc:
        print(s.firstBadVersion(t) )
