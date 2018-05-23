"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Approach #2a, use collections.Counter
        # Count occurance of every element in both list and intersection
        # Oneline
        # O(n+m), 49%
        import collections
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

        
        # Approach #2, use collections.Counter
        # Count occurance of every element in both list and intersection
        # O(n+m), 33%
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        c3 = c1 & c2
        return list(c3.elements())

        # Approach #1, naive
        # Count occurance of every element in both list
        # append those shows in both list
        # 
        # O(n+m+e) 117ms, 6%
        s1=set(nums1)
        s2=set(nums2)
        d1 = {}
        d2 = {}
        ans = []
        for e in s1:
            d1[e]=nums1.count(e)
        for e in s2:
            d2[e]=nums2.count(e)
        for e in d1:
            if e in d2:
                i = min(d1[e],d2[e])
                for j in range(i):
                    ans.append(e)
        return ans
                    
                

if __name__ == '__main__':
    tc = [([1, 2, 2, 1],[2, 2]),([1,2,2,1],[1,2,1]),([],[1,2,3])]
    ans = [[2,2],[1,2,1],[]]
    s = Solution()
    for t in tc:
        print(s.intersect(t[0],t[1]))


